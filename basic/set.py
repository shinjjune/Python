# 파이썬 연습 - 집합 자료형

s1 =set([1,2,3])
print(s1)

s2 = set("Hello")
print(s2)

# set의 특징 1. 중복을 허용하지 않는다. 2. 순서가 없다

l1=list(s1)
print(l1)
t1=tuple(s1)
print(t1)


# 집합 자료형 활용하는 방법
s1= set([1,2,3,4,5,6])
s2= set([3,4,5,6,7,8])
# 1. 교집합 &
print(s1&s2)
print(s1.intersection(s2))
# 2. 합집합 |
print(s1|s2)
print(s1.union(s2))
# 3. 차집합 (-)
print(s1-s2)
print(s2.difference(s1))

# 집합 자료형 관련 함수
#  값 1개 추가하기(add)
s1.add(77)
print(s1)
# 값 여러 개 추가하기(update)
s1.update([99,88])
print(s1)
# 특정 값 제거하기(remove)
s1.remove(77)
print(s1)



# 자료형 숫자, 문자열, 리스트, 튜플, 딕셔너리, 집합에 대해서 알아보았다. 
# 자료형은 중요하고 프로그램의 근간이 되기 때문에 확실하게 해놓지 않으면 좋은 프로그램을 만들 수 없다.
