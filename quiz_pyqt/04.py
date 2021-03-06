#pyqt 창 띄우기, 기본 요소

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        #창크기 조절
        self.setFixedSize(200, 300)
        #창제목 설정
        self.setWindowTitle('GA Mario')

        self.label = QLabel(self)
        self.label.setGeometry(100, 100, 100, 100)
        #창 띄우기
        self.show()


    def keyPressEvent(self, event):
        key = event.key()
        self.label.setText(str(key) + 'press')


    def keyReleaseEvent(self, event):
        key = event.key()
        print(str(key) + 'release')

#직접 실행할때만 실행되는 코드
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    sys.exit(app.exec_())