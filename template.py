import pyxel
import pygame.midi


class Base:
    def __init__(self):
        pygame.midi.init()
        self.midi_events = None

        for i in range(pygame.midi.get_count()):
            interf, name, input_dev, output_dev, opened = pygame.midi.get_device_info(i)
            if input_dev and b'X-TOUCH MINI' in name:
                print('X-TOUCH MINI is found, midi id=' + str(i))
                self.midi_input = pygame.midi.Input(i)

        pyxel.init(256, 256, caption="Template")
        pyxel.run(self.update, self.draw)

    def update(self):
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
