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
st.sidebar.subheader('Linear Regression')

# def load_csv(data):
#     df = pd.read_csv(os.path.join(data))
#     return df

# uploaded_file = st.file_uploader("Upload Files",type=['csv'])
# if uploaded_file is not None:
#     file_details = {"FileName":uploaded_file.name,"FileType":uploaded_file.type,"FileSize":uploaded_file.size}
#     files = load_csv(data)
#     st.write(files)
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
  st.write(df)

x = df.iloc[:, :-1].values
y = df.iloc[:, 1].values

params={
    'sigma x' : st.sidebar.text('Sigma X :'+str(sum(x))),
    'sigma y' : st.sidebar.text('Sigma Y :'+str(sum(y))),
    'sigma x^2' : st.sidebar.text('Sigma X^2 :'+str(sum(x)**2)),
    'sigma Y^2' : st.sidebar.text('Sigma Y^2 :'+str(sum(y)**2)),
}