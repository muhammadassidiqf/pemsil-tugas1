import csv
import streamlit as st
import pandas as pd
import os

# def file_selector(folder_path='.'):
    # filenames = os.listdir(folder_path)
    # selected_filename = st.selectbox('Select a file', filenames)
    # return os.path.join(folder_path, uploaded_file.name)

# filename = file_selector()
# st.write('You selected `%s`' % filename)

st.title('Forecasting Sertifikat')
st.subheader('Nama : Muhammad Assidiq Fattah')
st.subheader('NRP : 152017015')
st.sidebar.subheader('Linear Regression')

# def load_csv(data):
#     df = pd.read_csv(os.path.join(data))
#     return df

# uploaded_file = st.file_uploader("Upload Files",type=['csv'])
# if uploaded_file is not None:
#     file_details = {"FileName":uploaded_file.name,"FileType":uploaded_file.type,"FileSize":uploaded_file.size}
#     files = load_csv(data)
#     st.write(files)
def find_mul_sum(d, e):
    res = 0

    for i in range(len(d)):
        res += (d[i]*e[i])
    
    return res

uploaded_file = st.file_uploader("Choose a file")
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