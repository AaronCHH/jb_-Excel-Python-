# Ch09 時間序列

## 取得現在的時間
### 傳回現在的日期和時間

from datetime import datetime
datetime.now()

### 分別傳回現在的年、月、日

# 傳回年
datetime.now().year

# 傳回月
datetime.now().month

# 傳回日
datetime.now().day

### 傳回現在的周數

# 傳回今天是星期幾，因為Python中周幾是從0開始數的，周日傳回的是6，所以在後面加1
datetime.now().weekday()+1

datetime.now().isocalendar()

datetime.now().isocalendar()[1]#傳回周數

## 指定日期和時間的格式

# 只顯示日期
datetime.now().date()

# 只顯示時間
datetime.now().time()

# 用strftime()函式自訂時間和日期的格式
datetime.now().strftime('%Y-%m-%d')

datetime.now().strftime("%Y-%m-%d %H:%M:%S")

## 字串和時間格式相互轉換
### 將時間格式轉換為字串格式

#新增一個時間格式的時間
now = datetime.now()
now

type(now)#查看變數now的資料類型

type(str(now))

### 將字串格式轉換為時間格式

#新增一個字串格式的時間
str_time = "2018-10-14"
type(str_time)#查看變數str_time的資料類型

from dateutil.parser import parse
parse(str_time)#將字串解析為時間

type(parse(str_time))

## 時間索引

import pandas as pd
import numpy as np
index = pd.DatetimeIndex(['2018-01-01', '2018-01-02', '2018-01-03', '2018-01-04',
               '2018-01-05', '2018-01-06', '2018-01-07', '2018-01-08',
               '2018-01-09', '2018-01-10'])
data = pd.DataFrame(np.arange(1,11),columns = ["num"],index = index)
data

# 取得2018年的資料
data["2018"]

# 取得2018年1月的資料：
data["2018-01"]

# 取得2018年1月1日到2018年1月5日的資料：
data["2018-01-01":"2018-01-05"]

# 取得2018年1月1日的資料：
data["2018-01-01":"2018-01-01"]

df = pd.read_excel(r"C:\ACD019600\data\test8.xlsx")
df

#選取成交時間為2018年8月8日的訂單
df[df["成交時間"] == datetime(2018,8,8)]

#選取成交時間在2018年8月9日之後的訂單
df[df["成交時間"] > datetime(2018,8,9)]

#選取成交時間在2018年8月10日之前的訂單
df[df["成交時間"] < datetime(2018,8,10)]

#選取成交時間在2018年8月8到2018年8月11之間的訂單
df[(df["成交時間"] > datetime(2018,8,8))&(df["成交時間"] < datetime(2018,8,11))]

## 時間運算
### 兩個時間之差

diff = datetime(2018,5,21,19,50) - datetime(2018,5,18,20,32)
diff

diff.days #傳回天的時間差

diff.seconds #傳回秒的時間差

diff.seconds/3600 #換算成小時的時間差

### 時間偏移

# timedelta
from datetime import timedelta
date = datetime(2018,5,18,20,32)
#往後推1天
date + timedelta(days = 1)

#往後推60秒
date + timedelta(seconds = 60)

#往前推1天
date - timedelta(days = 1)

#往前推60秒
date - timedelta(seconds = 60)

# date offset
from pandas.tseries.offsets import Day,Hour,Minute
date = datetime(2018,5,18,20,32)

#往後推1天
date + Day(1)

#往後推1小時
date + Hour(1)

#往後推10分鐘
date + Minute(10)

#往前推1天
date - Day(1)

#往前推1小時
date - Hour(1)

#往前推10分鐘
date - Minute(10)

