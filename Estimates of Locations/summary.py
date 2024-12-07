import pandas as pd

df = pd.read_csv('data.csv', delimiter = ';')

#1. Calculate  The Mean
mean = df['Score'].mean()
print('Mean  of the score is: ',mean)

#2. Calculate  Median
median = df['Score'].median()
print('Median of the Score is: ', median)

#3.  Calculate  mode
mode = df['Score'].mode()
print('Mode of teh score  is: ', mode)
