from fynance import tickers
import plotting
import pandas as pd
import streamlit as st
from datetime import time

selectbox = st.sidebar.selectbox("Escolha um ticker",
                                 (tickers))  

mediaCurta = st.sidebar.number_input("Digite o valor da média curta", value=9)
mediaLonga = st.sidebar.number_input("Digite o valor de média longa", value=72)

df = pd.read_csv(f"dados/{selectbox}.csv")
df['MediaLonga'] = df['Close'].rolling(window=mediaLonga, min_periods=1).mean()
df['MediaCurta'] = df['Close'].rolling(window=mediaCurta, min_periods=1).mean()

candle = plotting.candlePlot(df, 120)
macd = plotting.gerarMACD(df, 120)

st.plotly_chart(candle)
st.plotly_chart(macd)

