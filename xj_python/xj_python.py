import pyxel
import pygame.midi
import time

class Base:
    def __init__(self):
        # general setting
        self.window_width = 256
        self.window_height = 256

        # midi input setting
        self.midi_events = None
        self.midi_input = None
        self.midi_value_max = 127
        self.key_channel = 0
        self.key_value = [0, 0, 0, 0, 0, 0]
        self.midi_device_flag = False

        # audio output setting
        self.music_x = 0
        self.music_y = 0
        self.music_size = 10
        self.music_flag = True
        self.music_timer = 0
        self.music_wait = 0.1
        self.note_numb_max = 6

        pygame.midi.init()
        for i in range(pygame.midi.get_count()):
            interf, name, input_dev, output_dev, opened = pygame.midi.get_device_info(i)
            if input_dev and b'X-TOUCH MINI' in name:
                self.midi_device_flag = True
                print('X-TOUCH MINI is found, midi id=' + str(i))
                self.midi_input = pygame.midi.Input(i)

    def audio_initialize(self):
        pyxel.sound(0).set('d3', 'p', '7', 's', 5)
        pyxel.sound(1).set('e3', 'p', '7', 's', 5)
        pyxel.sound(2).set('f3', 'p', '7', 's', 5)
        pyxel.sound(3).set('g3', 'p', '7', 's', 5)
        pyxel.sound(4).set('a3', 'p', '7', 's', 5)
        pyxel.sound(5).set('b3', 'p', '7', 's', 5)

    def add_key(self, channel, value):
        self.key_channel = channel
        self.key_value[self.key_channel] += value
        if self.key_value[self.key_channel] < 0:
            self.key_value[self.key_channel] = 0
        if self.key_value[self.key_channel] > self.midi_value_max:
            self.key_value[self.key_channel] = self.midi_value_max

    def audio_sequence(self):
        if self.music_flag is True:
            self.music_flag = False
            self.music_timer = time.time()
            self.music_x += self.music_size
            while self.music_x > self.window_width:
                self.music_x -= self.window_width
                self.music_y += self.music_size
            while self.music_y > self.window_height:
                self.music_y -= self.window_height
            note = pyxel.pget(self.music_x, self.music_y) % self.note_numb_max
            print(note)
            pyxel.play(0, note, loop=False)

        else:
            if time.time() - self.music_timer > self.music_wait:
                self.music_flag = True
        pyxel.rect(self.music_x, self.music_y, self.music_size, self.music_size, 1)

    def update(self):
        if self.midi_device_flag:
            if self.midi_input is not None:
                if self.midi_input.poll():
                    self.midi_events = self.midi_input.read(10)
                    print("full midi_events:" + str(self.midi_events))
        else:
            if pyxel.btnp(pyxel.KEY_E):
                self.add_key(1, 1)
            if pyxel.btnp(pyxel.KEY_D):
                self.add_key(1, -1)
            if pyxel.btnp(pyxel.KEY_R):
                self.add_key(2, 1)
            if pyxel.btnp(pyxel.KEY_F):
                self.add_key(2, -1)
            if pyxel.btnp(pyxel.KEY_T):
                self.add_key(3, 1)
            if pyxel.btnp(pyxel.KEY_G):
                self.add_key(3, -1)
            if pyxel.btnp(pyxel.KEY_Y):
                self.add_key(4, 1)
            if pyxel.btnp(pyxel.KEY_H):
                self.add_key(4, -1)
            if pyxel.btnp(pyxel.KEY_U):
                self.add_key(5, 1)
            if pyxel.btnp(pyxel.KEY_J):
                self.add_key(5, -1)
            if pyxel.btnp(pyxel.KEY_I):
                self.add_key(6, 1)
            if pyxel.btnp(pyxel.KEY_K):
                self.add_key(6, -1)

            self.midi_events = [[[0, self.key_channel, self.key_value[self.key_channel], 0], 0]]
            print("full midi_events:" + str(self.midi_events))

        if pyxel.btnp(pyxel.KEY_Q):
            if self.midi_device_flag:
                self.midi_input.close()
                pygame.midi.quit()
            pyxel.quit()

    def draw(self):
        pyxel.cls(1)


if __name__ == '__main__':
    class Blank(Base):
        def __init__(self):
            super().__init__()
            pyxel.init(self.window_width, self.window_height, caption="Template")
            pyxel.run(self.update, self.draw)

    Blank()
