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


# rotate_right 向右翻转
def rotate_right(image: list[list[tuple[int, int, int]]]) -> list[list[tuple[int, int, int]]]:
    rotated = []
    num_rows = len(image)
    num_cols = len(image[0])

    for j in range(num_cols):
        rotated.append([])
        for i in range(num_rows-1, -1, -1):
            rotated[-1].append(image[i][j])

    return rotated


# crop 裁剪
def crop(image: list[list[tuple[int, int, int]]],
         x: int, # 开始裁剪的坐标点
         y: int,
         width: int, # 开始裁剪的长宽
         height: int) -> list[list[tuple[int, int, int]]]:

    cropped = []
    for i in range(y, y + height):
        cropped.append([])
        for j in range(x, x + width):
            cropped[-1].append(image[i][j])

    return cropped


# 平移
def shift(image: list[list[tuple[int, int, int]]],
          horizontal: int, # 平移的垂直和水平距离
          vertical: int) -> list[list[tuple[int, int, int]]]:
    shifted = []
    num_rows = len(image)
    num_cols = len(image[0])

    for i in range(num_rows):
        shifted.append([])
        for j in range(num_cols):
            new_i = i + vertical
            new_j = j + horizontal
            # 在画布内的用平移的像素代替
            if 0 <= new_i < num_rows and 0 <= new_j < num_cols:
                shifted[-1].append(image[new_i][new_j])
            else:
                # 其余的用黑色像素点补位
                shifted[-1].append((0,0,0))

    return shifted