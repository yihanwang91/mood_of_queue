import streamlit as st
import pandas as pd
import plotly.express as px
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
client = gspread.authorize(credentials)
sheet = client.open("Mood of the Queue").sheet1

st.title("Mood of the Queue")

mood = st.selectbox("Select your mood", ["Happy 😊", "Angry 😠", "Sad 😕", "Excited 🎉"])
note = st.text_input("Add a note (optional)")
submit = st.button("Enter your mood")

if submit:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sheet.append_row([timestamp, mood, note])
    st.success("Mood entered. Thank you!")
