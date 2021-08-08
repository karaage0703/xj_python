import cv2
import pyxel
import xj_python


class Camera(xj_python.Base):
    def __init__(self):
        self.color_numb = 0
        self.cap = cv2.VideoCapture(1)

        super().__init__()
        pyxel.init(self.window_width, self.window_height, caption="Camera")
        pyxel.run(self.update, self.draw)

    def update(self):
        super().update()
        if self.midi_events is not None:
            self.color_numb = self.midi_events[0][0][2] % 16

    def color_palette_matching(self, color):
        palette_list = [[0, 0, 0], [43, 51, 95], [126, 32, 114], [25, 149, 156],
            [139, 72, 82], [57, 92, 152], [169, 193, 255], [238, 238, 238], [212, 24, 108],
            [211, 132, 65], [233, 195, 91], [112, 198, 169], [118, 150, 222], [163, 163, 163],
            [255, 151, 152], [237, 199, 176]]

        min_color_distance = 255 * 255 * 255 + 1
        for i in range(len(palette_list)):
            rgb = [0, 0, 0]
            for ch in range(len(color)):
                rgb[ch] = color[ch] - palette_list[i][ch]
            color_distance = rgb[0] ** 2 + rgb[1] ** 2 + rgb[2] ** 2
            if color_distance < min_color_distance:
                min_color_distance = color_distance
                pick_color = i

        print(pick_color)
        return pick_color

    def draw(self):
        try:
            ret, image = self.cap.read()
            image = cv2.flip(image, 1)
            image = cv2.resize(image, (self.window_width, self.window_height))
            for y in range(image.shape[0]):
                for x in range(image.shape[1]):
                    pyxel.pset(x, y, int(image[y][x][0] / 20))
                    # pyxel.pset(x, y, self.color_palette_matching(image[y][x]))
        except cv2.error:
            print('cv2.error')


if __name__ == '__main__':
    Camera()
