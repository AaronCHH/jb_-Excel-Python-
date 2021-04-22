# Ch12 結果匯出

## 匯出為Excel工作簿
### 設定檔案匯出路徑

import pandas as pd
data = {"使用者ID":[59224,55295,46035,2459,22179,22557],
        "客戶分類":["A類","B類","A類","C類","B類","A類"],
         "區域":["北區","南區","中區","北區","南區","中區"],
         "7月銷量":[6,37,8,7,9,42],
         "8月銷量":[20,27,1,8,12,20],
         "9月銷量":[0,35,8,14,4,55]}
df = pd.DataFrame(data)

df

df.to_excel(excel_writer = "../測試文件.xlsx")

### 設定Sheet名稱

df.to_excel(excel_writer = r"..\測試文件2.xlsx", sheet_name = "測試文件")

### 設定索引

df.to_excel(excel_writer = r"..\匯出文件.xlsx",
             sheet_name = "測試文件",
             index = False)

### 設定要匯出的欄位

df.to_excel(excel_writer = r"..\匯出文件2.xlsx",
             sheet_name = "測試文件",
             index = False,
             columns = ["使用者ID","7月銷量","8月銷量","9月銷量"])

### 設定編碼格式

df.to_excel(excel_writer = r"..\匯出文件3.xlsx",
             sheet_name = "測試文件",
             index = False,
             encoding = "utf-8"
           )

### 缺失值處理

df.to_excel(excel_writer = r"..\匯出文件4.xlsx",
             sheet_name = "測試文件",
             index = False,
             encoding = "utf-8",
             na_rep = 0 #缺失值填充為0
             )

### 無窮值處理

float("inf")

float("-inf")

## 匯出為.csv檔

import numpy as np
data20 = {"使用者ID":[59224,55295,46035,2459,22179,22557],
        "客戶分類":["A類","B類","A類","C類","B類","A類"],
         "區域":["北區","南區","中區","北區","南區","中區"],
         "7月銷量":[6,np.inf,8,7,9,42],
         "8月銷量":[20,27,1,8,12,20],
         "9月銷量":[0,35,8,14,4,55]}
df = pd.DataFrame(data20)
df

df.to_excel(excel_writer = r"..\匯出文件.xlsx",
             sheet_name = "測試文件",
             index = False,
             encoding = "utf-8",
             na_rep = 0,#缺失值填充為0
             inf_rep = 0#無窮值填充為0             
)


### 設定檔案匯出路徑

df.to_csv(path_or_buf = r"..\匯出文件.csv")

### 設定索引

df.to_csv(path_or_buf = r"..\匯出文件2.csv",
             index = False)

### 設定要匯出的欄位

df.to_csv(path_or_buf = r"..\匯出文件3.csv",
             index = False,
             columns = ["用戶ID","7月銷量","8月銷量","9月銷量"])

### 設定分隔符號

df.to_csv(path_or_buf = r"..\匯出文件4.csv",
             index = False,
             columns = ["用戶ID","7月銷量","8月銷量","9月銷量"],
             sep = ",")

### 缺失值處理

df.to_csv(path_or_buf = r"..\匯出文件5.csv",
             index = False,
             columns = ["用戶ID","7月銷量","8月銷量","9月銷量"],
             sep = ",",
             na_rep = 0)

### 設定編碼格式

df.to_csv(path_or_buf = r"..\匯出文件6.csv",
             index = False,
             columns = ["用戶ID","7月銷量","8月銷量","9月銷量"],
             sep = ",",
             na_rep = 0,
             encoding = "big5")

## 將檔案匯出到多個Sheet

data1 = {"使用者ID":[59224,55295,46035,2459,22179,22557],
        "客戶分類":["A類","B類","A類","C類","B類","A類"],
         "區域":["北區","南區","中區","北區","南區","中區"],
         "7月銷量":[6,37,8,7,9,42]}
df1 = pd.DataFrame(data1)         
df1 

data2 = {"使用者ID":[59224,55295,46035,2459,22179,22557],
        "客戶分類":["A類","B類","A類","C類","B類","A類"],
         "區域":["北區","南區","中區","北區","南區","中區"],
         "8月銷量":[20,27,1,8,12,20]}
df2 = pd.DataFrame(data2)
df2

data3 = {"使用者ID":[59224,55295,46035,2459,22179,22557],
        "客戶分類":["A類","B類","A類","C類","B類","A類"],
         "區域":["北區","南區","中區","北區","南區","中區"],
         "9月銷量":[0,35,8,14,4,55]}
df3 = pd.DataFrame(data3)
df3

#宣告一個讀寫物件
#excelpath為檔案要存放的路徑與檔名
excelpath = "../12-3.xlsx"
writer = pd.ExcelWriter(excelpath,engine = "xlsxwriter")

#分別將表df1、df2、df3寫入Excel中的Sheet1、Sheet2、Sheet3
#並命名為7月、8月、9月
df1.to_excel(writer,sheet_name = "7月")
df2.to_excel(writer,sheet_name = "8月")
df3.to_excel(writer,sheet_name = "9月")

#保存讀寫的內容
writer.save()


print('Done!')