import numpy as np

# Data dari Soal 1
data = [165, 170, 160, 155, 175, 180, 165, 170, 160, 155,175, 180, 165, 170, 160, 155, 175, 180, 165, 170]

# Standar deviasi untuk populasi (dengan ddof=0)
pop_std_dev = np.std(data, ddof=0)

# Standar deviasi untuk sampel (dengan ddof=1)
sample_std_dev = np.std(data, ddof=1)

print("Standar Deviasi Populasi: ", pop_std_dev)
print("Standar Deviasi Sampel: ", sample_std_dev)