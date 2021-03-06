# db1.py
import sqlite3

#연결객체를 리턴받기(일단은 메모리에서 연습)
con = sqlite3.connect(":memory:")  #"memory" 예약되어있는 단어 메모리에서 수행해 
#커서객체를 리턴받기
cur = con.cursor()
#테이블(스키마)를 생성
cur.execute("create table PhoneBook (Name text, PhoneNum text);")
#1건 입력
cur.execute("insert into PhoneBook values('derick', '010-222');")# 밖이 ""이면 안에는 ''

#입력파라메터 처리 
name = "gildong"
phoneNumber = "010-123"
cur.execute("insert into PhoneBook values (?, ?);", (name, phoneNumber))

#여러건을 입력 
datalist = (("tom","010-123"), ("dsp","010-456"))
cur.executemany("insert into PhoneBook values (?, ?);", (datalist))

#검색
cur.execute("select * from PhoneBook;")  

# 검색메서드 사용 
print("---fetchone()---")
print(cur.fetchone())    # 한건 가져와 임시메모리에 가져오고 삭제 
print("---fetchmany(2)---")
print(cur.fetchmany(2)) #두건 
print("---fetchone()---")
cur.execute("select * from PhoneBook;") #다시 검색하면 재생성됨 >마지막 다나옴 
print(cur.fetchall())   #나머지 다가져와  
# for row in cur:
#     print(row[0]+ " , "+ row[1]) #여러개면 무조건 튜플로 나옴 