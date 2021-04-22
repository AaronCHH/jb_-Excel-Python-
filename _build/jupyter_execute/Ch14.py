# Ch14 典型資料分析案例

## 利用Python實現報表自動化

# 匯入來源資料
import pandas as pd
from datetime import datetime
data = pd.read_csv(r"C:\ACD019600\data\order-14.1.csv",
                   parse_dates = ["成交時間"])
data.head()  #預覽數據
data.info()  #查看來源資料類型

# 計算本月相關指標
This_month = data[(data["成交時間"] >= datetime(2018,2,1))&
                (data["成交時間"] <= datetime(2018,2,28))]
sales_1 = (This_month["銷量"]*This_month["單價"]).sum()#銷售額計算
#客流量計算
traffic_1 = This_month["訂單ID"].drop_duplicates().count()
s_t_1 = sales_1/traffic_1#客單價計算
print("本月銷售額為:{:.2f},客流量為:{}, 客單價為:{:.2f}".format(sales_1,traffic_1,s_t_1))

# 計算上月相關指標
last_month = data[(data["成交時間"] >= datetime(2018,1,1))&
                (data["成交時間"] <= datetime(2018,1,31))]
sales_2 = (last_month["銷量"]*last_month["單價"]).sum() #銷售額計算

#客流量計算
traffic_2 = last_month["訂單ID"].drop_duplicates().count()
s_t_2 = sales_2/traffic_2 #客單價計算
print("本月銷售額為:{:.2f},客流量為:{}, 客單價為:{:.2f}".format(sales_2,traffic_2,s_t_2))

# 計算去年同期相關指標
same_month = data[(data["成交時間"] >= datetime(2017,2,1))&
                (data["成交時間"] <= datetime(2017,2,28))]
sales_3 = (same_month["銷量"]*same_month["單價"]).sum()#銷售額計算

#客流量計算
traffic_3 = same_month["訂單ID"].drop_duplicates().count()
s_t_3 = sales_3/traffic_3 #客單價計算
print("本月銷售額為:{:.2f},客流量為:{}, 客單價為:{:.2f}".format(sales_3,traffic_3,s_t_3))

# 利用函式提高編碼效率
def get_month_data(data):
    sale = ((data["單價"]*data["銷量"]).sum())
    traffic = data["訂單ID"].drop_duplicates().count()
    price = sale / traffic
    return (sale,traffic,price)

#計算本月相關指標
sale_1,traffic_1,s_t_1 = get_month_data(This_month)

#計算上月相關指標
sale_2,traffic_2,s_t_2 = get_month_data(last_month)

#計算去年同期相關指標
sale_3,traffic_3,s_t_3 = get_month_data(same_month)

report = pd.DataFrame([[sale_1,sale_2,sale_3], 
                       [traffic_1,traffic_2,traffic_3], 
                       [s_t_1,s_t_2,s_t_3]], columns = ["本月累計","上月同期","去年同期"], 
                      index = ["銷售額","客流量","客單價"])
report

report["環比"] = report["本月累計"]/report["上月同期"] - 1
report["同比"] = report["本月累計"]/report["去年同期"] - 1
report


report.to_csv(r"C:\ACD019600\data\report.csv", encoding = "utf-8-sig")

## 自動發送電子郵件

import smtplib
from email import encoders
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from email.mime.application import MIMEApplication


#寄件者email
asender="thisisdemo543@outlook.com"

#收件人email
areceiver="service@gotop.com.tw"

#副本email
acc = 'thisisdemo543@outlook.com'

#郵件主題
asubject = '這是一份測試郵件'  

#寄件者地址
from_addr = "thisisdemo543@outlook.com"

#郵件密碼（）
password="1234Data"

#郵件設定
msg = MIMEMultipart()
msg['Subject'] = asubject  
msg['to'] = areceiver  
msg['Cc'] = acc 
msg['from'] = "你的名字"

#郵件正文
body = "你好，這是一份測試郵件"

#添加郵件正文
msg.attach(MIMEText(body, 'plain', 'utf-8'))

#添加附件
#注意，這裡的檔案路徑是分隔線
xlsxpart = MIMEApplication(open('C:/ACD019600/data/這是附件.xlsx', 'rb').read())
xlsxpart.add_header('Content-Disposition', 
                          'attachment', 
                          filename='這是附件.xlsx')
msg.attach(xlsxpart) 

#設定郵箱伺服器位址及埠
smtp_server ="smtp-mail.outlook.com"
server = smtplib.SMTP(smtp_server, 587)
server.set_debuglevel(1)
server.ehlo()
server.starttls()

#登錄郵箱
server.login(from_addr, password)
#發送郵件
server.sendmail(from_addr, 
                      areceiver.split(',')+acc.split(','),
                      msg.as_string())
#斷開伺服器連接
server.quit()


## 假如你是某連鎖超市的資料分析師

import pandas as pd
from datetime import datetime
data = pd.read_csv(r"C:\ACD019600\data\order-14.3.csv",parse_dates = ["成交時間"])

data.groupby("類別ID")["銷量"].sum().reset_index()

data.groupby("類別ID")["銷量"].sum().reset_index().sort_values(by = "銷量",ascending = False).head(10)

pd.pivot_table(data,index = "商品ID",values = "銷量",
        aggfunc = "sum").reset_index().sort_values(by = "銷量",ascending = False).head(10)


data["銷售額"] = data["銷量"]*data["單價"]
data.groupby("門市編號")["銷售額"].sum()

data.groupby("門市編號")["銷售額"].sum()/data["銷售額"].sum()

#繪製圓形圖
import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"]='Microsoft JhengHei'

(data.groupby("門市編號")["銷售額"].sum()/data["銷售額"].sum()).plot.pie()

#利用自訂時間格式函式strftime提取小時數
data["小時"] = data["成交時間"].map(lambda x:int(x.strftime("%H")))

#對小時和訂單刪除重複
traffic = data[["小時","訂單ID"]].drop_duplicates()

#求每小時的客流量
traffic.groupby("小時")["訂單ID"].count()


#繪製每小時客流量折線圖
traffic.groupby("小時")["訂單ID"].count().plot()

## 假如你是某銀行的資料分析師

#匯入資料來源
data = pd.read_csv(r"C:\ACD019600\data\loan.csv")
data.info()

data = data.fillna({"月收入":data["月收入"].mean()})
data.info()

cut_bins=[0,5000,10000,15000,20000,100000]
income_cut=pd.cut(data["月收入"],cut_bins)
income_cut

all_income_user = data["好壞客戶"].groupby(income_cut).count()
bad_income_user = data["好壞客戶"].groupby(income_cut).sum()
bad_rate = bad_income_user/all_income_user
bad_rate 

#繪製月收入與壞帳率關係圖
bad_rate.plot.bar()

age_cut=pd.qcut(data["年齡"],6)
all_age_user = data["好壞客戶"].groupby(age_cut).count()
bad_age_user = data["好壞客戶"].groupby(age_cut).sum()
bad_rate = bad_age_user/all_age_user
bad_rate

#繪製年齡與壞帳率關係圖
bad_rate.plot.bar()

all_age_user = data.groupby("眷屬數量")["好壞客戶"].count()
bad_age_user = data.groupby("眷屬數量")["好壞客戶"].sum()
bad_rate = bad_age_user/all_age_user
bad_rate

#繪製眷屬數量與壞帳率關係圖
bad_rate. plot()