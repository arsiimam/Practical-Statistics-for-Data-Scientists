import pandas as pd
import os

file_path = os.path.join('..', 'Estimates of Locations', 'data.csv')
df = pd.read_csv(file_path, delimiter=';')

#Calculate the Mean
mean = df['Score'].mean()

#Calculate deviation of each value
df['deviation'] = df['Score'] - mean
print(df['Score'], df['deviation'])

#Calculate deviattionn for spesific subject
mean_math = df[df['Subject']== 'Math']['Score'].mean()
df['NewDeviation'] = df[df['Subject']=='Math'] - mean_math
print(df[df['Subject']=='Math']['Score'], df['NewDeviation'])