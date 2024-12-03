#Mean Absolut Deviation (MAD) is a mean of absolute value of deviation from the mean
import pandas as pd
import os

file_path = os.path.join('..', 'Estimates of Locations', 'data.csv')
df = pd.read_csv(file_path, delimiter=';')

#Step By Step to Calculate MAD
#1.Calculate mean from All data. Exm : score
mean = df['Score'].mean()

#2. Calculate Absolute Deviation between each value in data and the mea
df['deviation'] = abs(df['Score'] - mean)

#3.Sum all absolute deviation
abs_deviation = df['deviation'].sum()

#4.count of Score : 1000
count_score = df['Score'].count()
print(count_score)

#5. Divide the sum of the absolute deviations by the number of data points (𝑛)
mad = abs_deviation / count_score

print('Mean Absolute Deviation is: ', mad)