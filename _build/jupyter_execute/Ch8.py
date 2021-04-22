# Ch08 資料運算
## 算術運算

import pandas as pd
data = {"C1":[1,4],"C2":[2,5],"C3":[3,6]}
df = pd.DataFrame(data,index = ["S1","S2"])
df

df["C1"] + df["C2"]

df["C1"] - df["C2"]

df["C1"] * df["C2"]

df["C1"] / df["C2"]

df["C1"] + 2

df["C1"] - 2

df["C1"] * 2

df["C1"] / 2

## 比較運算

df

df["C1"] > df["C2"]

df["C1"] != df["C2"]

df["C1"] < df["C2"]

## 彙總運算

### 非空格計數

df

df.count()

df.count(axis = 1)

df["C1"].count()

### sum求和

df

df.sum()

df.sum(axis = 1)

### mean求均值

df

df.mean()

df.mean(axis = 1)

df["C1"].mean()#對C1欄求均值

### max求最大值

df

df.max()

df.max(axis = 1)

df["C1"].max()#對C1欄求最大值

### min求最小值

df

df.min()

#求取每一列的最小值
df.min(axis = 1)


#求取C1欄的最小值
df["C1"].min()

### median求中位數

data = {"C1":[1,4,7],"C2":[2,5,8],"C3":[3,6,9]}
df = pd.DataFrame(data,index = ["S1","S2","S3"])
df

df.median()

#求取每一列的中位數
df.median(axis = 1)

#求取C1欄的中位數
df["C1"].median()

### mode求眾數

data = {"C1":[1,4,1],"C2":[4,4,6],"C3":[1,1,3]}
df = pd.DataFrame(data,index = ["S1","S2","S3"])
df

df.mode()

#求取每一列的眾數
df.mode(axis=1)

#求取C1欄的眾數
df["C1"].mode()


### var求變異數

data = {"C1":[1,4,7],"C2":[2,5,8],"C3":[3,6,9]}
df = pd.DataFrame(data,index = ["S1","S2","S3"])
df

df.var()

#求取每一列的變異數
df.var(axis = 1)

#求取C1欄的變異數
df["C1"].var()

### std求標準差

df

df.std()

#求取每一列的標準差
df.std(axis = 1)

#求取C1欄的標準差
df["C1"].std()

### quantile求分位數

data = {"C1":[1,4,7,10,13],"C2":[2,5,8,11,14],"C3":[3,6,9,12,15]}
df = pd.DataFrame(data,index = ["S1","S2","S3","S4","S5"])
df

df.quantile(0.25)#求四分之一分位數

df.quantile(0.75)#求四分之三分位數

#求取每一列的四分之一分位數
df.quantile(0.25, axis = 1)

#求取C1欄的四分之一分位數
df["C1"].quantile(0.25)

## 相關性運算

data = {"col1":[1,3,5,7,9],"col2":[2,4,6,8,10]}
df = pd.DataFrame(data,index = [0,1,2,3,4])
df

df["col1"].corr(df["col2"]) #求取col1欄與col2欄的相關係數

data = {"col1":[1,4,7,10,13],
             "col2":[2,5,8,11,14],
             "col3":[3,6,9,12,15]}
df = pd.DataFrame(data,index = [0,1,2,3,4])
df

#計算欄位col1、col2、col3兩兩之間的相關性
df.corr()

