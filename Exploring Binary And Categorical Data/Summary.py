import pandas  as  pd
import os

#Read CSV File
file_path = os.path.join('..', 'Estimates of Locations', 'data.csv')
df = pd.read_csv(file_path, delimiter=';')

#1.  Mode
mode = df['Score'].mode()
print(mode)

#2. Expected Value