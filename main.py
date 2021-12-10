import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
pd.set_option('mode.chained_assignment',  None)

#폰트 지정-한글 폰트 깨지지 않기 위함
plt.rcParams['font.family'] = 'D2Coding'

#csv파일 불러오기 및 필터링
accident = pd.read_csv("data//accident.csv", encoding = 'cp949')
# accident=pd.pivot_table(accident,index=['차종','종류'])

#바이크와 승용차를 두개의 데이터 프레임으로 쪼갬
# bike=accident.xs('bike',level=0,axis=0)
# car=accident.xs('car',level=0,axis=0)

ax = plt.gca()
accident['사고율']=accident['사고건수']/accident['등록대수']
# bike['사고율']=bike['사고건수']/bike['등록대수']
# car['사고율']=car['사고건수']/car['등록대수']
accident4graph=accident.drop(['사망자수','중상자수','경상자수','부상신고자수','등록대수','사고건수'],axis=1)
print(accident4graph)
accident_pivot=accident4graph.pivot(index='종류',columns='차종',values='사고율')
accident_pivot.plot.bar(rot=0)
print("===================================")
print(accident_pivot)
# print(bike)
# print(car)
print(accident.dtypes)
# x=np.array(range(len(accident)))
# w=0.3
# accident.plot.bar(x,accident.loc[:,'사고건수'],width=w,label='바이크')
# plt.bar(x+w,accident.loc[:,'사고율'],width=w,label='승용차')
# plt.xticks(range(2),accident.index)
# plt.legend(loc=5)
# bike.reset_index().plot(kind='bar', x="종류", y='사고율',label='바이크',ax=ax,rot=0)
# car.reset_index().plot(kind='bar', x="종류", y='사고율',label='승용차',color='red',ax=ax,rot=0)


plt.show()


