import pandas as pd
import matplotlib.pyplot as plt
import  os 

file_path = os.path.join('..', 'Estimates of Locations', 'data.csv')
df = pd.read_csv(file_path, delimiter=';')
data = df['Score']

# Histogram
plt.hist(data, bins=30, alpha=0.7, color='blue')
plt.title("Histogram Data")
plt.xlabel("Nilai")
plt.ylabel("Frekuensi")
plt.show()