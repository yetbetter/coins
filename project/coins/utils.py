import cv2 as opencv
from PIL import Image as image


def open_image(path_to_img):
    return image.open(path_to_img)


def get_metadata(opened_img):
    return opened_img.size


def get_average_color(opened_img):
    rgb_img = opened_img.convert('RGB')
    return rgb_img.getpixel((1, 1))


def count_coins(path_to_image):
    img = opencv.imread(path_to_image)

    gray_img = opencv.cvtColor(img, opencv.COLOR_BGR2GRAY)
    blur_img = opencv.GaussianBlur(gray_img, (3, 3), 0)
    contour_img = opencv.Canny(blur_img, 10, 250)
    kernel = opencv.getStructuringElement(opencv.MORPH_RECT, (7, 7))
    without_gap_img = opencv.morphologyEx(contour_img, opencv.MORPH_CLOSE, kernel)
    contours = opencv.findContours(without_gap_img.copy(),
                                   opencv.RETR_EXTERNAL,
                                   opencv.CHAIN_APPROX_SIMPLE)[1]

    total = 0
    for contour in contours:
        perimeter = opencv.arcLength(contour, True)
        approx = opencv.approxPolyDP(contour, 0.02 * perimeter, True)

        if len(approx) == 8:
            total += 1

    return total