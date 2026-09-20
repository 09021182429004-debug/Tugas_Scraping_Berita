import pandas as pd

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

except FileNotFoundError:
    print(f"File '{file_path}' tidak ditemukan! Pastikan file 'Data_BPS.csv' sudah ada.")
except Exception as e:
    print(f"Terjadi error: {e}")