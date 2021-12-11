import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
pd.set_option('mode.chained_assignment',  None)

#폰트 지정-한글 폰트 깨지지 않기 위함
plt.rcParams['font.family'] = 'D2Coding'

#csv파일 불러오기 및 필터링
accident = pd.read_csv("data//도로교통공단_가해운전자 차종별 피해운전자 차종별 교통사고 통계_20201231.csv", encoding = 'cp949')
bikeresist=pd.read_csv("data//이륜차신고현황_연도별_20211210003715.csv", encoding = 'cp949')
carresisttemp=pd.read_csv("data//자동차등록대수현황_연도별_20211205232951.csv", encoding = 'cp949')

#가해차종이 이륜차, 승용차가 아니면 drop 후 하나로 합침
accidentcar=accident[(accident.가해당사자종=='승용차')].drop('가해당사자종',axis=1)
inflictaccidentcar=pd.DataFrame({'차종':['승용차'],'종류':['가해'],'사고건수':[accidentcar['사고건수'].sum()],'사망자수':[accidentcar['사망자수'].sum()],'중상자수':[accidentcar['중상자수'].sum()],'경상자수':[accidentcar['경상자수'].sum()]})
accidentbike=accident[(accident.가해당사자종=='이륜차')].drop('가해당사자종',axis=1)
inflictaccidentbike=pd.DataFrame({'차종':['이륜차'],'종류':['가해'],'사고건수':[accidentbike['사고건수'].sum()],'사망자수':[accidentbike['사망자수'].sum()],'중상자수':[accidentbike['중상자수'].sum()],'경상자수':[accidentbike['경상자수'].sum()]})
inflictaccident=pd.concat([inflictaccidentbike,inflictaccidentcar], ignore_index=True)

#피해차종 이하동문
accidentcar=accident[(accident.피해당사자종=='승용차')].drop('피해당사자종',axis=1)
damageaccidentcar=pd.DataFrame({'차종':['승용차'],'종류':['피해'],'사고건수':[accidentcar['사고건수'].sum()],'사망자수':[accidentcar['사망자수'].sum()],'중상자수':[accidentcar['중상자수'].sum()],'경상자수':[accidentcar['경상자수'].sum()]})
accidentbike=accident[(accident.피해당사자종=='이륜차')].drop('피해당사자종',axis=1)
damageaccidentbike=pd.DataFrame({'차종':['이륜차'],'종류':['피해'],'사고건수':[accidentbike['사고건수'].sum()],'사망자수':[accidentbike['사망자수'].sum()],'중상자수':[accidentbike['중상자수'].sum()],'경상자수':[accidentbike['경상자수'].sum()]})
damageaccident=pd.concat([damageaccidentbike,damageaccidentcar], ignore_index=True)
#피해 및 가해 병합
organizedAccident=pd.concat([inflictaccident,damageaccident], ignore_index=True)
#이륜차 등록대수 현황 필터링
bikeresist=bikeresist[bikeresist.시점=='2020']
bikeresist['차종']='이륜차'
bikeresist.rename(columns = {'총합계' : '등록대수'}, inplace = True)
#승용차 등록대수 현황 필터링
carresisttemp=carresisttemp[carresisttemp['레벨01(1)']=='승용']
carresist=pd.DataFrame({'차종':['승용차'],'시점':[2020],'등록대수':[carresisttemp['2020.2'].sum()]})
#등록대수 병합
resist=pd.concat([carresist,bikeresist], ignore_index=True)
#등록대수 현황 dataframe과 사고 dataframe 병합
accidentAndResist=pd.merge(organizedAccident,resist)
accidentAndResist['등록대수']=pd.to_numeric(accidentAndResist['등록대수'])

print(accident)
print(inflictaccident)
print(damageaccident)
print(organizedAccident)
print('================')
print(resist)
print('================')
print(accidentAndResist)
print(accidentAndResist.dtypes)