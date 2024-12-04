import pandas as pd
import os

'''
 Median Absolute Deviation (MAD) is a median of the absolute deviations from the dataset's median. It is  a robust statistical measure that quantifies the variability in a dataset.
'''

#import data  as  DataFrame
file_path = os.path.join('..', 'Estimates of Locations', 'data.csv')
df = pd.read_csv(file_path, delimiter=';')

'''
Step by step  to calculate median absolute deviation
'''
#1.Calculate the median
median =  df['Score'].median()

#2. Calculate Absolute deviation from the median
df['absolute_deviation'] = abs(df['Score'] - median)

#3. Calculate Median from absolute deviation
mad  =  df['absolute_deviation'].median()

print("Median is: ", median)
print('Median absolute deviation is: ', mad)
