import pyxel
import template
import recur_div_square as rds
import time


class EuclidMusic(template.Base):
    def __init__(self):
        self.num_a = 10
        self.num_b = 6
        self.color = 1
        self.thr = 10

        super().__init__()

        # music setting
        self.music_x = 0
        self.music_y = 0
        self.music_size = 20
        self.music_flag = True
        self.music_timer = 0
        self.music_wait = 0.4
        pyxel.init(self.window_width, self.window_height, caption="Template")
        pyxel.sound(0).set("c3", "p", "7", "s", 5)
        pyxel.sound(1).set("d3", "p", "7", "s", 5)
        pyxel.sound(2).set("e3", "p", "7", "s", 5)
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
        rds.div_square(0, 0, self.window_width, ratio, self.color, self.thr)

        if self.music_flag is True:
            self.music_flag = False
            self.music_timer = time.time()
            self.music_x += self.music_size
            while self.music_x > self.window_width:
                self.music_x -= self.window_width
                self.music_y += self.music_size
            while self.music_y > self.window_height:
                self.music_y -= self.window_height
            note = pyxel.pget(self.music_x, self.music_y) % 3
            pyxel.play(0, note, loop=False)

        else:
            if time.time() - self.music_timer > self.music_wait:
                self.music_flag = True
        pyxel.rect(self.music_x, self.music_y, self.music_size, self.music_size, 1)


if __name__ == '__main__':
    EuclidMusic()
