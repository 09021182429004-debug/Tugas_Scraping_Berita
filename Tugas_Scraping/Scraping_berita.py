import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.antaranews.com/terkini"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

try:
    response = requests.get(url, headers=headers, timeout=10)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        data_berita = []

        # Mencari elemen artikel berita
        articles = soup.find_all("article")
        if not articles:
            articles = soup.find_all("div", class_=lambda x: x and ("post" in x or "card" in x or "article" in x))

        for article in articles:
            title_tag = article.find("h3") or article.find("h2") or article.find("a")
            if title_tag:
                a_tag = title_tag.find("a") if title_tag.name != "a" else title_tag
                if a_tag and a_tag.text.strip():
                    judul = a_tag.text.strip()
                    link = a_tag.get("href", "")
                    
                    time_tag = article.find("time") or article.find("span", class_=lambda x: x and ("date" in x or "time" in x))
                    waktu = time_tag.text.strip() if time_tag else "Terbaru"
                    
                    data_berita.append({
                        "Judul": judul,
                        "Waktu": waktu,
                        "Link": link
                    })

        # Cara cadangan jika selector di atas kosong
        if not data_berita:
            for h3 in soup.find_all("h3"):
                a_tag = h3.find("a")
                if a_tag and a_tag.text.strip():
                    data_berita.append({
                        "Judul": a_tag.text.strip(),
                        "Waktu": "Terbaru",
                        "Link": a_tag.get("href", "")
                    })

        if data_berita:
            # Ambil TEPAT 5 berita saja
            df = pd.DataFrame(data_berita).drop_duplicates(subset=["Judul"]).head(5)
            
            nama_file = "hasil_scraping_berita.csv"
            df.to_csv(nama_file, index=False, encoding="utf-8-sig")
            
            print(f"Scraping BERHASIL! 🎉 {len(df)} berita tersimpan di '{nama_file}'.\n")
            print("--- 5 JUDUL BERITA TERAMBIL ---")
            print(df[["Judul", "Waktu"]].to_string(index=False))
        else:
            print("Elemen berita masih tidak ditemukan pada halaman.")
    else:
        print(f"Gagal mengambil halaman. Status Code: {response.status_code}")

except Exception as err:
    print(f"Terjadi kesalahan: {err}")