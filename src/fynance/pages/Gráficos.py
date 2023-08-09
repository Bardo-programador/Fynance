import yfinance as yf
import plotting
import pandas as pd
import streamlit as st
from datetime import time
tickers =['FNF', 'ASML', 'GOOGL', 'AAPL'] ##Lista de tickersit

selectbox = st.sidebar.selectbox("Escolha um ticker",
                                 (tickers))  
with st.sidebar:
    mediaCurta = st.number_input("Digite o valor da média curta", value=9)
    mediaLonga = st.number_input("Digite o valor de média longa", value=72)

df = yf.download(selectbox, group_by="ticker", period='20y') ##Baixa os dados do yahoo finance
df['MediaLonga'] = df['Close'].rolling(window=mediaLonga, min_periods=1).mean() ##Faz o calculo da media longa
df['MediaCurta'] = df['Close'].rolling(window=mediaCurta, min_periods=1).mean() ##Faz o calculo da media curta

candle = plotting.candlePlot(df, 120) ##Cria o gŕafico de candlestick
macd = plotting.gerarMACD(df, 120) ##Cria o gráfico de MACD

#Plota os gráficos
st.plotly_chart(candle)
st.plotly_chart(macd)

