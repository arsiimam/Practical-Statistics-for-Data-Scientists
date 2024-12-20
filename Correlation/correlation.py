import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Read the data of F1 lip times
df = pd.read_csv('lap_times.csv')

# Fungsi untuk mengonversi waktu ke detik, menangani format jam:menit:detik dan menit:detik
def time_to_seconds(time_str):
    parts = time_str.split(':')
    
    # Jika ada 3 bagian (jam, menit, detik)
    if len(parts) == 3:
        h, m, s = map(float, parts)
        return h * 3600 + m * 60 + s
    
    # Jika hanya ada 2 bagian (menit:detik)
    elif len(parts) == 2:
        m, s = map(float, parts)
        return m * 60 + s
    
    # Jika format tidak valid
    else:
        return None
# Mengonversi kolom waktu ke detik
df['time_seconds'] = df['time'].apply(time_to_seconds)


df_filtered = df[df['raceId'] == 1131]

# Membuat hexbin plot untuk visualisasi hubungan antara 'time_seconds' dan 'position'
plt.figure(figsize=(8, 6))
plt.hexbin(df['time_seconds'], df['position'], gridsize=50, cmap='Blues')

# Menambahkan color bar untuk menunjukkan jumlah titik dalam setiap bin
plt.colorbar(label='Jumlah Titik')

plt.title('Hexbin Plot antara Waktu dalam Detik dan Posisi')
plt.xlabel('Waktu dalam Detik')
plt.ylabel('Posisi')

plt.show()