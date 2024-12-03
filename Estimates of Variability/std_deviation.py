import pandas as pd
import  os
file_path = os.path.join('..', 'Estimates of Locations', 'data.csv')
df = pd.read_csv(file_path, delimiter=';')

#Calculate Stadard Deviation Using pandas.std()
std_score = df['Score'].std(ddof=0)
mean = df['Score'].mean()

print(std_score)
print(mean)