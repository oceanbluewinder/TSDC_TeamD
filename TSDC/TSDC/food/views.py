from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import json
import yfinance as yf
import datetime as dt
import plotly.graph_objs as go
from plotly.offline import plot

def index(request):
    df = pd.read_csv("food/static/csv/data.csv")
  
    # parsing the DataFrame in json format.
    json_records = df.reset_index().to_json(orient ='records')
    data = []
    data = json.loads(json_records)
    context = {'d': data}
  
    return render(request, 'food/csvshow.html', context)

def stock(request):
    # 股票資料
    start = dt.datetime(2022, 2, 1)
    end = dt.datetime(2022, 3, 31)
    df = yf.download('2330.tw',start, end)
    #df['Date'] = pd.to_datetime(df['Date'],unit='s')
    json_records = df.reset_index().to_json(orient='records', date_format='iso')
    data = []
    data = json.loads(json_records)


    # 股票圖形
    result = go.Figure()
    result.add_trace(
        go.Bar(
            name = '成交量',
            x = df['Volume'],
            y = df['Volume'],
            yaxis = 'y2',
            marker_color = '#99ccff'
        )
    )

    result.add_trace(
        go.Candlestick(
            name = '',
            x = df['Volume'],
            open = df['Open'],
            close = df['Close'],
            high = df['High'],
            low = df['Low'],
            increasing_line_color ='#fd5047',
            increasing_fillcolor ='#f29696',
            decreasing_line_color ='#3d9970',
            decreasing_fillcolor ='#91c2b3'
        )
    )

    result.update_layout(
        title = '2330 台積電',
        hovermode = 'x unified',
        yaxis = dict(
            title = '股價'
        ),
        yaxis2 = dict(
            overlaying = 'y',
            visible = False,
        ),
        font = dict(
            size = 20,
        )
    )

    plot_div = plot(result, output_type='div')

    context = {
                'd': data,
                'plot': plot_div
              }
    return render(request, 'food/stockshow.html', context)