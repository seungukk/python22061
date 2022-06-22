# DemoRandom.py
import random

print(random. random())
print(random. random())
print([random. randrange(20) for i in range(10)]) # 10번루프돌고 0부터 19까지 임의의 숫자 10개를 만들ㅇ 
print([random. randrange(20) for i in range(10)]) #중복이 있음 
print(random. sample(range(20),10))
print(random. sample(range(20),10)) # 0부터 19까지 10개만 샘플링 unqiue한것만 


print("--- 로또번호---")
lotto = list(range(1,46))  #1부터 45
print(lotto)
random.shuffle(lotto)   #shuffle로 순서 섞어 
print(lotto) #뒤섞은걸 출력해바 
for item in range(5):
    print(lotto.pop())


#파일과 폴더 다루기 
from os.path import *
print(abspath("python.exe"))
print(basename("c:\\python39\\python.exe"))
print(getsize("c:\\python39\\python.exe"))
print(exists("c:\\python39\\python.exe"))  #교재 293페이지 

#운영체제 정보 보기 
from os import *
print(getcwd())
print(name)
# system("notepad.exe")

#파일, 폴더리스트 
import glob
result = glob. glob("c:\\work\\*.py")
print(result)