import streamlit as st
import pandas as pd

st.write('Time required to make tea')

st.write(pd.DataFrame({
    'Levi': ["2 min"],
    'Phill': ["30 secs"],
    'Oli': ["14 hours"]
}))

