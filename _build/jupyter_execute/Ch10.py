# Ch10 資料分組/樞紐分析表

## 資料分組
### 分組鍵是欄名

import pandas as pd
df = pd.read_excel("../data/test10.xlsx")
df

df.groupby("客戶分類")

df.groupby("客戶分類").count()

df.groupby("客戶分類").sum()

#對分組後的資料進行計數運算
df.groupby(["客戶分類","區域"]).count()

#對分組後的資料進行求和運算
df.groupby(["客戶分類","區域"]).sum()

df.groupby("客戶分類")

df.groupby("客戶分類")["使用者ID"].count()

### 分組鍵是Series

df

df["客戶分類"]

#對分組以後的資料進行計數運算
df.groupby("客戶分類")

#對分組以後的資料進行計數運算
df.groupby(df["客戶分類"])

#對分組以後的資料進行計數運算
df.groupby("客戶分類").count()

#對分組以後的資料進行計數運算
df.groupby(df["客戶分類"]).count()

#對分組以後的資料進行求和運算
df.groupby(["客戶分類","區域"]).sum()

#對分組以後的資料進行求和運算
df.groupby([df["客戶分類"],df["區域"]]).sum()

### 神奇的aggregate方法

df = pd.read_excel("../data/test10.xlsx", sheet_name="工作表2")
df

df.columns

df.groupby("客戶分類").aggregate(["count","sum"])

df.groupby("客戶分類").aggregate({
    "使用者ID":"count",
    "7月銷量":"sum",
    "8月銷量":"sum"})

### 對分組後的結果重置索引

df.groupby("客戶分類").sum()

df.groupby("客戶分類").sum().reset_index()

## 樞紐分析表

df = pd.read_excel("../data/test10.xlsx")

df

pd.pivot_table(df,
               values = "使用者ID",
               columns = "區域",
               index = "客戶分類",
               aggfunc='count')

pd.pivot_table(df,
               values = "使用者ID",
               columns = "區域",
               index = "客戶分類",
               aggfunc='count')

pd.pivot_table(df,values = "使用者ID",
               columns = "區域",
               index = "客戶分類",
               aggfunc='count',
               margins = True)

pd.pivot_table(df,values = "使用者ID",
               columns = "區域",
               index = "客戶分類",
               aggfunc='count',
               margins = True,
               margins_name = "總計")

#將缺失值填充為0
pd.pivot_table(df,
               values = "使用者ID",
               columns = "區域",
               index = "客戶分類",
               aggfunc='count',
               margins = True,
               fill_value = 0)

pd.pivot_table(df,
               values = ["使用者ID",
                         "7月銷量"],
               columns = "區域",
               index = "客戶分類",
               aggfunc={"使用者ID":"count",
                        "7月銷量":"sum"})

pd.pivot_table(df,
               values = "使用者ID",
               columns = "區域",
               index = "客戶分類",
               aggfunc='count')

print('Done!')

