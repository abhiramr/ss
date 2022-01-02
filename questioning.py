import streamlit as st
import pandas as pd
import numpy as np



st.markdown("# :santa: Broke Bibliophiles Bangalore Secret Santa 2021 - Homenum Revelio !")

df = pd.read_csv("./BBBSecretSanta 2021_W.csv")
st.table(df)