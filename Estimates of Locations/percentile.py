import pandas as pd

df = pd.read_csv('data.csv', delimiter=';')

percentiles = [25, 50, 75]

#calculate the 25th percentiles, 50th (median) and 75
results = df['Score'].quantile([p / 100 for p in percentiles])

print(results)