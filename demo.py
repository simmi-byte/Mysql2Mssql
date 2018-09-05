# -*- coding: utf-8 -*-
"""
Created on Tue Aug 07 14:46:56 2018

@author: finere
"""
import os  
import sys
import pymysql
import pymssql
reload(sys)
sys.setdefaultencoding('utf8')
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
mssql_conn = pymssql.connect(server="localhost",port="3723",user="admin",password="admin",database="Cash",charset="utf8")
mysql_conn = pymysql.connect(host='localhost',port= 3306,user = 'admin',passwd='admin',db='IntForce',charset="utf8")
#mysql2mssql
mysql_cur = mysql_conn.cursor()

mysql_cur.execute("select Id,PhysicalZoneName,FlowDateTime,ZoneTypeName,Zone_Enter,Zone_Exit,UpdateTime from T_Zone_Flow where To_DAYS(UpdateTime)=TO_DAYS(now())")
resultmysql = mysql_cur.fetchall()
mssql_cur = mssql_conn.cursor()
for row in resultmysql:
    if row[0]==0:
       mssql_conn.commit()
       oracle_conn.close()
       mssql_conn.close()
       mysql_conn.close() 
    else:
        mssql_cur.execute("insert into [Cash].[dbo].[T_Zone_Flow] ( Id,PhysicalZoneName,FlowDateTime,ZoneTypeName,Zone_Enter,Zone_Exit,UpdateTime ) values(%s,%s,%s,%s,%s,%s,%s)",(row))
mssql_conn.commit()
mssql_conn.close()
mysql_conn.close()
