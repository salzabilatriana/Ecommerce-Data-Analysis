# ✨ E-Commerce Public Dataset — Data Analysis Project

Proyek analisis data menggunakan **E-Commerce Public Dataset (Olist Brazilian E-Commerce)**. Proyek ini mencakup proses analisis data lengkap (data wrangling, EDA, visualisasi, hingga kesimpulan & rekomendasi) serta dashboard interaktif berbasis **Streamlit**.

## Struktur Direktori

```
submission
├───dashboard
│   ├───main_data.csv       # data hasil cleaning & merging, dipakai dashboard
│   └───dashboard.py        # aplikasi Streamlit
├───data                    # dataset mentah (raw CSV)
│   ├───customers_dataset.csv
│   ├───order_items_dataset.csv
│   ├───order_payments_dataset.csv
│   ├───order_reviews_dataset.csv
│   ├───orders_dataset.csv
│   ├───product_category_name_translation.csv
│   ├───products_dataset.csv
│   └───sellers_dataset.csv
├───notebook.ipynb          # notebook analisis data lengkap (sudah dijalankan)
├───README.md
├───requirements.txt
└───url.txt
```

## Pertanyaan Bisnis

1. Bagaimana tren jumlah pesanan (order) secara bulanan sepanjang Januari 2017 - Agustus 2018, dan 5 kategori produk apa yang menyumbang revenue tertinggi selama periode tersebut?
2. Berapa perbedaan rata-rata skor ulasan (review score) antara pesanan yang terlambat dikirim dengan pesanan yang tepat waktu?

Jawaban lengkap beserta proses analisisnya ada di `notebook.ipynb`.

## Setup Environment

Disarankan menggunakan virtual environment terlebih dahulu.

**Menggunakan venv (pip):**
```
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

**Menggunakan Anaconda:**
```
conda create --name ecommerce-analysis python=3.11
conda activate ecommerce-analysis
pip install -r requirements.txt
```

## Menjalankan Notebook

```
jupyter notebook notebook.ipynb
```
Notebook membaca dataset mentah dari folder `data/` (path relatif `data/`), sehingga jalankan Jupyter dari dalam folder `submission/`.

## Menjalankan Dashboard (Streamlit)

Dashboard membaca `main_data.csv` yang sudah bersih (hasil dari proses di notebook), jadi jalankan dari dalam folder `dashboard/`:

```
cd dashboard
streamlit run dashboard.py
```

Setelah berjalan, buka browser ke alamat yang ditampilkan di terminal (default: `http://localhost:8501`).

### Fitur Dashboard
- Filter interaktif: rentang bulan, wilayah pelanggan (state), dan kategori produk.
- Ringkasan metrik utama: jumlah order, total revenue, persentase pesanan terlambat, rata-rata review score.
- Visualisasi tren order bulanan & top 5 kategori produk berdasarkan revenue.
- Visualisasi perbandingan review score untuk pesanan tepat waktu vs terlambat, serta 10 wilayah dengan pesanan terlambat terbanyak.

## Sumber Data

E-Commerce Public Dataset (Olist Brazilian E-Commerce), diunggah oleh pengguna sebagai bagian dari submission proyek analisis data.
