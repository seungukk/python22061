# DemoForm.py
# DemoForm.ui(디자인) + DemoForm.py(로직)
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic


#디자인 파일 로딩
form_class = uic.loadUiType("DemoForm.ui")[0]  

#폼 클래스 정의

class DemoForm(QDialog, form_class):    #디자인 + Demoform 둘다 상속받는다 
    #생성자 메서드
    def __init__(self):    #부모가 여러명이니 super로 뭉뚱그리면 양쪽을 불러줌. 
        super().__init__()
        self.setupUi(self)
        self.label.setText("첫번째 데모~~")

#진입점 체크

if __name__ == "__main__":       # __name__  원래 씨언어는 main부터 시작하는데 Demoform 모듈에서 __main__ 기본세팅값같은 진입점 역할을 해서 나부터 시작 >> 쿠키틀로 쿠키찍어내는 
    #실행프로세스 
    app = QApplication(sys.argv)
    #창을 실행
    demoWindow = DemoForm()
    demoWindow.show()
    #이벤트 처리 대기 
    app.exec_()