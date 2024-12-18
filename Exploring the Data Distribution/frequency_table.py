import pandas as pd
import matplotlib.pyplot as plt
import os

# Load the CSV file
file_path = os.path.join('..', 'Estimates of Locations', 'data.csv')
df = pd.read_csv(file_path, delimiter=';')

# CreateFrequency Table
df['Interval'] = pd.cut(df['Score'], bins=[40, 49, 59, 69, 79])

#Frequency Table
frequency_table = df['Interval'].value_counts().sort_index().reset_index()
frequency_table.columns = ['Interval Kelas', 'Frekuensi']

# Menambahkan Frekuensi Relatif dan Kumulatif
frequency_table['Frekuensi Relatif (%)'] = (frequency_table['Frekuensi'] / len(df)) * 100
frequency_table['Frekuensi Kumulatif'] = frequency_table['Frekuensi'].cumsum()

print(frequency_table)

# Plotting grafik bar
plt.figure(figsize=(8, 6))
plt.bar(frequency_table['Interval Kelas'].astype(str), frequency_table['Frekuensi'], color='skyblue', edgecolor='black')
plt.title("Distribusi Frekuensi", fontsize=14)
plt.xlabel("Interval Kelas", fontsize=12)
plt.ylabel("Frekuensi", fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# Menampilkan grafik sebagai pop-up
plt.show()

# Menampilkan tabel sebagai grafik
fig, ax = plt.subplots(figsize=(8, 4))  # Mengatur ukuran
ax.axis('tight')  # Menyesuaikan ukuran tabel dengan grafik
ax.axis('off')    # Menghilangkan sumbu pada grafik

# Membuat tabel
table = ax.table(
    cellText=frequency_table.values,  # Isi tabel
    colLabels=frequency_table.columns,  # Header tabel
    cellLoc='center',  # Lokasi teks dalam sel
    loc='center'  # Lokasi tabel pada grafik
)

table.auto_set_font_size(False)
table.set_fontsize(10)  # Ukuran font
table.auto_set_column_width(col=list(range(len(frequency_table.columns))))  # Penyesuaian lebar kolom

plt.title("Tabel Frekuensi", fontsize=14, pad=20)  # Judul tabel
plt.show()