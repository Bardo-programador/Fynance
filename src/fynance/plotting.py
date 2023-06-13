
import plotly.graph_objects as go
from datetime import date, timedelta

def candlePlot(df:dict, tempo:int) -> go.Figure:
    fig = go.Figure(data=[go.Candlestick(x=gerarDatas(date.today(), date.today()-timedelta(tempo)),
                                    open=df['Open'],
                                    low=df['Low'],
                                    high=df['High'],
                                    close=df['Close'],
                                    name="Candle")])
    
    fig.add_trace(go.Scatter(x=gerarDatas(date.today(), date.today()-timedelta(tempo)), y=df['MediaCurta'], mode='lines', name='MediaMovel'))
    fig.add_trace(go.Scatter(x=gerarDatas(date.today(), date.today()-timedelta(tempo)), y=df['MediaLonga'], mode='lines', name='MediaMovel'))
    return fig

def gerarDatas(inicio:str, fim:str):
    datas = []
    data = inicio
    while data >= fim:
        datas.append(data)
        data -= timedelta(days=1)
    return datas

def gerarMACD(df, tempo):
        # Criação do gráfico
    datas = gerarDatas(date.today(), date.today()-timedelta(tempo))
    df['MACD'] = df['MediaCurta'] - df['MediaLonga']
    df['Signal'] = df['MACD'].ewm(span=9, adjust=False).mean()
    fig = go.Figure()

    # Adição das barras positivas
    fig.add_trace(go.Bar(
        x=datas,
        y=df['MACD'],
        marker=dict(color='green'),
        opacity=0.7
    ))

    # Adição das barras negativas
    fig.add_trace(go.Bar(
        x=datas,
        y=df['MACD'].where(df['MACD'] < 0, 0),
        marker=dict(color='red'),
        opacity=0.7
    ))

    # Adição da linha de sinal
    fig.add_trace(go.Scatter(
        x=datas,
        y=df['Signal'],
        name='Signal',
        line=dict(color='blue')
    ))
    return fig