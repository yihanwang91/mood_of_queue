import streamlit as st
import pandas as pd
import plotly.express as px
import gspread
import json
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

@st.cache_resource
def get_gspread_sheet():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds_dict = json.loads(st.secrets["GOOGLE_CREDENTIALS"])
    credentials = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
    client = gspread.authorize(credentials)
    sheet = client.open_by_key(st.secrets["GOOGLE_SHEET_ID"]).sheet1
    return sheet

sheet = get_gspread_sheet()

st.title("Mood of the Queue")

with st.form("mood_form"):
    mood = st.selectbox("Select your mood", ["Happy 😊", "Angry 😠", "Sad 😕", "Excited 🎉"])
    note = st.text_input("Add a note (optional)")
    submit = st.button("Enter your mood")

if submit:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sheet.append_row([timestamp, mood, note])
    st.success("Mood entered. Thank you!")
