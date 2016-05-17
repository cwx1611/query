'''
Created on 2016年5月9日

@author: Administrator
'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from WindPy import w
import pymysql
import datetime

w.start();

def saveSecurityCodes(securityCodes,queryDate, nextDate):
    
    if securityCodes.ErrorCode!=0:
        print('error code:'+str(securityCodes.ErrorCode)+'\n');
        return();
    print('Data length:',len(securityCodes.Data[0]))
    conn=pymysql.connect(host='192.168.10.189',user='cc',passwd='cc2718281828',db='AMGMH',charset='utf8')
    cur=conn.cursor()
    for i in range(0,len(securityCodes.Data[0])):
        #print("securityCodes.Data[1][i]=%s",securityCodes.Data[1][i])
        #print("securityCodes.Data[0][i]=%s",securityCodes.Data[0][i])
        checkValue=[securityCodes.Data[0][i],securityCodes.Data[1][i]]
        checkExist = cur.execute("select begin_date, end_date from WSETSecurityCode where \
                wind_code=%s and sec_name= %s",checkValue)
        #print(checkExist)
        if(checkExist==0):
            #说明是新的证券
            print("New Security")
            insertValue=(queryDate,nextDate,securityCodes.Data[0][i],securityCodes.Data[1][i])
            cur.execute("insert into WSETSecurityCode values(%s,%s,%s,%s)",insertValue)
        else:
            #更新证券
            #print("Update Security")
            updateValue=(nextDate,queryDate,securityCodes.Data[0][i],securityCodes.Data[1][i])
            cur.execute("update WSETSecurityCode set end_date=%s \
                    where end_date=%s and wind_code=%s and sec_name= %s",updateValue)
    conn.commit()
    cur.close()
    conn.close()

def queryDataByDate(begin, end, mkt="SSE"):
    # 所有A股
    sectorid="a001010100000000"
    if(mkt=="CFFEX"):
        sectorid="a599010101000000"
    elif(mkt=="SHFE"):
        sectorid="a599010201000000"
    elif(mkt=="DCE"):
        sectorid="a599010301000000"
    elif(mkt=="CZCE"):
        sectorid="a599010401000000"
    else:
        print("Bad Market NAME,DEFAULT　SSE")
    
    conn=pymysql.connect(host='192.168.10.189',user='cc',passwd='cc2718281828',db='AMGMH',charset='utf8')
    cur=conn.cursor()
    
    try:
        cur.execute("select t1.DateTime, min(t2.DateTime) as nextDate from TDays t1, TDays t2 \
                where t1.TradingCalendar=t2.TradingCalendar and t1.DateTime<t2.DateTime and \
                t1.TradingCalendar='%s' and t1.DateTime>='%s' and t1.DateTime<='%s' \
                group by t1.DateTime"%(mkt, begin, end))
        results = cur.fetchall()
        for row in results:
            print(row[0])
            print(row[1])
            paramStr="date="+row[0].strftime("%Y%m%d")+";sectorid="+sectorid+";field=wind_code,sec_name"
            print(paramStr)
            securityCodes = w.wset("sectorconstituent","%s"%(paramStr))
            saveSecurityCodes(securityCodes, row[0], row[1])
    except:
        print("Error when query trade date")
    cur.close()
    conn.close()
    

#queryDataByDate("2012-12-01","2016-03-31","CFFEX")
#queryDataByDate("2012-12-01","2016-03-31","SHFE")
#queryDataByDate("2012-12-01","2016-03-31","CZCE")
#queryDataByDate("2012-12-01","2016-03-31","DCE")
queryDataByDate("2013-01-18","2016-03-31","SSE")

w.stop();

