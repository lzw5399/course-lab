#!/usr/bin/python3

import sys
from PIL import Image
from transforms import change_colors, mirror, grayscale


def image_to_rgb_array(input_file):
    try:
        img = Image.open(input_file)
    except Exception as e:
        print(f"open image failed: {e}")
        return None

    img = img.convert("RGB")

    # 获取图像的宽度和高度
    width, height = img.size

    # 获取图像的 RGB 数据
    rgb_data = list(img.getdata())

    # 将 RGB 数据转换为二维数组
    rgb_array = [rgb_data[i:i+width] for i in range(0, len(rgb_data), width)]

    return rgb_array


def save_as_jpg(rgb_array, output_file):
    # 将 RGB 数组转换为图像
    width = len(rgb_array[0])
    height = len(rgb_array)
    image = Image.new("RGB", (width, height))

    for y, row in enumerate(rgb_array):
        for x, pixel in enumerate(row):
            image.putpixel((x, y), pixel)

    # 保存图像为 jpg 文件
    image.save(output_file, "JPEG")


if __name__ == "__main__":
    # 获取命令行参数, 必须是大于等于3个
    # 示例: python3 program.py ../cafe.jpg grayscale mirror
    # 第一个参数: program.py
    # 第二个参数: ../cafe.jpg 文件路径
    # 第三个之后的参数: grayscale, mirror 等，是一个针对图像进行依次处理的命令的管道
    if len(sys.argv) < 3:
        print("arg num err")
        exit(-1)

    file_path = sys.argv[1] # 文件路径

    img_rgb_array = image_to_rgb_array(file_path)

    # 创建一个空白的图像
    final_image_result = img_rgb_array

    commands = sys.argv[2:]
    for index, command in enumerate(commands):
        if command == "grayscale":
            final_image_result = grayscale(final_image_result)
            if index == len(commands) - 1:
                save_as_jpg(final_image_result, "cafe_gray.jpg")
        elif command == "mirror":
            final_image_result = mirror(final_image_result)
            if index == len(commands) - 1:
                save_as_jpg(final_image_result, "cafe_mirror.jpg")
        elif command == "change_colors":
            final_image_result = change_colors(final_image_result, to_change=(255, 255, 255), to_change_to=(0, 255, 0))
            if index == len(commands) - 1:
                save_as_jpg(final_image_result, "captura_change_colors.jpg")
