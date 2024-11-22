import pandas as pd

#import dataset from data.csv as a pandas DataFrame
df = pd.read_csv('data.csv', delimiter=';')

#Weighted mean
weighted_mean = (df['Score'] * df['Weight']).sum() / df['Weight'].sum()

#Print Weighted Mean
print('Weighted Mean: ', weighted_mean)


#Weighted Mean With Filtered Subject : english
filtered_weighted_mean = ((df[df['Subject'] == 'English']['Score']) * df[df['Subject']=='English']['Weight']).sum() / df[df['Subject'] == 'English']['Weight'].sum()

print('Filtered Weigthed Mean: ', filtered_weighted_mean)

#Weighted Mean with dynamic filter
#This variabel used as dynamic vilter. 
#It can be change with any value inside subject
subject_filter = 'Math' 
#Calculate diltered Mean with dynamic filter
dynamic_filtered_mean = ((df[df['Subject'] == subject_filter]['Score'])*df[df['Subject'] == subject_filter]['Weight']).sum() / df[df['Subject']== subject_filter]['Weight'].sum()

print('weighted Mean for subject', subject_filter, "is ",dynamic_filtered_mean)

