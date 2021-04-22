# Ch03 Pandas資料結構
## Series資料結構

# 傳入一個列表
import pandas as pd
S1 = pd.Series(["a","b","c","d"])
S1

# 指定索引
S2 = pd.Series([1,2,3,4],index = ["a","b","c","d"])
S2

# 傳入一個字典
S3 = pd.Series({"a":1,"b":2,"c":3,"d":4})
S3

# 利用index方法取得Series的索引
S1.index

S2.index

# 利用values方法取得Series的值
S1.values

S2.values

## DataFrame 表格型資料結構

# 傳入一個列表
import pandas as pd
df1 = pd.DataFrame(["a","b","c","d"])
df1

# 傳入一個嵌套列表
import pandas as pd
df2 = pd.DataFrame([["a","A"],["b","B"],["c","C"],["d","D"]])
df2

#設定欄索引
df31 = pd.DataFrame([["a","A"],["b","B"],["c","C"],["d","D"]], columns = ["小寫","大寫"])
df31

#設定列索引
df32 = pd.DataFrame([["a","A"],["b","B"],["c","C"],["d","D"]], index = ["一","二","三","四"])
df32

#列、欄索引同時設定
df33 = pd.DataFrame([["a","A"],["b","B"],["c","C"],["d","D"]], columns = ["小寫","大寫"], index = ["一","二","三","四"])
df33

#傳入一個字典
data = {"小寫":["a","b","c","d"],"大寫":["A","B","C","D"]}
df41 = pd.DataFrame(data)
df41

data = {"小寫":["a","b","c","d"],"大寫":["A","B","C","D"]}
df42 = pd.DataFrame(data,index = ["一","二","三","四"])
df42

#利用columns方法取得DataFrame的欄索引
df2.columns

df33.columns

#利用index方法取得DataFrame的列索引
df2.index

df33.index