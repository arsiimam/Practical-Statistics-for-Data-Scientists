import numpy as np
import seaborn as sns
import pandas as pd
import  os
import matplotlib.pyplot as plt


#Read CSV File
file_path = os.path.join('..', 'Estimates of Locations', 'data.csv')
df = pd.read_csv(file_path, delimiter=';')


# Expected value
expected_value = np.mean(df['Score'])
print(expected_value)

# Distribution Plot
sns.histplot(df['Score'], kde=True, color='blue', alpha=0.6)
plt.axvline(expected_value, color='red', linestyle="--", label=f'Expected Value: {expected_value:.2f}')

plt.title('Data Distribution Using Expected Value')
plt.xlabel('Score')
plt.ylabel('Frequency')
plt.legend()
plt.show()