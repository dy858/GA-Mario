#pyqt 그리기

import sys
from PyQt5.QtGui import QPainter, QPen, QBrush, QColor
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        #창크기 조절
        self.setFixedSize(200, 300)
        #창제목 설정
        self.setWindowTitle('GA Mario')
        #창 띄우기
        self.show()

    #창이 업데이트 될 때마다 실행되는 함수
    def paintEvent(self, event):
        #그리기 도구
        painter = QPainter()
        #그리기 시작
        painter.begin(self)

        #펜 설정(테두리)
        painter.setPen(QPen(Qt.blue, 2.0, Qt.SolidLine))  #색 두께 종류

        #선 그리기
        painter.drawLine(0, 10, 200, 100) #(시작점) (끝점)

        #RGB 설정으로 펜 설정
        painter.setPen(QPen(QColor.fromRgb(255, 0, 0), Qt.SolidLine))

        #브러쉬 설정(채우기)
        painter.setBrush(QBrush(Qt.blue))

        #직사각형 그리기
        painter.drawRect(0, 100, 100, 100) # 시작점 너비 높이

        painter.setPen(QPen(Qt.black, 1.0, Qt.SolidLine))
        painter.setBrush(QBrush(QColor.fromRgb(0, 255, 0)))
        #타원 그리기
        painter.drawEllipse(100, 100, 100, 100) #왼쪽 윗점 가로변의 지름 세로변의 지름

        painter.setPen(QPen(Qt.cyan, 1.0, Qt.SolidLine))
        painter.setBrush(Qt.NoBrush) #브러쉬 초기화(더이상 색으 채우지 않음)
        #텍스트 그리기
        painter.drawText(0, 250, 'ABCD')

        #그리기 끝
        painter.end()



#직접 실행할때만 실행되는 코드
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    sys.exit(app.exec_())

