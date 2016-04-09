#!/usr/bin/python3
import pandas as pd
from urllib.request import urlopen

# Read in US population data
# data = pd.read_csv('../uspop.csv')
us_pop = pd.read_csv('./uspop.csv')

# Read in homeless population data
url = 'https://www.hudexchange.info/resources/documents/2007-2015-PIT-Counts-by-CoC.xlsx'
socket = urlopen(url)
xd = pd.ExcelFile(socket)
df = xd.parse(xd.sheet_names[-1], header=None)
