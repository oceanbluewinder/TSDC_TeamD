from django.shortcuts import render
from django.http import HttpResponse

import pandas as pd
import json
import yfinance as yf
import datetime as dt
import plotly.graph_objs as go
from plotly.offline import plot
import mplfinance as mpf

def stock2330(request):
    # 下載台積電股票資料，以日期(Date欄位)為索引
    # 為了要顯示在網頁上，把資料轉換成JSON格式
    
    # 步驟1
    # 透過yfinance package 下載資料，日期 2022-03-01 ~ 2022-03-10
    # *注意 日期2022-03-01 不可以簡寫為 2022-3-1
    #df = pd.read_csv("staticfiles/csv/2330_TW.csv",encoding = 'utf-8')
    df = yf.download('2330.tw',start='2022-02-01', end='2022-03-18')

    # 步驟2
    # 以日期(Date欄位)為索引
    df.reset_index(inplace=True)

    # 步驟3
    # 將日期資料格式轉換成 YYYY-MM-DD，例如 2022-03-01
    # 原先下載的日期資料格式，例如 2022-03-01 00:00:00
    df['Date'] = df['Date'].dt.strftime('%Y-%m-%d')

    # 步驟4
    # 把資料轉換成JSON格式
    json_records = df.to_json(orient='records')
    data = json.loads(json_records)

    # 股票圖形
    result = go.Figure()
    result.add_trace(
        go.Bar(
            name = '成交量',
            x = df['Date'],
            y = df['Volume'],
            yaxis = 'y2',
            marker_color = '#99ccff'
        )
    )

    result.add_trace(
        go.Candlestick(
            name = '股價',
            x = df['Date'],
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


    return render(request, 'chJ/showstock2330.html', context)

def stock2881(request):
    return render(request, 'chJ/2881tw.html')

def index(request):
    return render(
        request,
        'chJ/index.html',
        {
            'title':'chJ Home Page',
        }
    )

##下面是業師的圖表code
