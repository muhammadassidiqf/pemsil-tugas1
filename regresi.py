import csv
import streamlit as st
import pandas as pd
import os

st.title('Forecasting Sertifikat dan Poin')
st.subheader('Nama : Muhammad Assidiq Fattah')
st.subheader('NRP : 152017015')
st.sidebar.subheader('Hasil Linear Regression')

def find_mul_sum(d, e):
    res = 0

    for i in range(len(d)):
        res += (d[i]*e[i])
    
    return res

uploaded_file = st.file_uploader("Pilih file csv yang akan digunakan")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)

    x = df.iloc[:, :-1].values
    y = df.iloc[:, 1].values
    sigmax = int(sum(x))
    sigmay = int(sum(y))
    sigmax2 = int(sum(x**2))
    sigmay2 = int(sum(y**2))
    sigmax_2 = int((sum(x))**2)
    sigmay_2 = int((sum(y))**2)
    sigmaxy = int(find_mul_sum(x,y))
    n = len(df)
    a = round((sigmay*sigmax2 - sigmax * sigmaxy) /
                (n*sigmax2 - sigmax_2), 2)
    b = round(((n*sigmaxy) - (sigmax * sigmay)) /
                ((n*sigmax2) - sigmax_2), 2)
    r = round(((n*sigmaxy - sigmax*sigmay)) / ((n*sigmax2 - sigmax_2)*(n*sigmay2 - sigmay_2))**0.5, 2)
    kd = round((r**2)*100,2)
    kd_sisa = round(100-kd,2)

    params={
        'sigma x' : st.sidebar.text('Sigma X :'+str(sigmax)),
        'sigma y' : st.sidebar.text('Sigma Y :'+str(sigmay)),
        'sigma x^2' : st.sidebar.text('Sigma X^2 :'+str(sigmax2)),
        'sigma y^2' : st.sidebar.text('Sigma Y^2 :'+str(sigmay2)),
        '(sigma x)^2' : st.sidebar.text('(Sigma X)^2 :'+str(sigmax_2)),
        '(sigma y)^2' : st.sidebar.text('(Sigma Y)^2 :'+str(sigmay_2)),
        'sigma XY' : st.sidebar.text('Sigma XY:'+str(sigmaxy)),
        'a' : st.sidebar.text('a :'+str(a)),
        'b' : st.sidebar.text('b :'+str(b)),
    }

    st.sidebar.subheader('X')
    x_input = st.sidebar.number_input('Masukan jumlah sertifikat')

    Y_hasil = a + b*int(x_input)
    st.sidebar.subheader('Y')
    st.sidebar.text(str(Y_hasil))
    st.sidebar.subheader('r')
    st.sidebar.text(str(r))
    st.sidebar.subheader('KD')
    st.sidebar.text(str(kd))

    if((r >= 0) and (r < 0.2)):
        r2 = ("Kekuatan hubungan (r) : Sangat Lemah")
    elif((r >= 0.2) and (r < 0.4)):
        r2 = ("Kekuatan hubungan (r) : Lemah")
    elif((r >= 0.4) and (r < 0.6)):
        r2 = ("Kekuatan hubungan (r) : Sedang")
    elif((r >= 0.6) and (r < 0.8)):
        r2 = ("Kekuatan hubungan (r) : Kuat")
    elif((r >= 0.8) and (r <= 1)):
        r2 = ("Kekuatan hubungan (r) : Sangat Kuat")

    if(r < 0):
        skor = ("Nilai korelasi tersebut adalah negatif yang menyatakan bahwa perbandingannya adalah terbalik")
    else:
        skor = ("Nilai korelasi tersebut adalah positif yang menyatakan bahwa perbandingannya adalah searah")

    kd_text = ("Besar kontribusi variable sertifikat terhadap poin adalah "+str(kd)+"% dan sisanya yaitu sebesar "+str(kd_sisa)+"% dipengaruhi oleh variabel selain sertifikat")
    st.text(str(r2))
    st.text(str(skor))
    st.text(str(kd_text))
else:
    st.write("Silahkan Pilih file csv yang akan digunakan !")


