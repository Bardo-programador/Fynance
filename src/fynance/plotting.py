
import plotly.graph_objects as go
from datetime import date, timedelta

def candlePlot(df:dict, tempo:int) -> go.Figure:
    fig = go.Figure(data=[go.Candlestick(x=gerarDatas(date.today(), date.today()-timedelta(tempo)),
                                    open=df['Open'],
                                    low=df['Low'],
                                    high=df['High'],
                                    close=df['Close'],
                                    name="Candle")])
    return fig

def gerarDatas(inicio:str, fim:str):
    datas = []
    data = inicio
    while data >= fim:
        datas.append(data)
        data -= timedelta(days=1)
    return datas