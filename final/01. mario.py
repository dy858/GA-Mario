import sys
import retro
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPainter, QPen, QBrush, QColor
import numpy as np

relu = lambda x: np.maximum(0, x)
sigmoid = lambda x: 1.0 / (1.0 + np.exp(-x))


class Chromosome:
    def __init__(self):
        self.w1 = np.random.uniform(low=-1, high=1, size=(13 * 16, 9))
        self.b1 = np.random.uniform(low=-1, high=1, size=(9,))

        self.w2 = np.random.uniform(low=-1, high=1, size=(9, 6))
        self.b2 = np.random.uniform(low=-1, high=1, size=(6,))

        self.distance = 0
        self.max_distance = 0
        self.frames = 0
        self.stop_frames = 0
        self.win = 0

    def predict(self, data):
        l1 = relu(np.matmul(data, self.w1) + self.b1)
        output = sigmoid(np.matmul(l1, self.w2) + self.b2)
        result = (output > 0.5).astype(np.int)
        return result

    def fitness(self):
        return self.distance


class GeneticAlgorithm:
    def __init__(self):
        self.chromosomes = [Chromosome() for _ in range(10)]
        self.generation = 0
        self.current_chromosome_index = 0

    def selection(self):
        result = self.chromosomes[:2]
        return result

    def crossover(self, chromosome1, chromosome2):
        child1 = Chromosome()
        child2 = Chromosome()

        return child1, child2

    def mutation(self, chromosome):
        pass

    def next_generation(self):
        next_chromosomes = []
        for i in range(5):
            selected_chromosome = self.selection()

            # ======================== 교배 연산 =====================
            child_chromosome1, child_chromosome2 = self.crossover(
                selected_chromosome[0],
                selected_chromosome[1])
            # ======================================================


            self.mutation(child_chromosome1)
            self.mutation(child_chromosome2)

            next_chromosomes.append(child_chromosome1)
            next_chromosomes.append(child_chromosome2)

        self.chromosomes = next_chromosomes
        self.generation += 1
        self.current_chromosome_index = 0



class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('GA Mario')

        self.env = retro.make(game='SuperMarioBros-Nes', state='Level1-1')
        screen = self.env.reset()

        self.screen_width = screen.shape[0] * 2
        self.screen_height = screen.shape[1] * 2

        self.setFixedSize(self.screen_width + 500, self.screen_height + 100)

        self.screen_label = QLabel(self)
        self.screen_label.setGeometry(0, 0, self.screen_width, self.screen_height)

        self.ga = GeneticAlgorithm

        self.game_timer = QTimer(self)
        self.game_timer.timeout.connect(self.update_timer)
        self.game_timer.start(1000 // 60)

        self.show()

    def update_timer(self):
        screen = self.env.get_screen()


    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)

        painter.setPen(QPen(Qt.black))

        ram = self.env.get_ram()

        full_screen_tiles = ram[0x0500:0x069F + 1]

        # print(full_screen_tiles.shape)
        # print(full_screen_tiles)

        full_screen_tile_count = full_screen_tiles.shape[0]

        full_screen_page1_tile = full_screen_tiles[:full_screen_tile_count // 2].reshape((13, 16))
        full_screen_page2_tile = full_screen_tiles[full_screen_tile_count // 2:].reshape((13, 16))

        full_screen_tiles = np.concatenate((full_screen_page1_tile, full_screen_page2_tile), axis=1).astype(np.int)

        painter.end()


#직접 실행할때만 실행되는 코드
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    sys.exit(app.exec_())