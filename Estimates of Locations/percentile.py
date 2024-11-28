import pandas as pd

#Create Dataframe and import data.csv
df = pd.read_csv('data.csv', delimiter=';')

percentiles = [25, 50, 75]

#calculate the 25th percentiles, 50th (median) and 75
results = df['Score'].quantile([p / 100 for p in percentiles])
print(results)

#Calculate percentiles for with filter spesific subject
results_subject= df[df['Subject']=='Math']['Score'].quantile([p / 100 for p in percentiles])
print('Percentiles of Subject Math is: ',results_subject)

#Calculate percenttiles using dynamic subject filter
subject_filter = 'English'
results_subject_dynamic = df[df['Subject']== subject_filter]['Score'].quantile([p / 100 for p in percentiles])
print('Percentiles  for subject ',subject_filter, 'is:', results_subject_dynamic)