from image import Image


def main():
    image = Image(0)
    win_name = 'Frame'
    image.set_window(win_name)
    capt, w, h = image.video_capure()
    w, h = image.factor((w, h), 300)
    key_q = False

    while not key_q:
        key_q = image.check_key('q')
        ret, frame = capt.read()
        frame = image.resize(frame, (w, h))
        gray = image.gray(frame)

        image.show_img(frame, win_name)

    image.release(capt)
    image.close_window(win_name)


if __name__ == '__main__':
    main()
