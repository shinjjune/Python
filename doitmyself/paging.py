# 총 페이지수 = 총 건수 / 한 페이지당 보여줄 건수 +1

def getTotalPage(m,n):
    if m%n==0:
        return m//n
    else:
        return m//n+1

print(getTotalPage(5,10))
print(getTotalPage(15,10))
print(getTotalPage(25,10))
print(getTotalPage(30,10))

