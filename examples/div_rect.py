import pyxel
import xj


class Euclid(xj.Base):
    def __init__(self):
        self.num_a = 10
        self.num_b = 6
        self.scalar = 10
        self.color_base = 1
        super().__init__()
        pyxel.init(self.window_width, self.window_height, caption="Template")
        pyxel.run(self.update, self.draw)

    def update(self):
        super().update()
        if self.midi_events is not None:
            if self.midi_events[0][0][1] == 1:
                self.num_a = 10 + self.midi_events[0][0][2]
            if self.midi_events[0][0][1] == 2:
                self.num_b = 6 + self.midi_events[0][0][2]
            if self.midi_events[0][0][1] == 3:
                self.scalar = 10 + self.midi_events[0][0][2]

    def draw(self):
        pyxel.cls(0)
        tmp_num_a = self.num_a * self.scalar
        tmp_num_b = self.num_b * self.scalar
        tmp_color = self.color_base
        wd = tmp_num_b
        x_pos = 0
        y_pos = 0
        itr = 0

        while wd > 0:
            itr += 1
            if itr % 2 == 1:
                while x_pos + wd <= tmp_num_a:
                    pyxel.rect(x_pos, y_pos, wd, wd, tmp_color % 16)
                    x_pos += wd
                    tmp_color += 1
                wd = tmp_num_a - x_pos
            else:
                while y_pos + wd <= tmp_num_b:
                    pyxel.rect(x_pos, y_pos, wd, wd, tmp_color % 16)
                    y_pos += wd
                    tmp_color += 1
                wd = tmp_num_b - y_pos


if __name__ == '__main__':
    Euclid()
