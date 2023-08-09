
import plotly.graph_objects as go
from datetime import date, timedelta

def candlePlot(df:dict, tempo:int) -> go.Figure: ## Recebe um dataframe e retorna um gráfico de candlestick
    ##Criacao de colunas
    fig = go.Figure(data=[go.Candlestick(x=gerarDatas(date.today(), date.today()-timedelta(tempo)), #Coluna de datas
                                    open=df['Open'], ##Coluna de Abertura
                                    low=df['Low'], ##Coluna de Minimo
                                    high=df['High'], ##Coluna de Maximo
                                    close=df['Close'], ##Coluna de Fechamento
                                    name="Candle")]) ##Nome do gráfico
    
    fig.add_trace(go.Scatter(x=gerarDatas(date.today(), date.today()-timedelta(tempo)), y=df['MediaCurta'], mode='lines', name='MediaMovel')) ##Adicona a linha de media curta
    fig.add_trace(go.Scatter(x=gerarDatas(date.today(), date.today()-timedelta(tempo)), y=df['MediaLonga'], mode='lines', name='MediaMovel')) ##Adiciona a linha de media longa
    return fig

def gerarDatas(inicio:str, fim:str): # Recebe duas datas no formato YYYY-MM-DD e retorna uma lista de datas entre elas
    datas = []
    data = inicio
    while data >= fim:
        datas.append(data)
        data -= timedelta(days=1)
    return datas

def gerarMACD(df, tempo:int):
        # Criação do gráfico MACD
    datas = gerarDatas(date.today(), date.today()-timedelta(tempo))
    df['MACD'] = df['MediaCurta'] - df['MediaLonga']
    df['Signal'] = df['MACD'].ewm(span=9, adjust=False).mean()
    fig = go.Figure()

    # Adição das barras positivas
    fig.add_trace(go.Bar(
        x=datas,
        y=df['MACD'].where(df['MACD'] > 0, 0),
        name= None,
        marker=dict(color='green'),
        opacity=0.7,
        showlegend=False
    ))

    # Adição das barras negativas
    fig.add_trace(go.Bar(
        x=datas,
        y=df['MACD'].where(df['MACD'] < 0, 0),
        name= None,
        marker=dict(color='red'),
        opacity=0.7,
        showlegend=False
    ))

    # Adição da linha de sinal
    fig.add_trace(go.Scatter(
        x=datas,
        y=df['Signal'],
        name='Signal',
        line=dict(color='blue')
    ))
    return fig