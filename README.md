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
streamlit 1.45.0 Untuk membuat website prediksi
```

## Business Dashboard

Link Dashboard: https://drive.google.com/file/d/1AZpy3li5vMpuIEBPbgw7g57JGXjpdeke/view?usp=sharing

📊 1. Total Students (Number Card)
Menampilkan total mahasiswa: 4.424.
Insight: Ini adalah basis populasi yang menjadi acuan seluruh analisis.

📊 2. Total Dropout (Number Card)
Menampilkan jumlah mahasiswa yang dropout: 1.421.
Insight: Lebih dari seribu mahasiswa berhenti sebelum menyelesaikan studi—skala masalahnya cukup besar.

📊 3. Percentage Dropout (Number Card)
Menampilkan persentase mahasiswa yang dropout: 32,12 %.
Insight: Sekitar sepertiga populasi mahasiswa berhenti kuliah, menandakan perlu upaya intervensi yang lebih intensif.

📊 4. Distribution Student Status (Donut Chart)
Menampilkan proporsi status mahasiswa:

Graduate 49,9 %

Dropout  32,1 %

Enrolled  17,9 %

Insight: Meskipun hampir setengah mahasiswa berhasil lulus, tingginya porsi dropout (32,1 %) dan rendahnya porsi masih aktif (17,9 %) mengindikasikan ada tantangan baik di sisi dukungan akademik maupun non‑akademik.

📊 5. Dropout Student by Displaced (Bar Chart)
Menampilkan jumlah siswa dropout berdasarkan apakah mereka tergolong displaced student:

No: 752

Yes: 669

Insight: Tingkat dropout sedikit lebih tinggi pada yang tidak displaced, menandakan faktor non‑displacement (misalnya dukungan sosial atau akademik) mungkin lebih dominan.

📊 6. Dropout Rate by Tuition Fee (Donut Chart)
Menampilkan persentase dropout berdasarkan status pembayaran biaya kuliah:

Belum Membayar: 78 %

Sudah Membayar: 22 %
(Total “111.3” menunjukkan rata‑rata persentase atau indeks yang diukur.)

Insight: Sebagian besar dropout berasal dari mereka belum membayar—menguatkan hipotesis bahwa kendala finansial adalah pemicu utama.

📊 7. Distribution Student Dropout by Debtor Status (Bar Chart)
Menampilkan jumlah siswa dropout berdasarkan apakah mereka tercatat sebagai debtor:

No: 1.109

Yes: 312

Insight: Mahasiswa tanpa catatan debtor justru lebih banyak yang dropout, bisa jadi karena sistem tagihan yang terlalu kaku bagi yang berutang ringan, atau karena debtor mendapat perhatian khusus sehingga tingkat dropout lebih rendah.

📊 8. Dropout Rate by Special Needs (Donut Chart)
Menampilkan persentase dropout berdasarkan kebutuhan perlakuan khusus:

Special Needs: 51 %

No Special Needs: 49 %

Insight: Angka hampir seimbang, tetapi sedikit lebih tinggi di kelompok special needs, menunjukkan diperlukan dukungan tambahan untuk mahasiswa berkebutuhan khusus.

📊 9. Age At Enrollment by Student Status (Stacked Bar Chart)
Menampilkan jumlah mahasiswa per rentang usia dan status (Dropout, Enrolled, Graduate):

17–27: Dropout 944, Enrolled 684, Graduate 1.936

28–38: Dropout 332, Enrolled 75, Graduate 167

39–49: Dropout 114, Enrolled 31, Graduate 82

50–60: Dropout 29, Enrolled 4, Graduate 23

61–70: Dropout 2, Enrolled 1, Graduate 0

Insight: Kelompok usia 17–27 mendominasi semua status—intervensi harus difokuskan.

📊 11. Distribution of Students by Course (Clustered Bar Chart)
Menampilkan jumlah Graduate (kuning), Enrolled (merah), dan Dropout (hijau) untuk setiap program studi.

Top 3 program dengan angka dropout tertinggi:

Veterinary Nursing: 75 mahasiswa

Nursing: 100 mahasiswa

Manajemen: 108 mahasiswa

Insight: Program‑program besar seperti Veterinary Nursing dan Management mengalami beban dropout yang signifikan—mungkin karena kurikulum yang berat, beban praktikum/klinis, atau kurangnya dukungan akademik di bidang tersebut.

🔑 Kesimpulan Keseluruhan & Rekomendasi Fokus ke Depan
Faktor Utama Penyebab Dropout

Kendala Finansial: 78 % dropout terjadi pada mahasiswa yang belum membayar biaya kuliah.

Konsentrasi Usia Awal: Kelompok 17–27 tahun mendominasi angka dropout, menandakan fase adaptasi awal yang kritis.

Program Studi Spesifik: Beberapa jurusan (Veterinary Nursing, Management) menunjukkan angka dropout jauh lebih tinggi dibanding rata‑rata.

Apa yang Perlu Difokuskan

Beasiswa & Skema Cicilan: Perkuat dukungan keuangan untuk mahasiswa berisiko gagal bayar.

Program Onboarding & Mentoring: Buat program pendampingan khusus di 2 tahun pertama—khususnya untuk kelompok usia 17–27.

Intervensi Berdasarkan Jurusan: Lakukan survei mendalam di Veterinary Nursing dan Management untuk identifikasi hambatan kurikulum atau fasilitas praktikum, lalu rancang solusi (misalnya tutor khusus, workshop keterampilan klinis).

## 🤖 Menjalankan Sistem Machine Learning

Model machine learning yang digunakan adalah Random Forest Classifier, dengan akurasi memuaskan pada data testing.

```
Langkah menjalankan sistem prediksi di prediction.py:
1. Buka terminal di IDE lalu lakukan pip install joblib serta pip install scikit-learn
2. Buka file prediction.py di IDE yang anda gunakan
3. Masukkan beberapa input secara manual
4. Jalankan Kodenya di terminal dengan python prediction.py
5. Hasil prediksi akan tampil pada terminal IDE yang anda gunakan

Langkah menjalankan sistem prediksi streamlit lokal dengan file index.py:
1. Lakukan pip install pipenv di command prompt
2. Inisialisasi pipenv install
3. Masuk ke environment Pipenv dengan pipenv shell
4. Install Dependensi dengan pip install -r requirements.txt
5. Jalankan Streamlit App (Local) dengan streamlit run index.py di terminal
6. Masukkan beberapa input
7. Hasil prediksi akan tampil

Langkah menjalankan sistem prediksi di streamlit website (Deploy):
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
