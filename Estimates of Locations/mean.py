import pandas as pd

#import data set from data.csv as pandas DataFrame
df = pd.read_csv('data.csv', delimiter=';')


#Mean formulas using .mean() function
mean_score = df['Score'].mean()
print(mean_score)

#Mean manual formulas
mean_manual = df['Score'].sum() / df['Score'].count()
print(mean_manual)

#Mean with spesific category. For example : math
mean_score_math = df[df['Subject'] == 'Math']['Score'].mean()
print(mean_score_math)

#Mean With Spesific Category and Dynamics Filter
filer_subject = 'English' #You can  change this value to anything inside the subject
mean_score_filtered = df[df['Subject'] == filer_subject]['Score'].mean()
print(mean_score_filtered)