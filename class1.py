# class1.py
#1) 클래스를 정의
class Person:
    # 생성자(초기화) 메서드
    def __init__(self):
        self.name = "default name"
    def print(self):
        print("My name is {0}".format(self.name))


#2) 인스턴스 생성
p1 = Person()
p2 = Person()
#3) 메서드 호출
p1.print()
p2.name = "전우치"
p2.print()

#런타임시에 변수 추가 
Person.title = "new title"
print(p1.title)   #p1에 없다 하지만 위로 person 가서 찾는다 에러 안난다  
print(p2.title)
print(Person.title)

