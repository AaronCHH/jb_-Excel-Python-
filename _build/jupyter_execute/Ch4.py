# Ch04 取得資料來源
## 匯入外部資料

### 匯入.xlsx

# 基本匯入
import pandas as pd
df = pd.read_excel(r"..\data\test.xlsx")
df

df.info()

df.describe()

df.dtypes

#路徑前面不加r
df = pd.read_excel("../data/test.xlsx")
df

df.dtypes

#指定匯入哪個Sheet
df = pd.read_excel("../data/test.xlsx", sheet_name="工作表1")
df

df.dtypes

df = pd.read_excel("C:/ACD019600/data/test.xlsx", sheet_name = 0)
df

df = pd.read_excel("C:/ACD019600/data/test.xlsx", sheet_name = 0, index_col = 0)
df

#使用第一列作為欄索引
df = pd.read_excel("C:/ACD019600/data/test.xlsx", sheet_name = 0,header = 0)
df

#使用第1列行作為欄索引
df = pd.read_excel("C:/ACD019600/data/test.xlsx", sheet_name = 0,header = 1)
df

#使用預設從0開始的數作為欄索引
df = pd.read_excel("C:/ACD019600/data/test.xlsx", sheet_name = 0,header = None)
df

#匯入指定欄
df = pd.read_excel("C:/ACD019600/data/test.xlsx", usecols = [0])
df

# 以列表形式匯入多個指定欄
df = pd.read_excel("C:/ACD019600/data/test.xlsx", usecols = [0,2])
df

### 匯入.csv

import pandas as pd
df = pd.read_csv(r"C:\ACD019600\data\test.csv")
df

df = pd.read_csv(r"C:\ACD019600\data\test1.csv")
df

df = pd.read_csv(r"C:\ACD019600\data\test1.csv",sep = " ")
df

# 指定讀取列數
df = pd.read_csv(r"C:\ACD019600\data\test1.csv",sep = " ",nrows = 2)
df

df1 = pd.read_csv(r"C:\ACD019600\data\test2.csv",encoding = "utf-8")
df1

df1 = pd.read_csv(r"C:\ACD019600\data\test2.csv")
df1

df1 = pd.read_csv(r"C:\ACD019600\data\test3.csv",encoding = "big5")
df1

df1 = pd.read_csv(r"C:\ACD019600\新增資料夾\test.csv")
df1

df1 = pd.read_csv(r"C:\ACD019600\新增資料夾\test.csv", engine = "python",encoding = "utf-8-sig")
df1

### 匯入.txt

#利用read_table()匯入.txt
import pandas as pd
df1 = pd.read_csv(r"C:\ACD019600\data\test.txt",sep = " ")
df1

## 新增資料
（本節無範例）

## 熟悉資料
### 利用head預覽前幾行

df = pd.read_csv(r"C:\ACD019600\data\test_head.csv")
df

df.head() #預設顯示前5列

df.head(2)#只顯示前2列

### 利用shape取得資料表的大小

df = pd.read_csv(r"C:\ACD019600\data\test.csv")
df

df.shape

### 利用info取得資料類型

df

df = pd.read_excel(r"C:\ACD019600\data\test.xlsx")
df
df.info()

### 利用describe取得數值分佈情況

df.describe()

# 含有多欄數值型別欄位的DataFrame
df = pd.DataFrame([[20,5000,2],[25,8000,3],[30,9000,3],[28,7000,2]], columns = ["年齡","收入","家屬數"])
df

df.describe()

