# Sistem Pakar Diagnosis Penyakit

Sistem ini merupakan **sistem pakar berbasis Python** yang dirancang untuk membantu mendiagnosis jenis penyakit berdasarkan gejala-gejala yang dimasukkan oleh pengguna. Proyek ini mengimplementasikan teknik **AI Reasoning** menggunakan **algoritma Backward Chaining**.

## 🧠 Apa itu Backward Chaining?
Backward chaining adalah metode penalaran dari *goal* (tujuan) ke *fact* (fakta). Sistem akan mulai dari dugaan penyakit, lalu menelusuri apakah gejala-gejala yang ada dapat mendukung dugaan tersebut.

## 📌 Fitur
- Antarmuka interaktif berbasis terminal (CLI)
- Input gejala dari pengguna
- Penalaran menggunakan backward chaining
- Hasil diagnosis jenis penyakit
- Basis pengetahuan yang dapat diperluas

## 🛠️ Teknologi yang Digunakan
- Python 3
- Rule-based reasoning
- File teks atau dictionary sebagai basis pengetahuan

## 📂 Struktur Folder
├── knowledge_base.py # Basis pengetahuan (aturan dan fakta)
├── inference_engine.py # Mesin inferensi dengan backward chaining
├── main.py # Program utama
├── README.md # Dokumentasi proyek
