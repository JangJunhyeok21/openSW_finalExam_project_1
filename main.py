import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
pd.set_option('mode.chained_assignment',  None)

#폰트 지정-한글 폰트 깨지지 않기 위함
plt.rcParams['font.family'] = 'D2Coding'

#csv파일 불러오기 및 필터링
accident = pd.read_csv("data//accident.csv", encoding = 'cp949')
accident['사고율']=accident['사고건수']/accident['등록대수']
accident['사망률']=accident['사망자수']/accident['사고건수']
accident4graph=accident.drop(['사망자수','중상자수','경상자수','부상신고자수','등록대수','사고건수'],axis=1)
print(accident4graph)
accident_pivot=accident4graph.pivot(index='종류',columns='차종',values=['사고율','사망률'])
accident_pivot.plot.bar(rot=0)
print("===================================")
print(accident)

plt.show()