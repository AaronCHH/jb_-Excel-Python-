# Ch07 數值操作

## 數值取代
### 一對一取代

import numpy as np
import pandas as pd
df = pd.read_excel(r"..\data\test7.xlsx", sheet_name="7-1")
df

#將240歲的年齡取代成33歲
df["年齡"].replace(240,33,inplace=True)
df


df = pd.read_excel(r"..\data\test7.xlsx", sheet_name="7-1b")
df

df.replace(np.NaN,0)

### 多對一取代

df = pd.read_excel(r"C:\ACD019600\data\test7.xlsx", sheet_name="7-1c")
df

df.replace([240,260,280],33)

### 多對多取代

df

df.replace({240:32,260:33,280:34})

## 數值排序
### 按照一欄數值排序

df = pd.read_excel(r"..\data\test7.xlsx")
df

#按照銷售ID昇冪排列
df.sort_values(by = ["銷售ID"])

#按照銷售ID降冪排列
df.sort_values(by = ["銷售ID"],ascending = False)

### 按照有缺失值的列進行排序

df = pd.read_excel(r"C:\ACD019600\data\test7.xlsx", sheet_name="工作表2")
df

df.sort_values(by = ["銷售ID"])

df.sort_values(by = ["銷售ID"],na_position = "first")

### 按照多欄數值進行排序

df = pd.read_excel(r"C:\ACD019600\data\test7.xlsx")
df

df.sort_values(by = ["銷售ID","成交時間"],ascending = [True,False])

## 數值排名

df = pd.read_excel(r"C:\ACD019600\data\test7.xlsx")
df["銷售ID"]

df["銷售ID"].rank(method = "average")

df["銷售ID"].rank(method = "first")

df["銷售ID"].rank(method = "min")

df["銷售ID"].rank(method = "max")

## 數值刪除
### 刪除欄

df

df.drop(["銷售ID","成交時間"],axis = 1)

#刪除第5欄和第6欄
df.drop(df.columns[[4,5]],axis = 1)

df.drop(columns = ["銷售ID","成交時間"])

### 刪除列

df = pd.read_excel(r"C:\ACD019600\data\test7.xlsx")
df.index = ("0a","1b","2c","3d","4e")
df

df.drop(["0a","1b"],axis = 0)

#刪除第一列和第二列資料
df.drop(df.index[[0,1]],axis = 0)

#刪除第一列和第二列資料
df.drop(index = ["0a","1b"])

### 刪除特定列

df = pd.read_excel(r"C:\ACD019600\data\test7.xlsx")
df

df[df["年齡"]<40]

## 數值計數

df = pd.read_excel(r"..\data\test7.xlsx")
df

df["銷售ID"]

df["銷售ID"].value_counts()

df["銷售ID"].value_counts(normalize = True)

df["銷售ID"].value_counts(normalize = True,sort = False)

## 唯一值取得

df

df["銷售ID"].unique()

## 數值查詢

df

#查詢年齡這一欄是否包含31、21這兩個值
df["年齡"].isin([31,21])

#全表中是否包含A2、31這兩個值
df.isin(["A2",31])

## 區間切分

df = pd.read_excel(r"..\data\test7.xlsx", sheet_name="工作表4")
df

pd.cut(df["年齡"],bins = [0,3,6,10])

#將數據切分成3份
pd.qcut(df["年齡"],3)

## 插入新的列或欄

df = pd.read_excel(r"..\data\test7.xlsx")
df

#在第二欄後插入一欄並命名為商品類別
df.insert(2,"商品類別",["cat01","cat02","cat03","cat04","cat05"])
df

df["商品類別"] = ["cat01","cat02","cat03","cat04","cat05"]
df

df.insert(3, "test", df['年齡']/df['年齡']) # INSERT DATAFRAME

df

## 欄列互換

df

df.T

df.T.T

## 索引重塑

df = pd.DataFrame([[1,2,3],[4,5,6]],
                  columns =["C1","C2","C3"], 
                  index=["S1","S2"])
df

df.stack()

df.stack().unstack()

## 長寬表轉換
### 寬表轉換為長表

df = pd.read_excel(r"..\data\test7.xlsx", sheet_name="工作表5")
df

df.set_index(["Company","Name"])

df.set_index(["Company","Name"]).stack()

df.set_index(["Company","Name"]).stack().reset_index()

df.melt(id_vars = ["Company","Name"],
        var_name = "Year",
        value_name = "Sale")

df = pd.read_excel(r"C:\ACD019600\data\test7.xlsx", sheet_name="工作表6")
df

### 長表轉換為寬表

df.pivot_table(index = ["Company","Name"],columns = "Year",values = "Sale")

## apply()與applymap()函式

df = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]],columns =["C1","C2","C3"])
df

#對C1列中的每一個元素加1
df["C1"].apply(lambda x:x+1)

#對df表中的每一個元素加1
df.applymap(lambda x:x+1)

