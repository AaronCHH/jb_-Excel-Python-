# Ch05 數據預處理

## 缺失值處理
### 缺失值查看

import pandas as pd
df = pd.read_excel(r"C:\ACD019600\data\test5.xlsx", sheet_name="5-1-1")
df

df.info()

df.isnull()

### 缺失值刪除

df = pd.read_excel(r"C:\ACD019600\data\test5.xlsx", sheet_name="5-1-2")
df

df.dropna()

df

df.dropna(how = "all")

### 缺失值填補

df = pd.read_excel(r"C:\ACD019600\data\test5.xlsx", sheet_name="5-1-3")
df

df.fillna(0)

df

df.fillna({"性別":"男"})#對性別進行填補

#分別對性別和年齡進行填充
df.fillna({"性別":"男","年齡":"30"})

## 重複值處理

df = pd.read_excel(r"C:\ACD019600\data\test5.xlsx", sheet_name="5-2")
df

df.drop_duplicates()

df

df.drop_duplicates(subset = "唯一識別碼")

df.drop_duplicates(subset = ["客戶姓名","唯一識別碼"])

#保留最後一個重複值
df.drop_duplicates(subset = ["客戶姓名","唯一識別碼"], keep = "last")

#不保留任何重複值
df.drop_duplicates(subset = ["客戶姓名","唯一識別碼"], keep = False)

## 異常值的檢測與處理
（本節無範例)

## 資料類型轉換
### 資料類型

df = pd.read_excel(r"C:\ACD019600\data\test5.xlsx", sheet_name="5-4")
df

df["訂單編號"].dtype #查看訂單編號這一欄的資料類型

df["唯一識別碼"].dtype #查看唯一識別碼這一欄的資料類型

### 類型轉換

df

df["唯一識別碼"].dtype #查看唯一識別碼這一列的資料類型

df["唯一識別碼"].astype("float64") #將唯一識別碼從int類型轉換為float類型

## 索引設定
### 為無索引表添加索引

import pandas as pd

df = pd.read_excel("../data/test5.xlsx", sheet_name="5-5")
df

df.info

df.describe()

df

# 為表添加欄索引
df.columns = ["訂單編號","客戶姓名","唯一識別碼","成交時間"]
df

#為表添加列索引
df.index = [1,2,3,4,5]
df

### 重新設定索引

df

df.set_index("訂單編號")

### 重新命名索引

df = pd.read_excel("../data/test5.xlsx", sheet_name="5-4")
df.index = [1,2,3,4,5,6]
df

#重新命名欄索引
df.rename(columns = {"訂單編號":"新訂單編號", "客戶姓名":"新客戶姓名"})

#重新命名列索引
df.rename(index = {1:"一",
                   2:"二",
                   3:"三"})


#同時重新命名列索引和欄索引
df.rename(columns = {"訂單編號":"新訂單編號",
                     "客戶姓名":"新客戶姓名"},
            index = {1:"一",
                     2:"二",
                     3:"三"})

### 重置索引(未完成，待確認)

# df = pd.DataFrame([[1,2],[3,4],[5,6],[7,8]],
#                   columns = ["C1","C2"],
#                   index = ["Z1","Z2","Z3","Z4"])
# df

df

df.reset_index()

df.reset_index(drop=True)

df = pd.read_excel("../data/test5.xlsx", sheet_name="5-5-4")
df

