# Ch11 多表拼接

## 表的橫向拼接
### 連接表的類型

import pandas as pd
data1 = {"名次":[1,2,3,4],
         "姓名":["小張","小王","小李","小趙"],
         "學號":["100","101","102","103"],
         "成績":[650,600,578,550]}
df1 = pd.DataFrame(data1)
df1

data2 = {"學號":["100","101","102","103"],
         "班級":["一班","一班","二班","二班"]}
df2 = pd.DataFrame(data2)
df2

pd.merge(df1,df2)

data1 = {"姓名":["小張","小王","小李"],
         "學號":["100","101","102"],
         "f_成績":[650,600,578]}
df1 = pd.DataFrame(data1)
df1

data2 = {"學號":['100',"100","101","102","101","102"],
         "e_成績":[586,602,691,702,645,676]}
df2 = pd.DataFrame(data2)
df2

pd.merge(df1,df2,on = "學號")

data1 = {"姓名":["小張","小張","小王","小李","小李"],
         "學號":["100","100","101","102","102"],
         "f_成績":[650,610,600,578,542]}
df1 = pd.DataFrame(data1)
df1

data2 = {"學號":['100',"100","101","102","102"],
         "e_成績":[650,610,600,578,542]}
df2 = pd.DataFrame(data2)
df2

pd.merge(df1,df2)

### 連接鍵的類型

data1 = {"名次":[1,2,3,4],
         "姓名":["小張","小王","小李","小趙"],
         "學號":["100","101","102","103"],
         "成績":[650,600,578,550]}
df1 = pd.DataFrame(data1)
df1

data2 = {"學號":["100","101","102","103"],
         "班級":["一班","一班","二班","三班"]}
df2 = pd.DataFrame(data2)
df2

pd.merge(df1,df2)

pd.merge(df1,df2,on = "學號")

df1

data2 = {"姓名":["小張","小王","小李","小趙"],
         "學號":["100","101","102","103"],
         "班級":["一班","一班","二班","三班"]}
df2 = pd.DataFrame(data2)
df2

pd.merge(df1,df2,on = ["姓名","學號"])

data1 = {"名次":[1,2,3,4],
         "姓名":["小張","小王","小李","小趙"],
         "編號":["100","101","102","103"],
         "成績":[650,600,578,550]}
df1 = pd.DataFrame(data1)
df1

data2 = {"學號":["100","101","102","103"],
         "班級":["一班","一班","二班","三班"]}
df2 = pd.DataFrame(data2)
df2

pd.merge(df1,df2,left_on = "編號",right_on = "學號")

df1 = pd.read_excel("../data/test11.xlsx", index_col = 0)
df1

df2 = pd.read_excel("../data/test11.xlsx", sheet_name="df2", index_col = 0)
df2

pd.merge(df1,df2,left_index = True,right_index = True)

df1

df2 = pd.read_excel("../data/test11.xlsx", sheet_name="df2")
df2

pd.merge(df1,df2,left_index = True,right_on = "學號")

### 連接方式

data1 = {"名次":[1,2,3,4],
         "姓名":["小張","小王","小李","小趙"],
         "學號":["100","101","102","103"],
         "成績":[650,600,578,550]}
df1 = pd.DataFrame(data1)
df1

data2 = {"姓名":["小張","小王","小李","小錢"],
         "學號":["100","101","102","104"],
         "班級":["一班","一班","二班","三班"]}
df2 = pd.DataFrame(data2)
df2

pd.merge(df1,df2,on = "學號",how = "inner")

pd.merge(df1,df2,on = "學號",how = "left")

pd.merge(df1,df2,on = "學號",how = "right")

pd.merge(df1,df2,on = "學號",how = "outer")

###  重複欄名處理

df1

df2

pd.merge(df1,df2,on = "學號",how = "inner")

#為重複的欄名加尾碼_L和_R
pd.merge(df1,df2,on = "學號",how = "inner",suffixes = ["_L","_R"])

## 表的縱向拼接
### 普通合併

df1 = pd.read_excel("../data/test11.xlsx", sheet_name="11-2a", index_col = 0)
df1

df2 = pd.read_excel("../data/test11.xlsx", sheet_name="11-2b", index_col = 0)
df2

pd.concat([df1,df2])

### 索引設定

pd.concat([df1,df2],ignore_index = True)

### 重疊資料合併

df1 = pd.read_excel("../data/test11.xlsx", sheet_name="11-2-3", index_col = 0)
df1

df2

pd.concat([df1,df2],ignore_index = True)

pd.concat([df1,df2],ignore_index = True).drop_duplicates()

print('Done!')

