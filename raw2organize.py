import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
pd.set_option('mode.chained_assignment',  None)

#폰트 지정-한글 폰트 깨지지 않기 위함
plt.rcParams['font.family'] = 'D2Coding'

#csv파일 불러오기 및 필터링
accident = pd.read_csv("data//도로교통공단_가해운전자 차종별 피해운전자 차종별 교통사고 통계_20201231.csv", encoding = 'cp949')

#가해차종이 이륜차, 승용차가 아니면 drop 후 하나로 합침
accidentcar=accident[(accident.가해당사자종=='승용차')].drop('피해당사자종',axis=1)
inflictaccidentcar=pd.DataFrame({'차종':['승용차'],'종류':['피해'],'사고건수':[accidentcar['사고건수'].sum()],'사망자수':[accidentcar['사망자수'].sum()],'중상자수':[accidentcar['중상자수'].sum()],'경상자수':[accidentcar['경상자수'].sum()]})

accidentbike=accident[(accident.가해당사자종=='이륜차')].drop('피해당사자종',axis=1)
inflictaccidentbike=pd.DataFrame({'차종':['이륜차'],'종류':['피해'],'사고건수':[accidentbike['사고건수'].sum()],'사망자수':[accidentbike['사망자수'].sum()],'중상자수':[accidentbike['중상자수'].sum()],'경상자수':[accidentbike['경상자수'].sum()]})

inflictaccident=pd.concat([inflictaccidentbike,inflictaccidentcar], ignore_index=True)
#피해차종 이하동문
accidentcar=accident[(accident.피해당사자종=='승용차')].drop('가해당사자종',axis=1)
damageaccidentcar=pd.DataFrame({'차종':['승용차'],'종류':['피해'],'사고건수':[accidentcar['사고건수'].sum()],'사망자수':[accidentcar['사망자수'].sum()],'중상자수':[accidentcar['중상자수'].sum()],'경상자수':[accidentcar['경상자수'].sum()]})

accidentbike=accident[(accident.피해당사자종=='이륜차')].drop('피해당사자종',axis=1)
damageaccidentbike=pd.DataFrame({'차종':['이륜차'],'종류':['가해'],'사고건수':[accidentbike['사고건수'].sum()],'사망자수':[accidentbike['사망자수'].sum()],'중상자수':[accidentbike['중상자수'].sum()],'경상자수':[accidentbike['경상자수'].sum()]})

damageaccident=pd.concat([damageaccidentbike,damageaccidentcar], ignore_index=True)

organizedAccident=pd.concat([inflictaccident,damageaccident], ignore_index=True)


print(accident)
print(accidentcar)
print(accidentbike)
print(inflictaccident)
print(damageaccident)
print(organizedAccident)