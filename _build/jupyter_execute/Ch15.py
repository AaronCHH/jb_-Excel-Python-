# Ch15 NumPy陣列

## NumPy簡介
（本節無範例）
## NumPy陣列的產生
### 產生一般陣列

import numpy as np
arr = np.array([2,4,6,8])
arr

arr = np.array([[1,2,3],[4,5,6]])
arr

### 產生特殊類型陣列

#產生一個以1為開始，15為結束，3為步長的隨機序列
np.arange(1,15,3)

#產生一個以1開始，15為結束，步長預設的隨機序列
np.arange(1,15)

#產生一個以15為結束，步長預設為1的隨機序列
np.arange(15)

#產生長度為3的0陣列
np.zeros(3)

#產生2行3列的一個陣列
np.zeros((2,3))

#產生長度為3的1陣列
np.ones(3)

np.ones((2,3))

#產生一個3×3的單位矩陣
np.eye(3)

### 產生亂數組

#產生長度為3的位於(0,1)之間的亂數組
np.random.rand(3)

#產生2行3列值位於(0,1)之間的陣列
np.random.rand(2,3)

#產生長度為3的滿足常態分佈的亂數組
np.random.randn(3)

#在區間[1,5)產生長度為10的亂數組
np.random.randint(1,5,10)

#在區間[0,5)上產生長度為10的亂數組
np.random.randint(5,size=10)

#在區間[0,5)產生2行3列的亂數組
np.random.randint(5,size = (2,3))

#從陣列a中選取2行3列的數值組成一個新的陣列
np.random.choice(5,(2,3))

arr = np.arange(10)
arr

np.random.shuffle(arr)
arr 

## NumPy陣列的基本屬性

#3行3列的陣列
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
arr

arr.shape

#arr陣列共有9個元素
arr.size

#arr陣列的類型為int
arr.dtype

#arr陣列為2維陣列
arr.ndim

#arr1陣列為1維陣列
arr1 = np.array([1,2,3])
arr1

arr1.ndim

## NumPy陣列的資料選取
### 一維資料選取

arr = np.arange(10)
arr

#取得第4位的數，即傳入3
arr[3]

#取得末端最後一個數值
arr[-1]

#取得末端倒數第二個數值
arr[-2]

#取得位置3到5的值，不包含位置5的值
arr[3:5]

#取得位置3以後的所有元素
arr[3:]

#取得位置3之前的所有元素
arr[:3]

#取得從第3位到倒數第2位的元素，不包括倒數第2位
arr[3:-2]

#取得陣列中大於3的元素
arr[arr > 3]

### 多維資料選取

# 建立一個多維陣列供使用
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
arr

#取得第2列資料
arr[1]

#取得第2列和第3列的資料，包括第3列
arr[1:3]

#取得第3列之前的所有行資料，不包括第3列
arr[:2]

#取得第2欄的資料
arr[:,1]

#取得第1到3欄的資料，不包括第3欄
arr[:,0:2]

#取得第3欄之前的所有欄，不包括第3欄
arr[:,:2]

#取得第2欄之後的所有欄，包括第2欄
arr[:,1:]

#取得第1到2列，第2到3欄的數據
arr[0:2,1:3]

## NumPy陣列的資料預處理
### NumPy陣列的類型轉換

arr = np.arange(5)
arr

#陣列arr的原資料類型為int32
arr.dtype

#將arr陣列從int類型轉換為float類型
arr_float = arr.astype(np.float64)
arr_float

arr_float.dtype

#將arr陣列從int類型轉換為str類型
arr_str = arr.astype(np.string_)
arr_str

arr_str.dtype

### NumPy陣列的缺失值處理

#建立一個含有缺失值的陣列，nan表示缺失值
arr = np.array([1,2,np.nan,4])
arr

# 第三位為缺失值
np.isnan(arr)

#用0填充
arr[np.isnan(arr)] = 0
arr

### NumPy陣列的重複值處理

arr = np.array([1,2,3,2,1])
np.unique(arr)

## NumPy陣列重塑
### 一維陣列重塑

#新增一個一維陣列
arr = np.arange(8)
arr

#將陣列重塑為4欄2列的多維陣列
arr.reshape(2,4)

#將陣列重塑為2欄4列的多維陣列
arr.reshape(4,2)

### 多維陣列重塑

#新增一個多維陣列
arr = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]]) 
arr

#將陣列重塑為3欄4列
arr.reshape(4,3)

#將陣列重塑為6欄2列
arr.reshape(2,6)

### 陣列轉置

arr

arr.T

## NumPy陣列合併
### 橫向合併

# 先新增兩個陣列，用來進行合併
arr1 = np.array([[1,2,3],[4,5,6]])
arr2 = np.array([[7,8,9],[10,11,12]])

# concatenate方法
np.concatenate([arr1,arr2],axis = 1)

# hstack方法
np.hstack((arr1,arr2))

# column_stack方法
np.column_stack((arr1,arr2))

### 縱向合併

# concatenate方法
np.concatenate([arr1,arr2],axis = 0)

np.vstack((arr1,arr2))

np.row_stack((arr1,arr2))

## 常用資料分析函式
### 元素級函式

#新增一個陣列
arr = np.arange(4)
arr

#求取各個元素的平方
np.square(arr)

#求取各個元素的平方根
np.sqrt(arr)

### 描述統計函式

#新增一個陣列
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
arr

#對整個陣列進行求和
arr.sum()

#對陣列中的每一列分別求和
arr.sum(axis = 1)

#對陣列中的每一欄分別求和
arr.sum(axis = 0)

#對整個陣列進行求均值
arr.mean()

#對陣列中的每一列分別求均值
arr.mean(axis = 1)

#對陣列中的每一欄分別求均值
arr.mean(axis = 0)

#對整個陣列求最大值
arr.max()

#對陣列中的每一列分別求最小值
arr.max(axis = 1)

#對陣列中的每一欄分別求最大值
arr.max(axis = 0)

### 條件函式

#新增一個陣列用來儲存學生成績
arr = np.array([56,61,65])
#大於60及格，小於60不及格
np.where(arr>60,"及格","不及格")

#傳回滿足條件的值對應的位置
np.where(arr>60)

### 集合關係

#新增兩個陣列
arr1 = np.array([1,2,3,4])
arr2 = np.array([1,2,5])

#包含
np.in1d(arr1,arr2)

#交集
np.intersect1d(arr1,arr2)

#並集
np.union1d(arr1,arr2)

#差集
np.setdiff1d(arr1,arr2)

