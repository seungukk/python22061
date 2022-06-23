# DemoForm.py
# DemoForm.ui(디자인) + DemoForm.py(로직)
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
#웹 크롤링
import urllib.request
from bs4 import BeautifulSoup

#디자인 파일 로딩
form_class = uic.loadUiType("DemoForm2.ui")[0]  

#폼 클래스 정의(QmainWindow)

class DemoForm(QMainWindow, form_class):    #디자인 + Demoform 둘다 상속받는다 
    #생성자 메서드
    def __init__(self):    #부모가 여러명이니 super로 뭉뚱그리면 양쪽을 불러줌. 
        super().__init__()
        self.setupUi(self)
        self.label.setText("첫번째 데모~~")
            # 슬롯 메서드 정의 
    def firstClick(self):
        #파일로 저장 
        f = open("c:\\work\\webtoon.txt", "wt", encoding="utf-8")
        #동적으로 주소 생성
        for i in range(1,6): 
            #웹페이지의 실행결과를 문자열로 받기 
            url = "https://comic.naver.com/webtoon/list?titleId=20853&weekday=fri&page=" + \
                str(i)
            print(url)
            data = urllib.request.urlopen(url)
            #검색을 할 객체 생성 
            soup = BeautifulSoup(data, "html.parser")
            cartoons = soup.find_all("td", class_="title")
            for item in cartoons:
                title = item.find("a").text 
                print(title.strip())
                f.write(title.strip() + "\n")
        f.close()
        self.label.setText("네이버 웹툰 크롤링 종료")
    def secountClick(self):
        self.label.setText("두번째 버튼클릭")    
    def thridClick(self):
        self.label.setText("세번째 버튼을 클릭~~")
#진입점 체크

if __name__ == "__main__":       # __name__  원래 씨언어는 main부터 시작하는데 Demoform 모듈에서 __main__ 기본세팅값같은 진입점 역할을 해서 나부터 시작 >> 쿠키틀로 쿠키찍어내는 
    #실행프로세스 
    app = QApplication(sys.argv)
    #창을 실행
    demoWindow = DemoForm()
    demoWindow.show()
    #이벤트 처리 대기 
    app.exec_()