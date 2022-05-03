import cv2
import numpy as np
import glob
import sys

from pyparsing import col


class Image:
    def __init__(self, path) -> None:
        if isinstance(path, int):
            self.__path = path
        elif isinstance(path, str):
            full_path = glob.glob(path, recursive=True)
            if full_path:
                self.__path = full_path[0]
            else:
                print('Coul not find file:', path)
                sys.exit(1)

    def set_window(self, name: str = 'Frame', x_pos: int = 20, y_pos: int = 20):
        cv2.namedWindow(name)
        cv2.moveWindow(name, x_pos, y_pos)

    def show_img(self, img, name: str = 'Frame'):
        cv2.imshow(name, img)

    def close_window(self, name: str = 'Frame'):
        cv2.destroyWindow(name)

    def close_windows(self):
        cv2.destroyAllWindows()

    def release(self, video):
        video.release()

    def gray(self, img: np.ndarray):
        return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    def gaussian_blur(self, img, kernel: tuple = (7, 7), skip: int = 0):
        return cv2.GaussianBlur(img, kernel, skip)

    def canny_edge_detector(self, img, threshold_1: int = 100, threshold_2: int = 200, aperture_size: int = 3):
        return cv2.Canny(img, threshold_1, threshold_2, apertureSize=aperture_size)

    def dilate(self, img, kernel, iterations):
        return cv2.dilate(img, kernel, iterations=iterations)

    def find_contours(self, img, hierarchy_1, hierarchy_2):
        return cv2.findContours(img, hierarchy_1, hierarchy_2)

    def put_text(self, img, text: str, coor: tuple, font, font_scale: int, color: tuple, thikness: int):
        cv2.putText(img, text, coor, font, font_scale, color, thikness)

    def draw_contours(self, img, coor, line_type, color, thikness):
        cv2.drawContours(img, [coor], line_type, color, thikness)

    def hsv_to_cv_hsv(self, hsv: np.ndarray) -> np.ndarray:
        '''
        Color normalization of HSV to OpenCV HSV
        For HSV, Hue range is [0,179], Saturation range is [0,255]
        and Value range is [0,255]. Different software use different scales.
        So if you are comparing in OpenCV values with them, you need to normalize these ranges.
        '''
        hsv_cv = np.array([179, 255, 255])
        hsv_orig = np.array([360, 100, 100])
        cv_hsv = np.divide((hsv * hsv_cv), hsv_orig)
        return cv_hsv

    def video_capure(self):
        video_capture = cv2.VideoCapture(self.__path)
        if video_capture.isOpened():
            # width
            width = video_capture.get(3)
            # height
            height = video_capture.get(4)
            return (video_capture, width, height)
        print('Video Capture not opened')
        sys.exit(1)

    def check_key(self, c: str = 'q') -> bool:
        '''check if key q was pressed'''
        if cv2.waitKey(1) & 0xFF == ord(c):
            return True
        return False

    def factor(self, dim, max_height=600, factor=1):
        w, h = dim
        if factor == 1:
            factor = max_height / h
            h = max_height
            w = int(w * factor)
        else:
            h = int(h * factor)
            w = int(w * factor)
        return (w, h)

    def resize(self, img: np.ndarray, dim: tuple) -> np.array:
        return cv2.resize(img, (dim[0], dim[1]))

    def bitwise_and(self, img_1, img_2):
        return cv2.bitwise_and(img_1, img_2)

    def hough_lines(self, img: np.ndarray, rho: float, theta: float, threshold: int, min_length: int, max_gap: int):
        lines = cv2.HoughLinesP(img, rho=rho, theta=theta, threshold=threshold,
                                minLineLength=min_length, maxLineGap=max_gap)
        return np.squeeze(lines)

    def draw_lines(self, img: np.ndarray, lines: np.ndarray):
        line_thickness = 2
        for x1, y1, x2, y2 in lines:
            cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0),
                     thickness=line_thickness)

    def get_color(self, img, colors):
        color_dict = {'white': 0, 'green': 1, 'red': 2,
                      'blue': 3, 'orange': 4, 'yellow': 5}
        h, s, v = tuple(np.mean(img, axis=(0, 1)))

        print(h, s, v)

        for key in list(colors.keys()):
            h_lower, s_lower, v_lower = self.hsv2cvhsv(colors[key][0])
            h_upper, s_upper, v_upper = self.hsv2cvhsv(colors[key][1])
            lower = h >= h_lower and s >= s_lower and v >= v_lower
            upper = h <= h_upper and s <= s_upper and v <= v_upper
            if lower and upper:
                return key
        return -1

    # color normalization of HSV to OpenCV HSV
    def hsv2cvhsv(self, hsv: np.array) -> np.array:
        # For HSV, Hue range is [0,179], Saturation range is [0,255]
        # and Value range is [0,255]. Different software use different scales.
        # So if you are comparinn in OpenCV values with them, you need to normalize these ranges.
        hsv_cv = np.array([180, 255, 255])
        hsv_orig = np.array([360, 100, 100])
        cv_hsv = np.divide((hsv * hsv_cv), hsv_orig)
        return cv_hsv
