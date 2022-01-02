import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_csv("./BBBSecretSanta 2021.csv")
st.table(df)