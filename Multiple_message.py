#!/usr/bin/env python
# coding: utf-8

# In[3]:


import mysql.connector
import requests
  

url = "https://www.fast2sms.com/dev/bulkV2"
headers = {
    'cache-control': "no-cache"
}

try:
    conn = mysql.connector.connect(host='localhost',
                            database='sailes',
                            user='root',
                            password='BR@jesh9511')
    cursor = conn.cursor()

    fetchrecord  = """select * from Employees"""

    cursor.execute(fetchrecord)
    record = cursor.fetchall()

    for row in record:
        num = row[2]
        msg = row[3]
        querystring = {"authorization":"Jdy9ja2TsbpLOcVAUFD1txlSimYNeBMIHfwg70nXPr3ZzRCvGhlsBpNzrkJf1dua3TQXIiyRoFOVPAmL",
                       "message":msg,
                       "language":"english",
                       "route":"q",
                       "numbers":num}
        response = requests.request("GET", url, headers=headers, params=querystring, verify=False)
        print(response.text)
        print(num,msg)
        
except Exception as e:
    print(e.args)

finally:
    cursor.close()
    conn.close()


# In[ ]:




