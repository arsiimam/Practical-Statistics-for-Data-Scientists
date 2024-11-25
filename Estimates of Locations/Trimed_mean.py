import pandas as pd
from scipy.stats import trim_mean #using scipy

df = pd.read_csv('data.csv', delimiter=';')

#Specify the triming ratio

triming_ratio = 0.1 #For example 10%

trimmed_mean = trim_mean(df['Score'], triming_ratio)

print(trimmed_mean)

