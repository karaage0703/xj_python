import pyxel
import template


def div_square(x_pos, y_pos, wd, ratio, color):
    itr = 0
    x_end_pos = wd + x_pos
    y_end_pos = wd + y_pos

    while wd > 0.1:
        itr += 1
        if itr % 2 == 1:
            while x_pos + wd * ratio < x_end_pos + 0.1:
                pyxel.rect(x_pos, y_pos, wd * ratio, wd, color % 16)
                x_pos += wd * ratio
                color += 1
            wd = x_end_pos - x_pos
        else:
            while y_pos + wd / ratio < y_end_pos + 0.1:
                pyxel.rect(x_pos, y_pos, wd, wd / ratio, color % 16)
                color += 1
                y_pos += wd / ratio
            wd = y_end_pos - y_pos


class Euclid(template.Base):
    def __init__(self):
        self.num_a = 10
        self.num_b = 6
        self.color_base = 1
        super().__init__()

    def update(self):
        super().update()
        if self.midi_events is not None:
            if self.midi_events[0][0][1] == 1:
                self.num_a = 10 + self.midi_events[0][0][2]
            if self.midi_events[0][0][1] == 2:
                self.num_b = 6 + self.midi_events[0][0][2]

    def draw(self):
        pyxel.cls(0)
        ratio = self.num_b / self.num_a
        color = self.color_base
        itr = 0
        x_pos = 0
        y_pos = 0
        wd = self.window_width * ratio

        while wd > 0.1:
            itr += 1
            if itr % 2 == 1:
                while x_pos + wd < self.window_width + 0.1:
                    div_square(x_pos, y_pos, wd, ratio, color)
                    x_pos += wd
                    color += 1
                wd = self.window_width - x_pos
            else:
                while y_pos + wd < self.window_width * ratio + 0.1:
                    div_square(x_pos, y_pos, wd, ratio, color)
                    y_pos += wd
                    color += 1
                wd = self.window_width * ratio - y_pos


if __name__ == '__main__':
    Euclid()
