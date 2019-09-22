# 오류 예외 처리 기법

try:
  4/0
except ZeroDivisionError as e:
  print(e)
# 결과값:division by zero

# try .. else
try:
  f=open('foo.txt','r')
except FileNotFoundError as e:
  print(str(e))
else:
  data = f.read()
  f.close()
# foo.txt 라는 파일이 없다면 except 절이 수행되고, foo.txt 파일이 있다면 else 절이 수행될 것이다.

# try .. finally
# try 문에 finally 절을 사용할 수 있다. finally절은 try 문 수행 도중 예외 발생 여부에 상관없이 항상 수행된다. 보통finally 절은 사용한 리소스를 close해야 할 경우에 많이 사용된다.

f = open('foo.txt','w')
try:
  # 무언가를 수행한다.
finally:
  f.close()

# 오류 회피하기
try:
  f=open("나없는파일",'r')
except FileNotFoundError:
  pass

# 오류 일부러 발생시키기, raise

class Bird:
    def fly(self):
        raise NotImplementedError

class Eagle(Bird):
    def fly(self):
        print("very fast")

eagle = Eagle()
eagle.fly()


