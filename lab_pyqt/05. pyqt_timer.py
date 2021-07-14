#pyqt 창 띄우기, 기본 요소

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import QTimer

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        #창크기 조절
        self.setFixedSize(400, 300)
        #창제목 설정
        self.setWindowTitle('GA Mario')
        #타이머 생성
        self.qtimer = QTimer(self)
        #타이머에 호출할 함수 연결
        self.qtimer.timeout.connect(self.timer)
        #1초마다 연결된 함수를 실행
        self.qtimer.start(1000) #밀리세컨드 단위



        #창 띄우기
        self.show()


    def timer(self):
        print('timer')

#직접 실행할때만 실행되는 코드
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    sys.exit(app.exec_())