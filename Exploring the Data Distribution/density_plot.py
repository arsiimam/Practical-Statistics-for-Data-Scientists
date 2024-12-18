import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import pandas as pd

# Load the CSV file
file_path = os.path.join('..', 'Estimates of Locations', 'data.csv')
df = pd.read_csv(file_path, delimiter=';')

#Creating density plot
sns.kdeplot(df['Score'], shade=True, color='blue', alpha = 0.7)

#Creating label
plt.title('Density Plot For Score')
plt.xlabel('Scores')
plt.ylabel('Density')
plt.show()