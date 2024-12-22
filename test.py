import numpy as np

# Data dari Soal 1
data = [50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145]

# Standar deviasi untuk populasi (dengan ddof=0)
pop_std_dev = np.std(data, ddof=0)

# Standar deviasi untuk sampel (dengan ddof=1)
sample_std_dev = np.std(data, ddof=1)

print("Standar Deviasi Populasi: ", pop_std_dev)
print("Standar Deviasi Sampel: ", sample_std_dev)