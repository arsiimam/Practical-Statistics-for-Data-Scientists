import pandas as pd
from scipy.stats import trim_mean #using scipy

df = pd.read_csv('data.csv', delimiter=';')

#Specify the triming ratio
triming_ratio = 0.1 #For example 10%
trimmed_mean = trim_mean(df['Score'], triming_ratio)
print(trimmed_mean)

#Trimmed mean for spesific subject
trimed_mean_subject = trim_mean(df[df['Subject']=='Math']['Score'], triming_ratio)
print('Trimed meanfor subject math is: ',trimed_mean_subject)

#Trimed mean for spesific subject with dynamic filter
subject_filter = 'English'#Change with anything inside subject coloumn

trimmed_mean_dynamic = trim_mean(df[df['Subject']==subject_filter]['Score'],triming_ratio)
print('Trimed mean for subject ',subject_filter,' is: ',trimmed_mean_dynamic)