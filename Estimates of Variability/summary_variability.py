import pandas as pd
import os

file_path = os.path.join('..', 'Estimates of Locations', 'data.csv')
df = pd.read_csv(file_path, delimiter=';')


#1. Deviation
#Calculate the Mean
mean = df['Score'].mean()
#Calculate deviation of each value
df['deviation'] = df['Score'] - mean
print(df['Score'], df['deviation'])

#2.Std_deviation
std_deviation = df['Score'].std(ddof=0)
print('Standard Deviation : ', std_deviation)

#3. Range
range = df['Score'].max() - df['Score'].min()
print('Range : ',range)

#4. Mean Absolute deviation
mean = df['Score'].mean()
df['deviation'] = abs(df['Score']-mean)
abs_deviation = df['deviation'].sum()
count_score = df['Score'].count()
mad  = abs_deviation / count_score
print('Mean Absolute Deviation : ',mad)

#5. Median ABsolute Deviation
median = df['Score'].median()
df['absolute_deviation'] = abs(df['Score'] - median)
median_absolute_deviations = df['absolute_deviation'].median()
print('Median Absolute Deviation  is :  ', median_absolute_deviations)
