import pyxel
import xj_python


def div_rect(x_pos, y_pos, wd, ratio, color, thr):
    itr = 0
    x_end_pos = x_pos + wd
    y_end_pos = y_pos + wd / ratio
    pyxel.rect(x_pos, y_pos, wd, wd / ratio, color % 16)
    color += 1

    while wd > thr:
        itr += 1
        if itr % 2 == 0:
            while x_pos + wd < x_end_pos + 0.1:
                div_square(x_pos, y_pos, wd, ratio, color, thr)
                x_pos += wd
            wd = x_end_pos - x_pos
        else:
            while y_pos + wd < y_end_pos + 0.1:
                div_square(x_pos, y_pos, wd, ratio, color, thr)
                y_pos += wd
            wd = y_end_pos - y_pos


def div_square(x_pos, y_pos, wd, ratio, color, thr):
    itr = 0
    x_end_pos = wd + x_pos
    y_end_pos = wd + y_pos
    pyxel.rect(x_pos, y_pos, wd, wd, color % 16)
    color += 1

    while wd > thr:
        itr += 1
        if itr % 2 == 1:
            while x_pos + wd * ratio < x_end_pos + 0.1:
                div_rect(x_pos, y_pos, wd * ratio, ratio, color, thr)
                x_pos += wd * ratio
            wd = x_end_pos - x_pos
        else:
            while y_pos + wd / ratio < y_end_pos + 0.1:
                div_rect(x_pos, y_pos, wd, ratio, color, thr)
                y_pos += wd / ratio
            wd = y_end_pos - y_pos


class Euclid(xj_python.Base):
    def __init__(self):
        self.num_a = 10
        self.num_b = 6
        self.color = 1
        self.thr = 10

        super().__init__()
        pyxel.init(self.window_width, self.window_height, caption="Template")
        self.audio_initialize()
        pyxel.run(self.update, self.draw)

    def update(self):
        super().update()
        if self.midi_events is not None:
            if self.midi_events[0][0][1] == 1:
                self.num_a = 1 + self.midi_events[0][0][2]
            if self.midi_events[0][0][1] == 2:
                self.num_b = 1 + self.midi_events[0][0][2]
            if self.midi_events[0][0][1] == 3:
                self.thr = 5 + self.midi_events[0][0][2]

    def draw(self):
        pyxel.cls(0)
        if self.num_a is not self.num_b:
            ratio = self.num_b / self.num_a
        div_square(0, 0, self.window_width, ratio, self.color, self.thr)
        self.audio_sequence()


if __name__ == '__main__':
    Euclid()
