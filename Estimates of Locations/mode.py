import pandas as pd

#Import data and Create DataFrame
df  = pd.read_csv('data.csv', delimiter = ';')

#calculate mode of score using .mode()  function
mode_result = df['Score'].mode()
print(mode_result)

#Mode in spesific subject
mode_subject = df[df['Subject']=='Math']['Score'].mode()
print('Mode from  the subject math is: ', mode_result)

