# 파이썬연습 -딕셔너리

# {Key1:Value1,Key2:Value2,...}
# dic = {'name':'shin','phone':'01012348808','birth':'0312'}

a= { 1: 'hi'}

# a={'a':[1,2,3]}
# 딕셔너리 쌍 추가하기

a[2]='b'
a['name']='pey'
a[3]=[1,2,3]
print(a)

# 딕셔너리 요소 삭제하기
del a[1]

print(a)

grade ={'shin': 30, 'june': 24}
print(grade['shin'])

dic = {'name':'shin','phone':'01012348808','birth':'0312'}
print(dic['phone'])
print(dic.keys())
for k in dic.keys():
    print(k)

print(list(dic.keys()))

print(dic.values())


