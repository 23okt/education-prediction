# 🎓 Proyek Akhir: Menyelesaikan Permasalahan Institusi Pendidikan Perguruan Jaya Jaya Institut

## Business Understanding

Jaya Jaya Institut merupakan institusi pendidikan tinggi yang telah berdiri sejak tahun 2000 dan memiliki reputasi baik dalam mencetak lulusan berkualitas. Namun, institusi ini menghadapi masalah serius: angka dropout mahasiswa yang tinggi. Dropout tidak hanya merugikan secara finansial dan reputasi, tetapi juga menghambat misi lembaga dalam mendidik generasi penerus.

Untuk itu, proyek ini bertujuan untuk membangun sistem yang dapat memprediksi potensi dropout mahasiswa sejak dini dengan menggunakan pendekatan machine learning. Dengan begitu, pihak kampus dapat segera memberikan intervensi dan bimbingan yang tepat kepada mahasiswa yang berisiko.

### Permasalahan Bisnis

Permasalahan utama yang ingin diselesaikan:

    - Tingginya angka mahasiswa dropout dari program studi di Jaya Jaya Institut.

    - Tidak adanya sistem prediksi untuk mengidentifikasi mahasiswa yang berpotensi dropout.

    - Kurangnya insight visual dan analitik yang dapat digunakan manajemen dalam mengambil keputusan terkait retention mahasiswa.

### Cakupan Proyek

Berikut adalah ruang lingkup dari proyek ini:

    -Melakukan analisis eksplorasi terhadap data akademik mahasiswa.

    -Membangun dashboard interaktif berbasis Streamlit untuk visualisasi data dan status mahasiswa.

    -Mengembangkan dan melatih model machine learning untuk memprediksi risiko dropout mahasiswa.

    -Membuat prototype aplikasi prediksi dropout berbasis Streamlit.

    -Memberikan rekomendasi tindakan berdasarkan hasil analisis dan prediksi.

### Persiapan

Sumber data: https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv

Setup environment:

```
💻 Platform & Tools
Google Colab
Digunakan sebagai platform utama untuk eksplorasi data, analisis statistik, dan pelatihan model machine learning.

Metabase v0.54.3
Digunakan sebagai platform BI (Business Intelligence) untuk membuat visualisasi dan dashboard interaktif.

Supabase
Digunakan untuk menampung data analisis yang akan dipergunakan pada visualisasi di platform Metabase.

StreamLit
Digunakan untuk menampilkan hasil seperti website prediksi.

📦 Library
pandas	2.2.2	Manipulasi dan analisis data tabular
numpy	1.26.4	Operasi numerik dan array
matplotlib	3.7.1	Visualisasi data dasar
seaborn	0.12.2	Visualisasi statistik dan heatmap
scikit-learn	1.4.2	Pembuatan dan evaluasi model machine learning
joblib	1.4.2	Menyimpan dan memuat model
sqlalchemy	2.0.29	Koneksi ke database SQL untuk integrasi data
```

## Business Dashboard

Link Dashboard: https://drive.google.com/file/d/1iq_E8RB0h9EomLww8bC1Zv6DSBsXNPDw/view?usp=sharing

📊 1. Distribusi Status Mahasiswa (Donut Chart)
Menampilkan persentase status mahasiswa: Lulus (49.9%), Dropout (32.1%), dan Masih Aktif (17.9%).

Insight: Tingginya angka dropout (32.1%) perlu mendapat perhatian serius. Bisa jadi terkait faktor internal kampus atau kondisi mahasiswa.

💸 2. Distribusi Permasalahan Keuangan Mahasiswa
67.8% mahasiswa tidak memiliki masalah keuangan, sementara 32.2% mengalami kendala finansial.

Insight: Sepertiga dari total mahasiswa mengalami kendala keuangan, yang mungkin menjadi salah satu penyebab dropout tinggi.

🏠 3. Distribusi Mahasiswa Terlantar
54.8% Mahasiswa terlantar (displaced), sedangkan 45.2% tidak.

