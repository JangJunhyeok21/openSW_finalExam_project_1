import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
pd.set_option('mode.chained_assignment',  None)
pd.set_option('display.max_columns', None)

#폰트 지정-한글 폰트 깨지지 않기 위함
plt.rcParams['font.family'] = 'D2Coding'

#csv파일 불러오기 및 필터링
accident = pd.read_csv("data//도로교통공단_가해운전자 차종별 피해운전자 차종별 교통사고 통계_20201231.csv", encoding = 'cp949')
bikeresist=pd.read_csv("data//이륜차신고현황_연도별_20211210003715.csv", encoding = 'cp949')
carresisttemp=pd.read_csv("data//자동차등록대수현황_연도별_20211205232951.csv", encoding = 'cp949')

#승용차 가해피해 필터링
accidentcar=accident[(accident.가해당사자종=='승용차')].drop('피해당사자종',axis=1)
inflictaccidentcar=pd.DataFrame({'차종':['승용차'],'종류':['가해'],'사고건수':[accidentcar['사고건수'].sum()],'사망자수':[accidentcar['사망자수'].sum()],'중상자수':[accidentcar['중상자수'].sum()],'경상자수':[accidentcar['경상자수'].sum()]})
accidentcar=accident[(accident.피해당사자종=='승용차')].drop('가해당사자종',axis=1)
damageaccidentcar=pd.DataFrame({'차종':['승용차'],'종류':['피해'],'사고건수':[accidentcar['사고건수'].sum()],'사망자수':[accidentcar['사망자수'].sum()],'중상자수':[accidentcar['중상자수'].sum()],'경상자수':[accidentcar['경상자수'].sum()]})
caraccident=pd.concat([inflictaccidentcar,damageaccidentcar], ignore_index=True)
#피해가해 총합 데이터 추가
totalcar = pd.DataFrame({'차종':['승용차'],'종류':['총합'],'사고건수':[caraccident['사고건수'].sum()],'사망자수':[caraccident['사망자수'].sum()],'중상자수':[caraccident['중상자수'].sum()],'경상자수':[caraccident['경상자수'].sum()]})
caraccident = caraccident.append(totalcar, ignore_index = True)

#이륜차 가해피해 필터링
accidentbike=accident[(accident.가해당사자종=='이륜차')].drop('피해당사자종',axis=1)
inflictaccidentbike=pd.DataFrame({'차종':['이륜차'],'종류':['가해'],'사고건수':[accidentbike['사고건수'].sum()],'사망자수':[accidentbike['사망자수'].sum()],'중상자수':[accidentbike['중상자수'].sum()],'경상자수':[accidentbike['경상자수'].sum()]})
accidentbike=accident[(accident.피해당사자종=='이륜차')].drop('가해당사자종',axis=1)
damageaccidentbike=pd.DataFrame({'차종':['이륜차'],'종류':['피해'],'사고건수':[accidentbike['사고건수'].sum()],'사망자수':[accidentbike['사망자수'].sum()],'중상자수':[accidentbike['중상자수'].sum()],'경상자수':[accidentbike['경상자수'].sum()]})
bikeaccident=pd.concat([inflictaccidentbike,damageaccidentbike], ignore_index=True)
#피해가해 총합 데이터 추가
totalbike = pd.DataFrame({'차종':['이륜차'],'종류':['총합'],'사고건수':[bikeaccident['사고건수'].sum()],'사망자수':[bikeaccident['사망자수'].sum()],'중상자수':[bikeaccident['중상자수'].sum()],'경상자수':[bikeaccident['경상자수'].sum()]})
bikeaccident = bikeaccident.append(totalbike, ignore_index = True)
#피해 및 가해 병합
organizedAccident=pd.concat([caraccident,bikeaccident], ignore_index=True)

#이륜차 등록대수 현황 필터링
bikeresist=bikeresist[bikeresist.시점=='2020']
bikeresist['차종']='이륜차'
bikeresist.rename(columns = {'총합계' : '등록대수'}, inplace = True)
#승용차 등록대수 현황 필터링
carresisttemp=carresisttemp[carresisttemp['레벨01(1)']=='승용']
carresist=pd.DataFrame({'차종':['승용차'],'시점':[2020],'등록대수':[carresisttemp['2020.2'].sum()]})
#등록대수 병합
resist=pd.concat([carresist,bikeresist], ignore_index=True)

#등록대수 현황 dataframe과 사고 dataframe 병합, 문자열을 숫자로 자료형 변환
accidentAndResist=pd.merge(organizedAccident,resist)
accidentAndResist['등록대수']=pd.to_numeric(accidentAndResist['등록대수'])

#필요없는 컬럼 삭제
accidentAndResist=accidentAndResist.drop(['시점','경상자수'],axis=1)

#사고율, 사망률, 중상률 계산 및 추가
accidentAndResist['사고율(%)']=accidentAndResist['사고건수']/accidentAndResist['등록대수']*100
accidentAndResist['사망률(%)']=accidentAndResist['사망자수']/accidentAndResist['사고건수']*100
accidentAndResist['중상률(%)']=accidentAndResist['중상자수']/accidentAndResist['사고건수']*100

#'이륜차는 승용차보다 안전하거나 같다'는 명제가 성립하기 위해서
accidentAndResist_list=accidentAndResist.values.tolist()
bikeresistNum=accidentAndResist_list[5][5] #이륜차 등록대수
bikeaccidentNum=accidentAndResist_list[5][2] #이륜차 사고건수
caraccidentrate=accidentAndResist_list[2][6] #승용차 사고율
leastnonresistbike=(bikeaccidentNum/(caraccidentrate/100))-bikeresistNum #(바이크 사고건수 / (승용차 사고율(%) * 100))-바이크 등록대수=무등록 이륜차