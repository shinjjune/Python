# class 란?

"틀"

```
class 클래스이름[(상속 클래스명)]:
  <클래스 변수1>
  <클래스 변수2>
  ...
  <클래스 변수N>
  def 클래스 함수1(self[,인수1, 인수2,,,]):
  <수행할 문장1>
  <수행할 문장2>
  ...
  def 클래스 함수2(self[,인수1, 인수2,,,]):
  <수행할 문장1>
  <수행할 문장2>
  ...
  def 클래스 함수N(self[,인수1, 인수2,,,]):
  <수행할 문장1>
  <수행할 문장2>
  ...
...
```

# module?

모듈이란 함수나 변수 또는 클래스들을 모아 놓은 파일이다.
모듈은 다름 파이썬 프로그램에서 불러와 사용할 수 있겠끔 만들어진 파이썬 파일

import 모듈이름

```
from 모듈이름 import 모듈함수
```

# package

패키지는 도트(.)를 이용하여 파이썬 모듈을 계층적(디렉터리 구조)으로 관리할 수 있게 해준다.
예를 들어 모듈명이 A.B인 경우 A는 패키지명이 되고 B는 A패키지의 B모듈이 된다.

```
game/
  __init__.py
  sound/
    __init__.py
    echo.py
    wav.py
  graphic/
    __init__.py
    screen.py
    render.py
  play/
    __init__.py
    run.py
    test.py
```

#### 패키지 안의 함수 실행하기 

1. echo 모듈을 import 하여 실행하는 방법
```
>>>import game.sound.echo
>>>game.sound.echo.echo_test()
echo
```
2. echo 모듈이 있는 디렉터림까지를 from...import 하여 실행하는 방법
```
>>>from game.sound import echo
>>>echo.echo_test()
echo
```
3. echo 모듈의 echo_test 함수를 직접 import 하여 실행하는 방법
```
>>>from game.sound.echo import echo_test
>>>echo_test()
echo
```
```
* __init__.py 의 용도
  해당 디렉터리가 패키지의 일부임을 알려주는 역할을 한다.--> "패키지로 인식"
  만약 디렉터리에__init__.py 파일이 없으면 importError가 발생하게된다.
```