Insight: Mayoritas mahasiswa mengalami kondisi sosial yang tidak stabil. Hal ini bisa berdampak negatif pada capaian akademik dan retensi.

🧠 4. Kebutuhan Perawatan Khusus
Dari total 4,424 mahasiswa, hanya 1.15% yang membutuhkan perlakuan khusus, dan 98.85% tidak.

Insight: Meski minoritas, mahasiswa dengan kebutuhan khusus tetap memerlukan perhatian dan dukungan institusi.

📈 5. Rata-rata Jumlah Mahasiswa per Program Studi (Bar Chart Horizontal)
Program studi seperti Biofuel Production Technologies memiliki rata-rata sangat rendah (4 mahasiswa).

Sedangkan rata-rata tertinggi berasal dari kelompok “Other (7)” dengan 901.67 mahasiswa.

Insight: Ada ketimpangan besar dalam distribusi mahasiswa antar program studi. Ini bisa menunjukkan ketidakseimbangan popularitas, kapasitas, atau daya saing antar prodi.

👨‍🎓 6. Distribusi Mahasiswa Berdasarkan Program Studi
Menampilkan jumlah lulusan, mahasiswa aktif, dan dropout pada masing-masing prodi.

Contoh:

Nursing: Tertinggi dalam jumlah lulusan (548) tapi juga tinggi dalam dropout (100).

Social Service (Evening) dan Communication Design menunjukkan angka dropout yang relatif tinggi dibanding jumlah total.

Insight: Beberapa program studi memiliki ketidakseimbangan dalam output pendidikan (lulus vs dropout), yang perlu dievaluasi dari segi kurikulum, beban studi, atau dukungan akademik.

📌 Kesimpulan Umum (Business Insight)
Dropout rate tinggi (32.1%) menjadi masalah utama, dan tampaknya terkait dengan faktor keuangan (32.2%) dan kondisi sosial (54.8% displaced).

Distribusi mahasiswa tidak merata di antara prodi, mengindikasikan perlunya peninjauan strategi promosi dan kapasitas masing-masing program.

Mayoritas mahasiswa tidak membutuhkan perlakuan khusus, namun segmen kecil tetap harus diperhatikan dengan pendekatan inklusif.

## 🤖 Menjalankan Sistem Machine Learning

Model machine learning yang digunakan adalah Random Forest Classifier, dengan akurasi memuaskan pada data testing.

```
Langkah menjalankan sistem prediksi di prediction.py:
1. Buka terminal di IDE lalu lakukan pip install joblib serta pip install scikit-learn
2. Buka file prediction.py di IDE yang anda gunakan
3. Masukkan beberapa input secara manual
4. Jalankan Kodenya
5. Hasil prediksi akan tampil pada terminal IDE yang anda gunakan

Langkah menjalankan sistem prediksi di streamlit website:
1. Klik link berikut: https://education-prediction-website.streamlit.app/
2. Lalu Masukkan beberapa input
3. Hasil prediksi akan keluar sesuai dengan inputan
```

## Conclusion

Berdasarkan analisis dan pengujian model, kami berhasil:

    -Mengidentifikasi fitur-fitur yang paling berpengaruh terhadap potensi dropout mahasiswa.

    -Membangun sistem prediksi yang dapat dioperasikan langsung oleh pihak institusi.

    -Membantu pihak manajemen memahami dan menangani risiko dropout lebih awal.

### Rekomendasi Action Items

Berikut beberapa langkah yang dapat dilakukan oleh Jaya Jaya Institut:

    - 🎯 Implementasi sistem prediksi secara menyeluruh untuk memantau mahasiswa setiap semester.

    - 👥 Membuat program bimbingan akademik yang ditujukan untuk mahasiswa dengan risiko dropout tinggi.

    - 📈 Memantau tren dropout secara periodik dengan dashboard yang mudah diakses.

    - 🧠 Meningkatkan kualitas data input, seperti validasi nilai dan pengisian profil mahasiswa secara lengkap.
