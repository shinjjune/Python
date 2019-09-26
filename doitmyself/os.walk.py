# os.walk 를 이용하면 위에서 작성한 코드를 보다 간편하게 만들 수 있다. os.walk는 시작 디렉터리부터 시작하여 그 하위의 모든 디렉터리를 차례대로 방문하게 해주는 함수이다.

import os

for(path, dir, files) in os.walk("C:/"):
    for filename in files:
        ext = os.path.splitext(filename)[-1]
        if ext == '.py':
            print("%s/%s" %(path, filename))
