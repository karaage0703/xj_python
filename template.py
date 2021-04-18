import pyxel
import pygame.midi


class Base:
    def __init__(self):
        pygame.midi.init()
        self.midi_events = None
        self.midi_input = None
        self.window_width = 256
        self.window_height = 256

        for i in range(pygame.midi.get_count()):
            interf, name, input_dev, output_dev, opened = pygame.midi.get_device_info(i)
            if input_dev and b'X-TOUCH MINI' in name:
                print('X-TOUCH MINI is found, midi id=' + str(i))
                self.midi_input = pygame.midi.Input(i)

        pyxel.init(self.window_width, self.window_height, caption="Template")
        pyxel.sound(0).set("c3", "p", "7", "s", 5)
        pyxel.sound(1).set("d3", "p", "7", "s", 5)
        pyxel.sound(2).set("e3", "p", "7", "s", 5)
        pyxel.run(self.update, self.draw)

    def update(self):
        if self.midi_input is not None:
            if self.midi_input.poll():
                self.midi_events = self.midi_input.read(10)
                print("full midi_events:" + str(self.midi_events))
        if pyxel.btnp(pyxel.KEY_Q):
            self.midi_input.close()
            pygame.midi.quit()
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)


if __name__ == '__main__':
    print("base")
    Base()
