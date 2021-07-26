import retro
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt
import numpy as np
from PyQt5.QtCore import QTimer



env = retro.make(game='SuperMarioBros-Nes', state='Level1-1')
env.reset()


#print(screen.shape[0], screen.shape[1])
#print(screen)

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        a = 2

        

        screen = self.env.get_screen()

        #창크기 조절
        self.setFixedSize(int(screen.shape[0] * a), int(a * screen.shape[1]))
        #창제목 설정
        self.setWindowTitle('GA Mario')

        self.qtimer = QTimer(self)
        # 타이머에 호출할 함수 연결
        self.qtimer.timeout.connect(self.timer)
        # 1초마다 연결된 함수를 실행
        self.qtimer.start(1000 / 60)


        #이미지
        label_image = QLabel(self)
        image = env.get_screen()
        qimage = QImage(image, image.shape[1], image.shape[0], QImage.Format_RGB888)
        pixmap = QPixmap(qimage)
        pixmap = pixmap.scaled(int(screen.shape[0] * a), int(a * screen.shape[1]), Qt.IgnoreAspectRatio)

        label_image.setPixmap(pixmap)
        label_image.setGeometry(0, 0, int(screen.shape[0] * a), int(a * screen.shape[1]))



        #창 띄우기
        self.show()

    def timer(self):
        env.step(np.array([0, 0, 0, 1, 0, 0, 0, 0, 0]))

#직접 실행할때만 실행되는 코드
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    sys.exit(app.exec_())