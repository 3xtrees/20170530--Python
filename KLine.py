'''
Created on 2017-5-9
@author: 3xtrees
'''
# coding=utf-8
import tushare as ts
import matplotlib.finance as mpf
import matplotlib.pyplot as plt
import datetime
from matplotlib.pylab import date2num

'''
绘制单只股票的K线
input:股票代码，起始日期，结束日期
output:K线图
'''

def drawKFig(quote_code, start_date, end_date):
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    
    # 对tushare获取到的数据转换成candlestick_ohlc()方法可读取的格式
    data_list = []
    
    hist_data = ts.get_hist_data(quote_code, start=start_date, end=end_date)  # 一次性获取全部日k线数据
    for date, row in hist_data.iterrows():
        # 将时间转换为数字
        date_time = datetime.datetime.strptime(date, '%Y-%m-%d')
        t = date2num(date_time)
        open, high, close, low = row[:4]
        datas = (t, open, high, low, close)
        print(datas)
        data_list.append(datas)
     
    # 创建子图
    fig, ax = plt.subplots()
    fig.subplots_adjust(bottom=0.2)
    
    # 设置X轴刻度为日期时间
    ax.xaxis_date()
    plt.xticks(rotation=45)
    plt.yticks()
    plt.title(u"股票代码：" + quote_code)
    plt.xlabel(u"时间")
    plt.ylabel(u"股价（元）")
    mpf.candlestick_ohlc(ax, data_list, width=0.9, colorup='red', colordown='green')
    ax.autoscale_view()
    plt.grid()
    plt.show()
    pass

if __name__ == "__main__":
    drawKFig(quote_code='601668', start_date='2016-05-29', end_date='2017-06-12')
    