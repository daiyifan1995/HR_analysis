import open_dataset
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import tree
import discretization


filename="WA_Fn-UseC_-HR-Employee-Attrition-rawdata.csv"

# #use csv to open csv
# dataset=open_dataset.readCsvToDictList(filename)
# print(open_dataset.readCsvGetTitle(filename))
# age_list=[]
# for i in dataset:
#     if "Age" in i.keys():
#         if i["Age"]!="":
#             age_list.append(int(i["Age"]))
# print(age_list)
# if len(age_list)!=0:
#     mean=np.mean(age_list)
#     var=np.var(age_list)
#     print(var,mean)

#use pandas to open csv to dataFrame
file=open(filename,encoding="utf-8")

#                       使数据尽可能显示完全
pd.options.display.max_rows=999
pd.options.display.max_columns=999

df=pd.read_csv(file)

#df.to_numpy  df.descrice() df.T

#print(df.describe())


#                                                    data cleaning and preprocessing
df = df.replace("NaN", np.nan)

#print(df.isna())#检查哪里有缺失值

#print(df.loc[df['Age']==18]) #查找df的“age”列等于18的行，return 为df
df=df.fillna(round(df["Age"].mean())) #使用均值来代替缺失值
colName=df.columns.values.tolist()
df.count()#检查各列的数据

#                                                  data visualtion，使用直方图确定数据离散化的bins，等宽或者等深

num_bins_Age=3
interval_age=14
df=discretization.discretizationByHist(df,"Age",num_bins_Age,interval_age)

num_bins_DailyRate=7
interval_DailyRate=200
df=discretization.discretizationByHist(df,"DailyRate",num_bins_DailyRate,interval_DailyRate)

num_bins_DistanceFromHome=4
interval_DistanceFromHome=7
df=discretization.discretizationByHist(df,"DistanceFromHome",num_bins_DistanceFromHome,interval_DistanceFromHome)

num_bins_EmployeeNumber=9
interval_EmployeeNumber=250
df=discretization.discretizationByHist(df,"EmployeeNumber",num_bins_EmployeeNumber,interval_EmployeeNumber)

num_bins_HourlyRate=3
interval_HourlyRate=24
df=discretization.discretizationByHist(df,"HourlyRate",num_bins_HourlyRate,interval_HourlyRate)

num_bins_MonthlyIncome=7
interval_MonthlyIncome=3000
df=discretization.discretizationByHist(df,"MonthlyIncome",num_bins_MonthlyIncome,interval_MonthlyIncome)

num_bins_MonthlyRate=5
interval_MonthlyRate=5000
df=discretization.discretizationByHist(df,"MonthlyRate",num_bins_MonthlyRate,interval_MonthlyRate)

# 有一些可能是不需要使用等距hist划分的/可以使用等频划分

interval_NumCompaniesWorked=[0,0.5,1.5,2,4,9]

df=discretization.discretizationByUserDedined(df,"NumCompaniesWorked",interval_NumCompaniesWorked)




num_bins_PercentSalaryHike=3
interval_PercentSalaryHike=5
df=discretization.discretizationByHist(df,"PercentSalaryHike",num_bins_PercentSalaryHike,interval_PercentSalaryHike)

num_bins_TotalWorkingYears=8
interval_TotalWorkingYears=5
df=discretization.discretizationByHist(df,"TotalWorkingYears",num_bins_TotalWorkingYears,interval_TotalWorkingYears)

interval_TrainingTimesLastYear=[0,1,2,3,6]

df=discretization.discretizationByUserDedined(df,"TrainingTimesLastYear",interval_TrainingTimesLastYear)


interval_YearsAtCompany=[0,2,5,10,40]

df=discretization.discretizationByUserDedined(df,"YearsAtCompany",interval_YearsAtCompany)



interval_YearsInCurrentRole=[0,1,2,6,8,18]
df=discretization.discretizationByUserDedined(df,"YearsInCurrentRole",interval_YearsInCurrentRole)



interval_YearsSinceLastPromotion=[0,0.5,1,2,15]
df=discretization.discretizationByUserDedined(df,"YearsSinceLastPromotion",interval_YearsSinceLastPromotion)


interval_YearsWithCurrManager=[0,1,2,5,7,17]
df=discretization.discretizationByUserDedined(df,"YearsWithCurrManager",interval_YearsWithCurrManager)


for i in colName:
    if len(df[i].value_counts().keys())==1:
        df = df.drop(i, axis=1)


df.to_csv("cleaning20190326.csv", encoding='utf-8')
file=open("cleaning20190326.csv",encoding="utf-8") #将字符，数值等信息转为index

df=pd.read_csv(file)
colName=df.columns.values.tolist()
for attr in colName:
    df=discretization.valuetoindex(df,attr)

df.to_csv("cleaning20190326_index.csv", encoding='utf-8')







