import pandas as pd
import  os

'''
Variance measures the average of the squared differences between each data point and the mean, reflecting the data's overall spread.
'''

#import data  as  DataFrame
file_path = os.path.join('..', 'Estimates of Locations', 'data.csv')
df = pd.read_csv(file_path, delimiter=';')

#n
N = df['Score'].count() 
n =  N - 1
#Step by step to calculate a variance
#1. Calculate the mean
mean = df['Score'].mean()

#2. Calculate deviation from the mean
df['deviation'] = df['Score'] -  mean

#3. Calculate the square of deviation
df['square_deviation'] = df['deviation'] ** 2

#4. Sum the square of deviations
sum_square_deviation = df['square_deviation'].sum()

#5. Calculate the variance
#for N total population
populations_variance = sum_square_deviation / N

#for n sample (ex : 5)
sample_variance = sum_square_deviation/n

print('Variance for populations (N = 1000): ', populations_variance)
print('Variace for Sample (n =  N -1) : ',sample_variance)