import pyxel
import template


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
        wd = self.window_width
        self.ratio = self.num_b / self.num_a
        tmp_color = self.color_base
        x_pos = 0
        y_pos = 0
        itr = 0

        while wd > 0.1:
            itr += 1
            if itr % 2 == 1:
                while x_pos + wd * self.ratio < self.window_width + 0.1:
                    pyxel.rect(x_pos, y_pos, wd * self.ratio, wd, tmp_color % 16)
                    x_pos += wd * self.ratio
                    tmp_color += 1
                wd = self.window_width -x_pos
            else:
                while y_pos + wd / self.ratio < self.window_width + 0.1:
                    pyxel.rect(x_pos, y_pos, wd, wd / self.ratio, tmp_color % 16)
                    y_pos += wd / self.ratio
                    tmp_color += 1
                wd = self.window_width - y_pos


if __name__ == '__main__':
    Euclid()
