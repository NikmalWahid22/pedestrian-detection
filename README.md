#  Pedestrian Detection menggunakan HOG + SVM

Proyek ini mengimplementasikan sistem deteksi pejalan kaki menggunakan metode **HOG (Histogram of Oriented Gradients)** yang dikombinasikan dengan **SVM (Support Vector Machine)** bawaan OpenCV. Tersedia dua mode: deteksi pada gambar statis dan deteksi pada video.

---

##  Deskripsi

Sistem deteksi pejalan kaki ini memanfaatkan descriptor HOG yang telah disediakan oleh OpenCV bersama dengan model SVM yang sudah dilatih sebelumnya (*pre-trained*). Program akan menandai area yang terdeteksi mengandung pejalan kaki dengan kotak merah pada gambar atau video.

---

##  Struktur File

```
project/
│
├── code1_image.py       # Deteksi pejalan kaki pada gambar
├── code2_video.py       # Deteksi pejalan kaki pada video
├── img.png              # File gambar input (untuk code1)
├── vid.mp4              # File video input (untuk code2)
└── README.md
```

---

##  Persyaratan

Pastikan Python dan library berikut sudah terinstal:

```bash
pip install opencv-python imutils
```

| Library       | Fungsi                                      |
|---------------|---------------------------------------------|
| `opencv-python` | Pemrosesan gambar, HOG descriptor, dan SVM |
| `imutils`       | Utilitas resize gambar yang mudah digunakan |

---

##  Code 1 — Deteksi pada Gambar Statis

**File:** `code1_image.py`

### Cara Kerja

1. Menginisialisasi HOG descriptor dan memuat model SVM default untuk deteksi orang.
2. Membaca file gambar `img.png`.
3. Meresize gambar agar lebarnya maksimal 400px.
4. Menjalankan `detectMultiScale` untuk mendeteksi pejalan kaki.
5. Menggambar kotak merah di sekitar setiap pejalan kaki yang terdeteksi.
6. Menampilkan hasil gambar di layar.

### Parameter Deteksi

| Parameter    | Nilai  | Keterangan                                      |
|--------------|--------|-------------------------------------------------|
| `winStride`  | (4, 4) | Langkah sliding window (lebih kecil = lebih akurat, lebih lambat) |
| `padding`    | (4, 4) | Padding di sekitar window deteksi               |
| `scale`      | 1.05   | Faktor skala pyramid (lebih kecil = lebih detail) |

### Cara Menjalankan

```bash
python code1_image.py
```

> Tekan sembarang tombol untuk menutup jendela gambar.

---

##  Code 2 — Deteksi pada Video

**File:** `code2_video.py`

### Cara Kerja

1. Menginisialisasi HOG descriptor dan memuat model SVM default.
2. Membuka file video `vid.mp4` menggunakan `VideoCapture`.
3. Membaca setiap frame secara berurutan.
4. Meresize setiap frame agar lebarnya maksimal 400px.
5. Menjalankan deteksi HOG pada setiap frame.
6. Menggambar kotak merah pada pejalan kaki yang terdeteksi.
7. Menampilkan video secara real-time.

### Parameter Deteksi

| Parameter    | Nilai  | Keterangan                                      |
|--------------|--------|-------------------------------------------------|
| `winStride`  | (4, 4) | Langkah sliding window                          |
| `padding`    | (4, 4) | Padding di sekitar window deteksi               |
| `scale`      | 1.05   | Faktor skala pyramid                            |

### Cara Menjalankan

```bash
python code2_video.py
```

> Tekan tombol **`q`** untuk menghentikan pemutaran video.

---

##  Penjelasan Metode HOG + SVM

**HOG (Histogram of Oriented Gradients)** adalah metode ekstraksi fitur yang mendeskripsikan struktur lokal suatu objek berdasarkan distribusi arah gradien intensitas piksel.

**Alur deteksi:**

```
Input Gambar/Frame
       ↓
  Resize Gambar
       ↓
  HOG Descriptor  →  Ekstraksi fitur dari sliding window
       ↓
  SVM Classifier  →  Klasifikasi: pejalan kaki / bukan
       ↓
  Non-Maximum Suppression (internal)
       ↓
  Bounding Box ditampilkan
```

---

## Catatan

- Pastikan file `img.jpg` dan `vid.mp4` berada di direktori yang sama dengan script.
- Performa deteksi bergantung pada kualitas gambar dan pencahayaan.
- Untuk akurasi lebih tinggi, nilai `scale` dapat dikecilkan (misal `1.02`), namun akan memperlambat proses.
- Untuk deteksi real-time yang lebih cepat, pertimbangkan menggunakan model deep learning seperti YOLO.

---
