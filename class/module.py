# module_prac.py

import mod1
print(mod1.safe_sum(3,'a'))
print(mod1.sum(10,20))

import mod2
result = mod2.sum(3,4)
print(result)

# mod1.py
def sum(a,b):
    return a+b

def safe_sum(a,b):
    if type(a) != type(b):
        print("더할수 있는 것이 아닙니다.")
        return
    else:
        result = sum(a,b)
    return result

if __name__ == "__main__":
    print(safe_sum('a',1))
    print(safe_sum(1,4))
    print(sum(10,10.4))

# mod2.py
PI = 3.141592
class Math:
    def solv(self, r):
        return PI*(r**2)
def sum(a,b):
    return a+b


if __name__=="__main__":
     print(PI)
     a = Math()
     print(a.solv(2))
     print(sum(PI,4.4))
