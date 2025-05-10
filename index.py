import joblib
import pandas as pd
import streamlit as st

# Judul aplikasi
st.title("🎓 Prediksi Dropout Mahasiswa")

# Deskripsi
st.write("""
Aplikasi ini memprediksi apakah seorang mahasiswa **berpotensi dropout** atau **tidak dropout** berdasarkan informasi akademik dan latar belakangnya.
""")

# Memuat model
model = joblib.load('model/random_forest_model.pkl')

# Input data pengguna
st.header("📥 Masukkan Data Mahasiswa")
application_mode = st.selectbox("Application Mode", [1, 5, 15, 16, 17])
debtor = st.radio("Apakah Mahasiswa Memiliki Hutang?", [0, 1], format_func=lambda x: 'Tidak' if x == 0 else 'Ya')
tuition_fees = st.radio("Apakah Biaya Kuliah Sudah Dibayar?", [1, 0], format_func=lambda x: 'Ya' if x == 1 else 'Tidak')
special_needs = st.radio("Apakah Mahasiswa Memiliki Kebutuhan Khusus?", [0, 1], format_func=lambda x: 'Tidak' if x == 0 else 'Ya')
displaced = st.radio("Apakah Mahasiswa Terdampak Sosial (Displaced)?", [0, 1], format_func=lambda x: 'Tidak' if x == 0 else 'Ya')
age = st.slider("Umur Saat Mendaftar", 16, 40, 19)
grade_1st = st.slider("Nilai Semester 1", 0.0, 20.0, 15.0)
grade_2nd = st.slider("Nilai Semester 2", 0.0, 20.0, 15.0)
prev_grade = st.number_input("Nilai Kualifikasi Sebelumnya", min_value=0.0, max_value=200.0, value=160.0)
admission_grade = st.number_input("Nilai Saat Masuk", min_value=0.0, max_value=200.0, value=180.0)

# Menyusun data
data_baru = pd.DataFrame({
    'Application_mode': [application_mode],
    'Debtor': [debtor],
    'Tuition_fees_up_to_date': [tuition_fees],
    'Educational_special_needs': [special_needs],
    'Displaced': [displaced],
    'Age_at_enrollment': [age],
    'Curricular_units_1st_sem_grade': [grade_1st],
    'Curricular_units_2nd_sem_grade': [grade_2nd],
    'Previous_qualification_grade': [prev_grade],
    'Admission_grade': [admission_grade]
})

# Tombol prediksi
if st.button("🔍 Prediksi"):
    hasil = model.predict(data_baru)
    label_prediksi = '✅ Tidak Dropout' if hasil[0] == 1 else '⚠️ Berpotensi Dropout'

    # Menampilkan hasil
    st.subheader("📊 Hasil Prediksi:")
    st.success(label_prediksi if hasil[0] == 1 else label_prediksi)
