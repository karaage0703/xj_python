import pyxel
import template


class Color(template.Base):
    def __init__(self):
        self.color_numb = 0
        super().__init__()

    def update(self):
        super().update()
        if self.midi_events is not None:
            self.color_numb = self.midi_events[0][0][2] % 16

    def draw(self):
        pyxel.cls(self.color_numb)


if __name__ == '__main__':
    Color()
