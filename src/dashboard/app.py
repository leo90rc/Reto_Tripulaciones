import re
import streamlit as st
import pandas as pd
import numpy as np


import requests
import sys,os

pato = os.path.dirname
direccion=pato(pato(pato(__file__)))
print(direccion)
sys.path.append(direccion)
from data import *


st.set_page_config(layout="wide") 
menu = st.sidebar.selectbox('Menu:',
            options=["Descripción aplicación","Información"])

st.title(' Easy Tour')


if menu == 'Descripción aplicación':
    st.write("Esta aplicación pretende revolucionar la forma de moverse de las personas con discapacidad. Los problemas y obstáculos que se tienen que enfrentar las personas con discapacidad provoca que muchas veces no puedan tener una experiencia plena cuando viajan a otra ciudad.") 
    st.write("Gracias a **Easy Tour** se pretende conseguir una mejora en la movililidad y accesibilidad tanto de los principales hitos turísticos y estaciones de metro como de las calles de la ciudad.")
    st.write(" Las personas podrán indicar la ruta con origen y destino a través de la aplicación y la aplicación les indicará cual es la ruta con mejor accesibilidad.")
    st.write("Actualmente está disponible para la zona centro de Barcelona. La aplicación incluye: 118 tramos de vías, todas las paradas de metro y 73 actividades culturales")
if menu == "Información":
    submenu=st.sidebar.selectbox(label="Tablas:",
            options=["Información","Accesibilidad calles","Accesibilidad metro","Accesibilidad actividades culturales"])
    if submenu=="Información":
        st.write("En este apartado se muestran las diferentes tablas generadas a través de la información recabada para las **tres áreas** que se tienen en cuenta en la aplicación: **calles, metro y monumentos.**")
    if submenu=="Accesibilidad calles":
        st.write("En este apartado se han tenido en consideración sólo aquellas vías cuya accesibilidad es **media o mala**. En total hay **118 tramos de vías**.")
        df = pd.read_csv(direccion + os.sep + 'data' + os.sep + "obstaculos.csv")
        st.write(df)
    if submenu=="Accesibilidad metro":
        st.write("En este apartado se han clasificado las **paradas de metro** en accesibles o no. El valor que se ha tenido en cuenta para esto ha sido las estaciones contaban o no con **ascensor**.")
        df = pd.read_csv(direccion + os.sep + 'data' + os.sep + "accessos.csv")
        st.write(df)
    if submenu=="Accesibilidad actividades culturales":
        st.write("En este apartado simplemente se pretende identificar las principales actividades turísticas de la ciudad para que los turistas puedan identificar aquellos lugares a los que quieren desplazarse para hacer turismo.")
        df = pd.read_csv(direccion + os.sep + 'data' + os.sep + "actividades_final.csv")
        st.write(df)

if menu == "Predicciones de los modelos":
    submenu=st.sidebar.selectbox(label="Predicciones de los modelos:",
            options=["Predicciones","Pruébame"])
    if submenu=="Predicciones":
        st.markdown('### Datos predecidos por los diferentes modelos')
        df = pd.read_csv(direccion + os.sep + 'data' + os.sep + "prediciones_vs_real.csv",nrows=50)
        st.write(df)
    if submenu=="Pruébame":
        st.title("Upload + Classification Example")
        uploaded_file = st.file_uploader("Choose a JPG image", type="jpg")
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            
            st.image(image, caption='Uploaded Image.', use_column_width=True)
            st.write("Classifying...")
            X = np.stack(np.array(image))
            model_path = direccion + os.sep + 'models' + os.sep + 'VGG16.h5'
            new_model = keras.models.load_model(model_path)
            
            smallimage = cv2.resize(X, (100, 300))
            pred = new_model.predict(preprocess_input(np.array(smallimage).reshape(1, 100, 100, 3)))
            if np.argmax(pred) == 0:
                st.write ("Lesión: Pólipo clase adenoma")
            if np.argmax(pred) == 1:
                st.write ("Lesión: Pólipo hiperplastico")    
            if np.argmax(pred) == 2:
                st.write ("Lesión: Úlcera") 
            if np.argmax(pred) == 3:
                st.write ("Lesión: Mucosa normal") 
            if np.argmax(pred) == 4:
                st.write ("Lesión: Lymfangiectasia") 
