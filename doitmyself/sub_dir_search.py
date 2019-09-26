# 1. 파이썬 파일만 출력
import os

def search(dirname):
    filenames = os.listdir(dirname)
    for filename in filenames:
        full_filename = os.path.join(dirname, filename)
        ext = os.path.splitext(full_filename)[-1] # 파이썬 파일만 출력
        if ext =='.py': # 파이썬 파일만 출력
            print(full_filename)

search("C:/")

# 2. C: 디렉터리 바로 밑에 있는 파일 뿐만 아니라 그 하위 디렉터리(sub_directory)를 포함한 모든 파이썬 파일을 검색

import os

def search(dirname):
    try:
        filenames = os.listdir(dirname)
        for filename in filenames:
            full_filename = os.path.join(dirname, filename)
            if os.path.isdir(full_filename):
                search(full_filename)
            else:
                ext = os.path.splitext(full_filename)[-1] # 파이썬 파일만 출력
                if ext =='.py': # 파이썬 파일만 출력
                    print(full_filename)
    except PermissionError:
        pass

search("C:/")
