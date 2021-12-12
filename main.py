from raw2organize import *

#필요없는 데이터 삭제 및 피봇
accident4graph=accidentAndResist.drop(['사망자수','중상자수','등록대수','사고건수'],axis=1)
accident_pivot=accident4graph.pivot(index='종류',columns='차종',values=['사고율(%)','사망률(%)'])
#총합 중상률 데이터 비교
accidenthurt=accident4graph[accident4graph.종류=='총합']

accident_pivot.plot.bar(rot=0)
plt.title("차종별 유형별 사고데이터 분석")
plt.xlabel('사고 분류')
plt.legend()
accidenthurt.plot(kind='bar',x='차종',secondary_y='중상률(%)',rot=0)
plt.title("피해•가해 총합 데이터")
plt.xlabel('사고 차종')

#'이륜차는 승용차보다 안전하거나 같다'는 명제가 성립하기 위해서
accidentAndResist_list=accidentAndResist.values.tolist()
bikeresistNum=accidentAndResist_list[5][5] #이륜차 등록대수
bikeaccidentNum=accidentAndResist_list[5][2] #이륜차 사고건수
caraccidentrate=accidentAndResist_list[2][6] #승용차 사고율
leastnonresistbike=(bikeaccidentNum/(caraccidentrate/100))-bikeresistNum #(바이크 사고건수 / (승용차 사고율(%) * 100))-바이크 등록대수=무등록 이륜차

print(accidentAndResist)
print("===================================")
print(f'만약 이륜차가 승용차와 비슷하거나 더 안전하기 위해서는 최소 {leastnonresistbike}대의 무등록 이륜차가 있어야 한다.')

# plt.show()