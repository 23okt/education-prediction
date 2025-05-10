import joblib
import pandas as pd

# Memuat model Random Forest yang telah disimpan
model = joblib.load('model/random_forest_model.pkl')

# Menyiapkan data baru untuk prediksi
data_baru = pd.DataFrame({
    'Application_mode': [1],
    'Debtor': [0],
    'Tuition_fees_up_to_date': [0],
    'Educational_special_needs': [0],
    'Displaced': [0],
    'Age_at_enrollment': [19],
    'Curricular_units_1st_sem_grade': [20.0],
    'Curricular_units_2nd_sem_grade': [20.0],
    'Previous_qualification_grade': [160.0],
    'Admission_grade': [200.0]
})

# Melakukan prediksi
prediksi = model.predict(data_baru)

# Mengonversi hasil prediksi menjadi label yang lebih mudah dipahami
label_prediksi = ['Tidak dropout' if hasil == 1 else 'Berpotensi dropout' for hasil in prediksi]

# Menampilkan hasil prediksi
print("Hasil Prediksi:", label_prediksi)