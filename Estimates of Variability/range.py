import pandas as pd
import os

'''
Range is different betweent the largest and the smallest value inn the data set
'''
#import data  as  DataFrame
file_path = os.path.join('..', 'Estimates of Locations', 'data.csv')
df = pd.read_csv(file_path, delimiter=';')

#using Varable min-max
max = df['Score'].max()
min = df['Score'].min()
print(max)
print(min)
range = max - min
print(range)

#one liner
data_range = df['Score'].max() - df['Score'].min()
print(data_range)