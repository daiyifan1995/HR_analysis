import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#使用直方图的方法进行变量离散化
def discretizationByHist(df,attr,num_bins,interval):
    # ___________________________DailyRate
    # x = df[attr].to_numpy().tolist()
    # mu = np.mean(x)
    # sigma = np.sqrt(np.var(x))
    #
    # fig, ax = plt.subplots()
    # # the histogram of the data
    # n, bins, patches = ax.hist(x, num_bins, density=1)
    #
    # # add a 'best fit' line
    # y = ((1 / (np.sqrt(2 * np.pi) * sigma)) *
    #      np.exp(-0.5 * (1 / sigma * (bins - mu)) ** 2))
    #
    # ax.plot(bins, y, '--')
    # ax.set_xlabel(attr)
    # ax.set_ylabel('Probability density')
    # ax.set_title(r'%s Hist:mu(%f),sigma(%f)' % (attr,mu, sigma))
    #
    # # Tweak spacing to prevent clipping of ylabel
    # fig.tight_layout()
    # plt.show()

    # 将连续性变量转为非连续变量，离散化
    #print(df[attr].min(),df[attr].max())
    bins_list=[df[attr].min()+interval*i for i in range(0,num_bins+1)]

    df[attr] = pd.cut(df[attr].to_numpy(), bins_list, include_lowest=True)

    #print(df[attr].value_counts())



    return df

#自定义,一般使用等频
def discretizationByUserDedined(df,attr,num_list):

    # 将连续性变量转为非连续变量，离散化
    #print(df[attr].min(),df[attr].max())

    df[attr] = pd.cut(df[attr].to_numpy(), num_list, include_lowest=True)
    #print(df[attr].value_counts())



    return df

def valuetoindex(df,attr):
    j = 0
    for i in df[attr].value_counts().keys():
        df[attr].replace(i, j, inplace=True)
        j = j + 1
        print(i)

    return df
