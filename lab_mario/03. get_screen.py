import retro
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt
import numpy as np
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPainter, QPen, QBrush, QColor

#보고서
#하게 된 계기, 과정, 느낀점





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
        self.setFixedSize(1200, int(2 * self.screen.shape[1]))
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

    def paintEvent(self, event):

        #램 정보
        ram = self.env.get_ram()


        full_screen_tiles = ram[0x0500:0x069F + 1]

        full_screen_tile_count = full_screen_tiles.shape[0]

        full_screen_page1_tile = full_screen_tiles[:full_screen_tile_count // 2].reshape((13, 16))
        full_screen_page2_tile = full_screen_tiles[full_screen_tile_count // 2:].reshape((13, 16))

        self.full_screen_tiles = np.concatenate((full_screen_page1_tile, full_screen_page2_tile), axis=1).astype(np.int)

        enemy_drawn = ram[0x000F:0x0013 + 1]

        enemy_horizon_position = ram[0x006E:0x0072 + 1]
        # 자신이 속한 페이지 속 x좌표
        enemy_screen_position_x = ram[0x0087:0x008B + 1]

        enemy_position_y = ram[0x00CF:0x00D3 + 1]

        enemy_position_x = (enemy_horizon_position * 256 + enemy_screen_position_x) % 512

        enemy_tile_position_x = (enemy_position_x + 8) // 16
        enemy_tile_position_y = (enemy_position_y - 8) // 16 - 1

        current_screen_page = ram[0x071A]
        # 0x071C	ScreenEdge X-Position, loads next screen when player past it?
        # 페이지 속 현재 화면 위치
        screen_position = ram[0x071C]
        # 화면 오프셋
        screen_offset = (256 * current_screen_page + screen_position) % 512
        # 타일 화면 오프셋
        screen_tile_offset = screen_offset // 16

        # 현재 화면 추출
        screen_tiles = np.concatenate((self.full_screen_tiles, self.full_screen_tiles), axis=1)[:,
                       screen_tile_offset:screen_tile_offset + 16]

        # 플레이어 현재 위치
        player_position_x = ram[0x03AD]
        player_position_y = ram[0x03B8]

        # 타일 좌표로 변환
        player_tile_position_x = (player_position_x + 8) // 16
        player_tile_position_y = (player_position_y + 8) // 16 - 1


        # 그리기 도구
        painter = QPainter()
        # 그리기 시작
        painter.begin(self)

        # RGB 설정으로 펜 설정
        painter.setPen(QPen(QColor.fromRgb(0, 0, 0), Qt.SolidLine))

        # 브러쉬 설정(채우기)

        # 직사각형 그리기
        for j in range(13):
            for i in range(32):
                x = 500 + 16 * i
                y = 20 + 16 * j
                if self.full_screen_tiles[j][i] == 0:
                    painter.setBrush(QBrush(Qt.gray))
                    painter.drawRect(x, y, 16, 16)  # 시작점 너비 높이
                else:
                    painter.setBrush(QBrush(Qt.blue))
                    painter.drawRect(x, y, 16, 16)






        for j in range(13):
            for i in range(16):
                x = 500 + 16 * i
                y = 250 + 16 * j
                if screen_tiles[j][i] == 0:
                    painter.setBrush(QBrush(Qt.gray))
                    painter.drawRect(x, y, 16, 16)
                elif j == player_tile_position_y and i == player_tile_position_x:
                    painter.setBrush(QBrush(Qt.red))
                    painter.drawRect(x, y, 16, 16)
                else:
                    painter.setBrush(QBrush(Qt.darkBlue))
                    painter.drawRect(x, y, 16, 16)

        for j in range(13):
            for i in range(16):
                x = 500 + 16 * i
                y = 250 + 16 * j
                if j == player_tile_position_y and i == player_tile_position_x:
                    painter.setBrush(QBrush(Qt.blue))
                    painter.drawRect(x, y, 16, 16)

                else:
                    pass



        for k in range(5):
            if enemy_drawn[k] == 1:
                for j in range(13):
                    for i in range(32):
                        x = 500 + 16 * i
                        y = 20 + 16 * j
                        if j == enemy_tile_position_y[k] and i == enemy_tile_position_x[k]:
                            painter.setBrush(QBrush(Qt.red))
                            painter.drawRect(x, y, 16, 16)
                        else:
                            pass

            else:
                pass















        painter.end()

    def timer(self):
        self.env.step(np.array(self.press_buttons))

        self.image = self.env.get_screen()
        self.screen = self.env.get_screen()
        self.qimage = QImage(self.image, self.image.shape[1], self.image.shape[0], QImage.Format_RGB888)
        pixmap = QPixmap(self.qimage)
        pixmap = pixmap.scaled(int(self.screen.shape[0] * 2), int(2 * self.screen.shape[1]), Qt.IgnoreAspectRatio)

        self.label_image.setPixmap(pixmap)


        self.update()




    # 키 배열: B, NULL, SELECT, START, U, D, L, R, A
    #env.step(np.array([0, 0, 0, 0, 0, 0, 0, 0, 0]))

    def keyPressEvent(self, event):
        key = event.key()
        if key == Qt.Key_Up:
            self.press_buttons[4] = 1
        elif key == Qt.Key_Down:
            self.press_buttons[5] = 1
        elif key == Qt.Key_Left:
            self.press_buttons[6] = 1
        elif key == Qt.Key_Right:
            self.press_buttons[7] = 1
        elif key == Qt.Key_A:
            self.press_buttons[8] = 1
        elif key == Qt.Key_B:
            self.press_buttons[0] = 1

    def keyReleaseEvent(self, event):
        key = event.key()
        if key == Qt.Key_Up:
            self.press_buttons[4] = 0
        elif key == Qt.Key_Down:
            self.press_buttons[5] = 0
        elif key == Qt.Key_Left:
            self.press_buttons[6] = 0
        elif key == Qt.Key_Right:
            self.press_buttons[7] = 0
        elif key == Qt.Key_A:
            self.press_buttons[8] = 0
        elif key == Qt.Key_B:
            self.press_buttons[0] = 00








#직접 실행할때만 실행되는 코드
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    sys.exit(app.exec_())