import cv2

# 读取图片
img = cv2.imread('image.png') 

# 变灰
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 翻转
flipped = cv2.flip(gray, 1) 

# 输出
cv2.imwrite('gray_flipped.jpg', flipped)
