import pickle
import pandas as pd
import streamlit as st
from sklearn.model_selection import train_test_split

st.markdown(
    "<h1 style='text-align: center;'>Klasifikasi Diabetes Menggunakan Model Random Forest</h1>", unsafe_allow_html=True
)
st.markdown(
    "<h4 style='text-align: center;'>Indah Pratiwi | 210411100050 | Metpen - B</h4>", unsafe_allow_html=True
)

with open('model_rf.pkl', 'rb') as file_model:
    model_rf = pickle.load(file_model)

Glucose = st.number_input("Input kadar glukosa dalam darah")
BloodPressure = st.number_input("Input tekanan darah")
Insulin = st.number_input ('Input kadar insulin dalam serum seteleh 2 jam tes')
BMI = st.number_input ('Input Body Mass Index anda. Anda bisa menghitung BMI melalui url berikut : https://www.halodoc.com/bmi-calculator/')
Age = st.number_input ('Input umur anda')


if st.button('Cek Status'):
    if Glucose is not None and BMI is not None and BloodPressure is not None and Age is not None and Insulin is not None:
        
        # # Konversi input yang diterima menjadi tipe data numerik
        # Glucose = int(Glucose)
        # BloodPressure = int(BloodPressure)

        data = {
            'Glucose': [Glucose],
            'BloodPressure': [BloodPressure],
            'Insulin' : [Insulin],
            'BMI': [BMI],
            'Age': [Age]
        }

        df = pd.DataFrame(data)
        
        # Prediksi berdasarkan input yang telah diubah menjadi numerik
        prediksi = model_rf.predict(df)
        if prediksi[0] == 0.0:
            st.success("Anda diprediksi tidak diabetese !")
        else:
            st.error("Anda diprediksi diabetese !")
    else:
        st.text('Data tidak boleh kosong. Harap isi semua kolom.')
