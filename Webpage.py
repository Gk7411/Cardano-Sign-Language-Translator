import streamlit as st
from streamlit_webrtc import webrtc_streamer
from google_trans_new import google_translator
import pandas as pd
import os
import cv2
#df = pd.read_excel(os.path.join('data', 'language.xlsx'), sheet_name='wiki')
#df.dropna(inplace=True)
#lang = df['name'].to_list()
#langlist=tuple(lang)
#langcode = df['iso'].to+list()

st.set_page_config(page_title="Webpage", layout="wide")
# --- Header section -- #
st.subheader("Hi, Welcome to Cardano!")
# setup camera on streamlit
webrtc_streamer(key="sample")
# convert sign language to english
translator = google_translator()
title = st.text_input('Sign Language Translator')
#convert the translation to any other languages
#Ill be adding a slider in a second i just didn't finish it yet 

