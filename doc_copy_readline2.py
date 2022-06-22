#정규표현식 사용 
import re 

#원본 로그파일
f=open('c:\\work\\PV3.txt','rt')
#복사본 
g=open('c:\\work\\PV3_copy.txt','wt',encoding='utf-8') #깨지면 utf-8로 인코딩할께 

#많은 라인의 파일이면 
#한번에 한줄씩 읽어서 처리한다.  
#파일의 EOF(End Of File)이 아니면 계속 읽도록 한다. 
line = f.readline()
while (line != ''):    # != ' ' 파일의 끝부분을 찾는다 끝까지 도달하면 빠져나옴
    if (re.search("error", line)):  # 숫자가 연속으로 4자리 보여있으면 
        g.write(line + "\n")         #참이면 쓰기와 줄바꾸기 
    line = f.readline()               

f.close() 
g.close()








