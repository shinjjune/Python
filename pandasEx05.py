import pandas as pd

# csv 파일 읽기
# pandas 에 read_csv() 를 사용하면 DataFrame 으로 값을 가져옴

print("----- 행 인덱스가 없는 csv 파일 읽기 ------")
csv_data1=pd.read_csv('sample1.csv', sep=",", dtype='unicode')
# 행 인덱스는 지정하지 앟ㄴ으면 자동으로 부여 0~정수로
print(csv_data1)
# ---------------------------------------------------------
csv_data1=pd.read_csv('sample1.csv',index_col='c1')
print(csv_data1)


print("----- 열 인덱스가 없는 csv 파일 읽기-------")
csv_data2=pd.read_csv('sample2.csv', names=['c1','c2','c3'])
print(csv_data2)


print('----- 구분자가 다른 csv  파일 읽기 -------')
csv_data3=pd.read_csv('sample3.csv',sep='\s+')
print(csv_data3)

print('----- 읽을 때 행 스킵이 필요한 경우 -------')
csv_data4=pd.read_csv('sample4.csv',skiprows=[0,1])
print(csv_data4)

# ----------------------------------------------------
csv_data5=pd.read_csv('sample5.csv',na_values=['누락',' '])
print(csv_data5)

print('--------- 웹 csv 파일 읽기 --------------')
titanic_csv=pd.read_csv('http://web.stanford.edu/class/archive/cs/cs109/cs109.1166/stuff/titanic.csv')
print(titanic_csv)
print(titanic_csv.head())
print(titanic_csv.tail(8))









