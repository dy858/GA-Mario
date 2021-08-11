import retro
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt
import numpy as np
from PyQt5.QtCore import QTimer






#print(screen.shape[0], screen.shape[1])
#print(screen)

class MyApp(QWidget):
    def __init__(self):
        super().__init__()


        self.press_buttons = [0, 0, 0, 0, 0, 0, 0, 0, 0]

        self.env = retro.make(game='SuperMarioBros-Nes', state='Level1-1')
        self.env.reset()

        self.screen = self.env.get_screen()

        #창크기 조절
        self.setFixedSize(int(self.screen.shape[0] * 2), int(2 * self.screen.shape[1]))
        #창제목 설정
        self.setWindowTitle('GA Mario')

        self.label_image = QLabel(self)

        self.image = self.env.get_screen()
        self.screen = self.env.get_screen()
        self.qimage = QImage(self.image, self.image.shape[1], self.image.shape[0], QImage.Format_RGB888)
        pixmap = QPixmap(self.qimage)
        pixmap = pixmap.scaled(int(self.screen.shape[0] * 2), int(2 * self.screen.shape[1]), Qt.IgnoreAspectRatio)

        self.label_image.setPixmap(pixmap)
        self.label_image.setGeometry(0, 0, int(self.screen.shape[0] * 2), int(2 * self.screen.shape[1]))

        self.qtimer = QTimer(self)
        # 타이머에 호출할 함수 연결
        self.qtimer.timeout.connect(self.timer)
        # 1초마다 연결된 함수를 실행
        self.qtimer.start(1000 // 60)


        #이미지




        #창 띄우기
        self.show()

    def timer(self):
        self.env.step(np.array(self.press_buttons))

        self.image = self.env.get_screen()
        self.screen = self.env.get_screen()
        self.qimage = QImage(self.image, self.image.shape[1], self.image.shape[0], QImage.Format_RGB888)
        pixmap = QPixmap(self.qimage)
        pixmap = pixmap.scaled(int(self.screen.shape[0] * 2), int(2 * self.screen.shape[1]), Qt.IgnoreAspectRatio)

        self.label_image.setPixmap(pixmap)




    def keyPressEvent(self, event):
        key = event.key()
        if key == Qt.Key_Up:
            self.press_buttons[7] = 1

    def keyReleaseEvent(self, event):
        key = event.key()
        if key == Qt.Key_Up:
            self.press_buttons[7] = 0








#직접 실행할때만 실행되는 코드
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    sys.exit(app.exec_())