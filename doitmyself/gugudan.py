# easy gugudan


def GuGu(n):
    result = []
    result.append(n * 1)
    result.append(n * 2)
    result.append(n * 3)
    result.append(n * 4)
    result.append(n * 5)
    result.append(n * 6)
    result.append(n * 7)
    result.append(n * 8)
    result.append(n * 9)
    return result
print(GuGu(2))

# 정말 무식한 방법이지만 원하는 결과값을 얻을 수 있다.

# 효과적이다.
def GuGu(n):
    result = []
    i = 1
    while i <10:
        result.append(n*i)
        i = i +1
    return result

print(GuGu(2))
