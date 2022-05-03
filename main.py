from rubik import Rubik
from image import Image
import cv2
import numpy as np


def main():
    image = Image(0)
    win_name = 'Frame'
    image.set_window(win_name)
    capt, W, H = image.video_capure()
    W, H = image.factor((W, H), 300)
    key_q = False
    kernel_ellipse = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2, 2))
    kernel_square = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
    ret = True
    colors = {0: (255, 255, 255), 1: (0, 200, 0), 2: (0, 0, 200),
              3: (200, 0, 0), 4: (0, 130, 255), 5: (0, 255, 255), -1: (0, 0, 0)}

    hsv_colors = {0: [(0, 0, 85), (360, 5, 100)],
                  1: [(80, 60, 40), (140, 100, 100)],
                  2: [(0, 60, 40), (20, 100, 100)],
                  3: [(160, 60, 40), (250, 100, 100)],
                  4: [(15, 50, 70), (50, 100, 100)],
                  5: [(45, 50, 70), (70, 100, 100)]}
    while not key_q and ret:
        key_q = image.check_key('q')
        ret, frame = capt.read()
        frame = image.resize(frame, (W, H))
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        gray = image.gray(frame)

        blur = image.gaussian_blur(gray, (3, 3), 0)

        edges = image.canny_edge_detector(
            blur, threshold1=30, threshold2=100, apertureSize=3)
        dilate = image.dilate(edges, kernel_square, iterations=3)

        contours, hirarchy = image.find_contours(
            dilate, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

        contour_id = 0
        i = 0
        face = []
        for contour in contours:
            area = cv2.contourArea(contour, True)
            contour_id += 1
            if area > 1000 and area < 3000:
                perimeter = cv2.arcLength(contour, True)
                hull = cv2.convexHull(contour)
                if cv2.norm(((perimeter / 4) * (perimeter / 4)) - area) < 150:
                    x, y, w, h = cv2.boundingRect(hull)
                    cubie = hsv[y+3:y + h - 3, x + 3: x + w - 3, :]

                    color = image.get_color(cubie, hsv_colors)

                    cv2.drawContours(frame, [hull], 0, colors[color], 2)

                    cv2.putText(frame, str(i), (x + int(w / 2), y + int(h/2)),
                                cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
                    i += 1
                    face += [np.array([x, y, w, h])]

        image.show_img(frame, win_name)

    image.release(capt)
    image.close_window(win_name)


def test():
    rubik = Rubik()
    rubik.create_solved_cube()
    print(rubik)


if __name__ == '__main__':
    test()
