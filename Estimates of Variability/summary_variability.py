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