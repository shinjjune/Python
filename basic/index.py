# 파이썬 연습입니다.
print("hello world\njava")

multiline='''
    python
    java
    ruby
'''
print(multiline)

# 문자열 연산
head="lacazette  "
tail="aubameyang"

print(head+tail)
print(head*2)

print("="*50)
print(tail)
print("="*44)

# 문자열 인덱싱과 슬라이싱
a="Life is too short, My job is developer"
print(a[3:6])
print(a[19:])

# 문자열 포맷팅
b="I eat %d apples." %3
print(b)

c="I have %s point" % "five"
print(c)

num=4
numb="nine"
k="I have %s apples, and %d oranges" %(numb, num)
print(k)

d="% -10sshe" % "hi"
print(d)

# 문자열 관련 함수들
ac="account"
print(ac.count('c'))
