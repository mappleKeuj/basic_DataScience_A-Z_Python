#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 14:47:38 2018

@author: jdelfrate
"""

import pandas as pd
import datetime as dt

# input data
inputData = '/home/jdelfrate/Documents/basics_python_data/guns.csv'
# read data csv file
guns_data = pd.read_csv(inputData, sep=',')
# get data frame header into
hdr = list(guns_data.columns.values)

# column year
year_data = guns_data.loc[:,'year'].values
# Count how many death per year
year_count = {}
for year in year_data:
    if year in year_count:
        year_count[year] += 1
    else:
        year_count[year] = 1

# column month
month_data = guns_data.loc[:,'month'].values
# creation of object dates = dt.datetime
dates = [dt.datetime(year = year, month = month_data[x], day = 1) for x, year in enumerate(year_data)]
# Count how many elements per date
date_count = {}
for date in dates:
    if date in date_count:
        date_count[date] += 1
    else:
        date_count[date] = 1