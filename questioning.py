import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_csv("./BBBSecretSanta 2021_W.csv")
st.table(df)