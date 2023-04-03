# streamlit run pingulit.py

import streamlit as st
import seaborn as sns
import pandas as pd

from matplotlib import pyplot as plt


st.write("""
# The Flip Side

*a report on penguin flippers*
""")

df = sns.load_dataset('penguins')
#st.write(df)

number = st.slider("pick a number", 0, 1000)

df = df[df["flipper_length_mm"] < number]
st.write(df)


st.bar_chart(df["species"].value_counts())

fig = plt.figure()
sns.histplot(df["flipper_length_mm"], kde=True)
st.pyplot(fig)
