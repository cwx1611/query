'''
Created on 2016年4月26日

@author: cc
'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from WindPy import w
import pymysql

w.start();

def saveTradeDate(tradeDates,mktName):
    if tradeDates.ErrorCode!=0:
        print('error code:'+str(tradeDates.ErrorCode)+'\n');
        return();
    print('Data length:',len(tradeDates.Data[0]))
    conn=pymysql.connect(host='192.168.10.189',user='cc',passwd='cc2718281828',db='AMGMH',charset='utf8')
    cur=conn.cursor()
    for i in range(0,len(tradeDates.Data[0])):
        strTemp=''
        if len(tradeDates.Times)>1:
            strTemp=str(tradeDates.Times[i])+' '
        for k in range(0, len(tradeDates.Fields)):
            strTemp=strTemp+str(tradeDates.Data[k][i])+' '
            value=[mktName,str(tradeDates.Data[k][i])]
            cur.execute('insert into TDays values(%s,%s)',value)
            #print(status)
        #print(strTemp)
    conn.commit()
    cur.close()
    conn.close()
        
sseTradeDate = w.tdays('2005-12-01', '2016-12-31', 'TradingCalendar=SSE')
saveTradeDate(sseTradeDate,'SSE')
szseTradeDate = w.tdays('2005-12-01', '2016-12-31', 'TradingCalendar=SZSE')
saveTradeDate(szseTradeDate,'SZSE')
cffeTradeDate = w.tdays('2005-12-01', '2016-12-31', 'TradingCalendar=CFFEX')
saveTradeDate(cffeTradeDate,'CFFEX')
dceTradeDate = w.tdays('2005-12-01', '2016-12-31', 'TradingCalendar=DCE')
saveTradeDate(dceTradeDate,'DCE')
czceTradeDate = w.tdays('2005-12-01', '2016-12-31', 'TradingCalendar=CZCE')
saveTradeDate(czceTradeDate,'CZCE')
shfeTradeDate = w.tdays('2005-12-01', '2016-12-31', 'TradingCalendar=SHFE')
saveTradeDate(shfeTradeDate,'SHFE')
w.stop();
