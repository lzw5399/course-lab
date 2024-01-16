#!/usr/bin/python3

import cv2
import numpy as np


def mirror(image: list[list[tuple[int, int, int]]]) -> list[list[tuple[int, int, int]]]:
    # 获取图像的行数和列数
    rows = len(image)
    cols = len(image[0])

    # 创建一个空白的镜像图像
    mirrored_image = [[(0, 0, 0) for _ in range(cols)] for _ in range(rows)]

    # 遍历原始图像并生成镜像
    for i in range(rows):
        mirrored_image[rows - i - 1] = image[i]

    return mirrored_image

# change_colors 将指定的RGB像素点 转换成另一个 颜色
def change_colors(image: list[list[tuple[int, int, int]]],
                  to_change: tuple[int, int, int], 
                  to_change_to: tuple[int, int, int]) -> list[list[tuple[int, int, int]]]:
    result_image = []
    
    for row in image:
        new_row = []
        for pixel in row:
            if pixel == to_change:
                new_row.append(to_change_to)
            else:
                new_row.append(pixel)
        result_image.append(new_row)
    
    return result_image


# 灰度
def grayscale(image: list[list[tuple[int, int, int]]]) -> list[list[tuple[int, int, int]]]:
    gray_image = []

    for row in image:
        gray_row = []
        for pixel in row:
            # 计算灰度值, 公式依据: https://stackoverflow.com/questions/17615963/standard-rgb-to-grayscale-conversion
            # The RGB values are converted to grayscale using the NTSC formula: 0.299 ∙ Red + 0.587 ∙ Green + 0.114 ∙ Blue
            gray_value = int(0.299 * pixel[0] + 0.587 * pixel[1] + 0.114 * pixel[2])
            gray_pixel = (gray_value, gray_value, gray_value)
            gray_row.append(gray_pixel)

        gray_image.append(gray_row)

    return gray_image
