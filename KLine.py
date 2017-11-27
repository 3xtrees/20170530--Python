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
缁樺埗鍗曞彧鑲＄エ鐨凨绾�
input:鑲＄エ浠ｇ爜锛岃捣濮嬫棩鏈燂紝缁撴潫鏃ユ湡
output:K绾垮浘
'''

def drawKFig(quote_code, start_date, end_date):
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    
    # 瀵箃ushare鑾峰彇鍒扮殑鏁版嵁杞崲鎴恈andlestick_ohlc()鏂规硶鍙鍙栫殑鏍煎紡
    data_list = []
    
    hist_data = ts.get_hist_data(quote_code, start=start_date, end=end_date)  # 涓�娆℃�ц幏鍙栧叏閮ㄦ棩k绾挎暟鎹�
    for date, row in hist_data.iterrows():
        # 灏嗘椂闂磋浆鎹负鏁板瓧
        date_time = datetime.datetime.strptime(date, '%Y-%m-%d')
        t = date2num(date_time)
        open, high, close, low = row[:4]
        datas = (t, open, high, low, close)
        print(datas)
        data_list.append(datas)
     
    # 鍒涘缓瀛愬浘
    fig, ax = plt.subplots()
    fig.subplots_adjust(bottom=0.2)
    
    # 璁剧疆X杞村埢搴︿负鏃ユ湡鏃堕棿
    ax.xaxis_date()
    plt.xticks(rotation=45)
    plt.yticks()
    plt.title(u"鑲＄エ浠ｇ爜锛�" + quote_code)
    plt.xlabel(u"鏃堕棿")
    plt.ylabel(u"鑲′环锛堝厓锛�")
    mpf.candlestick_ohlc(ax, data_list, width=0.9, colorup='red', colordown='green')
    ax.autoscale_view()
    plt.grid()
    plt.show()
    pass

if __name__ == "__main__":
    drawKFig(quote_code='601668', start_date='2016-05-29', end_date='2017-06-12')
    print("hello gittest")