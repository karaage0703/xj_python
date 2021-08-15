import cv2
import pyxel
import xj_python


class Camera(xj_python.Base):
    def __init__(self):
        self.color_numb = 0
        self.cap = cv2.VideoCapture(0)

        super().__init__()
        pyxel.init(self.window_width, self.window_height, caption="Camera")
        self.audio_initialize()
        pyxel.run(self.update, self.draw)

    def update(self):
        super().update()
        if self.midi_events is not None:
            self.color_numb = self.midi_events[0][0][2] % 16

    def draw(self):
        try:
            ret, image = self.cap.read()
            image = cv2.flip(image, 1)
            image = cv2.resize(image, (self.window_width, self.window_height))
            image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
            for y in range(image.shape[0]):
                for x in range(image.shape[1]):
                    pyxel.pset(x, y, (image[y][x][2] / 10) % 16)
            self.audio_sequence()
        except cv2.error:
            print('cv2.error')


if __name__ == '__main__':
    Camera()
