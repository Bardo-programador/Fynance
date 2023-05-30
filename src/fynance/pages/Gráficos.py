from fynance import tickers
import plotting
import pandas as pd
import streamlit as st

df = pd.read_csv("dados/AAPL.csv")

candle = plotting.candlePlot(df, 120)
st.plotly_chart(candle)



