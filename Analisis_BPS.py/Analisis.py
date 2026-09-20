import pandas as pd
import matplotlib.pyplot as plt

file_path = "Data_BPS.csv"

try:
    df = pd.read_csv(file_path)
    print("==========================================")
    print("        HASIL ANALISIS DATA BPS           ")
    print("==========================================")
    
    print("\n1. 5 Data Pertama:")
    print(df.head().to_string(index=False))
    
    print("\n2. Ringkasan Statistik Deskriptif:")
    stats_deskriptif = df.describe()
    print(stats_deskriptif.round(2).to_string())
    
    stats_deskriptif.to_csv("hasil_analisis_bps.csv")
    print("\n==========================================")
    print("Berhasil! Hasil analisis tersimpan di 'hasil_analisis_bps.csv'")
    print("==========================================")

    top_10 = df.nlargest(10, 'Jumlah Penduduk (Ribu)').sort_values('Jumlah Penduduk (Ribu)', ascending=True)
    
    plt.figure(figsize=(10, 6))
    plt.barh(top_10['Provinsi'], top_10['Jumlah Penduduk (Ribu)'])
    plt.title('10 Provinsi dengan Jumlah Penduduk Terbanyak')
    plt.xlabel('Jumlah Penduduk (Ribu Jiwa)')
    plt.ylabel('Provinsi')
    plt.tight_layout()
    
    plt.savefig('grafik_bps.png')
    print("Gambar grafik tersimpan sebagai 'grafik_bps.png'")
    
    plt.show()

except FileNotFoundError:
    print(f"File '{file_path}' tidak ditemukan! Pastikan file 'Data_BPS.csv' sudah ada.")
except Exception as e:
    print(f"Terjadi error: {e}")
