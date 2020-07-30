# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 10:29:11 2020

@author: Mumes
"""

#DATA LOADING

#Import libraries
from urllib.request import urlretrieve
import pandas as pd

# Assign url of file: url
url = 'https://covid.ourworldindata.org/data/owid-covid-data.csv'

# Save file locally
urlretrieve(url, r'C:\Users\Mumes\Desktop\COVID\data\data.csv')

# Read file
dataset= pd.read_csv(r'C:\Users\Mumes\Desktop\COVID\data\data.csv')
data = dataset.copy()


#DATA CLEANING

# Delete World and International location
data.location.unique()
filter_loc = (data.location != 'World') & (data.location != 'International') 
df = data[filter_loc]
df.location.unique()
df.shape

# Delete columns
df.columns
df.drop( columns = ['iso_code','total_cases_per_million','new_cases_per_million', 'total_deaths_per_million',
                    'new_deaths_per_million','new_tests_per_thousand',
                    'new_tests_smoothed', 'new_tests_smoothed_per_thousand', 'tests_units',
                    'stringency_index', 'population_density','median_age',
                    'aged_65_older', 'aged_70_older','gdp_per_capita', 'extreme_poverty',
                    'cardiovasc_death_rate', 'diabetes_prevalence', 'handwashing_facilities', 'hospital_beds_per_thousand',
                    'life_expectancy', 'female_smokers','male_smokers', 'new_tests', 'total_tests',
                    'total_tests_per_thousand'], inplace = True)
df.shape

# Convert float variables to int
df.info()
df['total_cases'] =df['total_cases'].astype(int)
df['new_cases'] =df['new_cases'].astype(int)
df['total_deaths'] =df['total_deaths'].astype(int)
df['new_deaths'] =df['new_deaths'].astype(int)
df['population'] =df['population'].astype(int)


#Replace Nan values with 0
df['total_cases']= df['total_cases'].fillna(0)
df['new_cases']= df['new_cases'].fillna(0)
df['total_deaths']= df['total_deaths'].fillna(0)
df['new_deaths']= df['new_deaths'].fillna(0)
df.info()

#DATA MANIPULATION

#Create month and year columns
df['month'] = pd.DatetimeIndex(df['date']).month
df['year'] = pd.DatetimeIndex(df['date']).year

# Unify North America and South America in unique America country
df.continent.unique()
df.continent = df.continent.str.replace( 'North America','America')
df.continent = df.continent.str.replace( 'South America','America')
df.continent.unique()

#Filter data frame year 2020
filter_2020 = (df.year != 2019) 
df_2020 = df[filter_2020]

#Save dataframe locally
df_2020.to_csv(r'C:\Users\Mumes\Desktop\COVID\data\data_cleaned.csv')




