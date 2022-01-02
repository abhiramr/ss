import streamlit as st
import pandas as pd
import numpy as np

st.markdown(":santa:")
st.title("Broke Bibliophiles Bangalore Secret Santa 2021 - Homenum Revelio !", anchor=None)


df = pd.read_csv("./BBBSecretSanta 2021.csv")
st.table(df)