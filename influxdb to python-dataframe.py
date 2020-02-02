#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from influxdb import InfluxDBClient
import pandas as pd
host='localhost'
port=8086
user = 'root'
password = 'root'
dbname = input("enter database\container name=")
client = InfluxDBClient(host,8086,user,password,dbname)
q='select * from '+ input("enter table name")
df = pd.DataFrame(client.query(q).get_points())
print(df)

