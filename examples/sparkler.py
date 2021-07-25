# Reference Nikkei Software 2021/07 P.142-P.149 "Sparkler"
import pyxel
import xj
import random
import numpy as np
import sys
# print(sys.getrecursionlimit())
sys.setrecursionlimit(20000)


class Sparkler(xj.Base):
    def __init__(self):
        self.thr = 0.47
        self.color = 1
        self.draw_enable = True

        super().__init__()
        self.lattice = np.random.uniform(0, 1.0, (self.window_width, self.window_height)).tolist()
        self.x_initial_pos = int(random.random() * self.window_width)
        self.y_initial_pos = int(random.random() * self.window_height)

        pyxel.init(self.window_width, self.window_height, caption="Sparkler")
        pyxel.cls(7)
        pyxel.run(self.update, self.draw)

    def update(self):
        super().update()
        if pyxel.btnp(pyxel.KEY_Z):
            self.color = random.random() * 16 % 16
            self.draw_enable = True
            self.x_initial_pos = int(random.random() * self.window_width)
            self.y_initial_pos = int(random.random() * self.window_height)
        if pyxel.btnp(pyxel.KEY_X):
            pyxel.cls(7)
        if pyxel.btnp(pyxel.KEY_C):
            self.thr += 0.01
        if pyxel.btnp(pyxel.KEY_V):
            self.thr -= 0.01
        if pyxel.btnp(pyxel.KEY_B):
            self.lattice = np.random.uniform(0, 1.0, (self.window_width, self.window_height)).tolist()

    def walk(self, x_pos, y_pos, threshold):
        pyxel.rect(x_pos, y_pos, 1, 1, self.color)
        self.lattice[x_pos][y_pos] = -1

        direction_order = list(range(4))
        random.shuffle(direction_order)
        for direction in direction_order:
            if direction == 0:
                if 0 < x_pos and threshold < self.lattice[x_pos - 1][y_pos]:
                    self.walk(x_pos - 1, y_pos, threshold)

            if direction == 1:
                if x_pos < self.window_width - 1 and threshold < self.lattice[x_pos + 1][y_pos]:
                    self.walk(x_pos + 1, y_pos, threshold)

            if direction == 2:
                if 0 < y_pos and threshold < self.lattice[x_pos][y_pos - 1]:
                    self.walk(x_pos, y_pos - 1, threshold)

            if direction == 3:
                if y_pos < self.window_height - 1 and threshold < self.lattice[x_pos][y_pos + 1]:
                    self.walk(x_pos, y_pos + 1, threshold)

    def draw(self):
        if self.draw_enable:
            self.walk(self.x_initial_pos, self.y_initial_pos, self.thr)
            self.draw_enable = False


if __name__ == '__main__':
    Sparkler()
