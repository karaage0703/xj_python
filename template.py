import pyxel
import pygame.midi


class Base:
    def __init__(self):
        # general setting
        self.window_width = 256
        self.window_height = 256

        # midi setting
        self.midi_events = None
        self.midi_input = None

        pygame.midi.init()
        for i in range(pygame.midi.get_count()):
            interf, name, input_dev, output_dev, opened = pygame.midi.get_device_info(i)
            if input_dev and b'X-TOUCH MINI' in name:
                print('X-TOUCH MINI is found, midi id=' + str(i))
                self.midi_input = pygame.midi.Input(i)

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
        pyxel.cls(1)


if __name__ == '__main__':
    class Blank(Base):
        def __init__(self):
            super().__init__()
            pyxel.init(self.window_width, self.window_height, caption="Template")
            pyxel.run(self.update, self.draw)

    Blank()
