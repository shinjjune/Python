## 메타 문자(meta characters)

```
.^$*+?{}[]\|()
```

* 문자클래스 []
```
EX) [abc] a => 매치  
    [abc] before => 매치  
    [abc] dude => 매치x
    
    [0-5]  ==  [012345]
    [a-zA-Z]: 알파벳 모두
    [0-9]: 숫자
```

* Dot(.)
```
EX) a.b aab => 매치
        a0b => 매치
        abc => 매치x "abc"는 "a"문자와 "b"문자 사이에 어떤 문자라도 하나는 있어야 하는 이정규식과 일치하지 않음
```

* 반복(*)
```
EX) ca*t ct => 매치
         cat => 매치
         caaaat => 매치
```

* 반복(+)
```
EX) ca+t ct => 매치x  "ca+t"는 "a"가 한번이상 반복되어야한다.
         cat => 매치
         caaat => 매치
```

* 반복({m,n},?)
: 반복회수를 제한할 때 사용
```
ca{2}t : a가 2번 박복되면 매치  caat => 매치
ca{2,5}t :a가 2~5번 반복되면 매치 caaat => 매치
                                 caaaaat => 매치
ab?c : b가 0~1 번사용되면 매치 abc => 매치
                              ac => 매치
```



## 파이썬에서 정규 표현식을 지원하는 re모듈
파이썬은 정규표현식을 지원하기 위해 re(regular expression) 모듈을 제공한다. re 모듈은 파이썬이 설치될 때 자동으로 설치되는 기본 라이브러리로,
사용방법은 다음과 같다.
```
>import re
>p = re.compile('ab*')
```
re.compile을 이용하여 정규 표현식(위 예에서는 ab*)을 컴파일한다. re.compile의 결과로 리턴되는 객체 p(컴파일된 패턴 객체)를 이용하여 그 이후의 작업을 수행할 것이다.

#### 정규식을 이용한 문자열 검색

* match()    : 문자열의 처음부터 정규식과 매치되는지 조사한다.
* search()   : 문자열 전체를 검색하여 정규식과 매치되는지 조사한다.
* findall()  : 정규식과 매치되는 모든 문자열(substring)을 리스트로 리턴한다.
* finditer() : 정규식과 매치되는 모든 문자열(substring)을 반복 가능한 객체로 리턴한다.

```
>import re
>p=re.compile('[a-z]+')
```
##### match
```
>m=p.match("python")
>print(m)
<re.Match object; span=(0, 6), match='python'>

>m=p.match("3 python")
>print(m)
None

# 종합
import re
p=re.compile('[a-z]+')
m=p.match("python")
if m:
    print('Match Found: ', m.group())
else:
    print('No match')

```
##### search

```
>m= p.search("python")
>print(m)
<re.Match object; span=(0, 6), match='python'>

>m= p.search("3 python")
>print(m)
<re.Match object; span=(2, 8), match='python'>
```
##### findall
```
>result=p.findall("life is too short")
>print(result)
['life', 'is', 'too', 'short']
```
##### finditer
```
>result=p.finditer("life is too short")
>print(result)
<callable_iterator object at 0x0000000002797EC8>

>for r in result: print(r)
<re.Match object; span=(0, 4), match='life'>
<re.Match object; span=(5, 7), match='is'>
<re.Match object; span=(8, 11), match='too'>
<re.Match object; span=(12, 17), match='short'>
```












