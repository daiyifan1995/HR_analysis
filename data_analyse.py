import open_dataset

import pandas as pd
import numpy as np
import math
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
import pydotplus
from sklearn.externals.six import StringIO
from IPython.display import Image
from sklearn import tree
import graphviz



#                                                data analyse
filename="cleaning20190326_index.csv"
df=pd.read_csv(filename)
pd.options.display.max_rows=999
pd.options.display.max_columns=999
df.count()#检查各列的数据
df=df.reindex(np.random.permutation(df.index))#重新排序
train_max_row = math.floor(df.shape[0]*0.8) #去尾去小数点，df.shape返回df的长宽
train_data= df.iloc[:int(train_max_row)]#训练集与测试集8：2
test_data=df.iloc[int(train_max_row):]

#Attrition
target=train_data.pop("Attrition") #删除Attrition并返回

clf = DecisionTreeClassifier(min_impurity_split=0.2)
clf.fit(train_data,target)
nameList=train_data.columns.values.tolist()



dot_data=tree.export_graphviz(clf,
                filled=True, rounded=True,
                special_characters=True,feature_names=nameList)
graph = graphviz.Source(dot_data)
graph.render("test.gv",view=True)

test_target=test_data.pop("Attrition")

print("Decision Tree score: %f"%(clf.score(test_data,test_target)))

