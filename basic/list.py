# 파이썬 연습 - 리스트 자료형
odd=[1,3,5,7,9,['a','b','c']]
print(odd)
print(odd[2]+odd[3])
print(odd[5])
print(odd[5][1])

# 삼중 리스트 인덱싱
sam=[1,2,['a','b',['Xhaka','chambers']]]
print(sam[2][2][1])

print("\n리스트의 수정과 삭제")
a=[1,2,3,4,5,6]
print(a[2])
print(a[1:3])

del a[1]
print(a)

a[4:5] = []
print(a)

a.append(2)
print(a)

a.sort()
print(a)
a.reverse()
print(a)

a.insert(0,7)
print(a)
a.remove(3)
print(a)
print(a.pop())
print(a)
print(a.count(4))





