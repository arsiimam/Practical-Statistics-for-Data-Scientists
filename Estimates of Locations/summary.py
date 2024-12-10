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
print('Mode of the  score  is: ', mode)

#4.Calculate Perceltile
percentiles = [25, 50, 75]
results = df['Score'].quantile([p / 100 for p in percentiles])
print(results)

#5. Trimmed Mean
triming_ratio = 0.1 #For example 10%
trimmed_mean = trim_mean(df['Score'], triming_ratio)
print(trimmed_mean)