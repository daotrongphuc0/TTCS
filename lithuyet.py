import cv2
import numpy as np
# path
path = r"E:\code-ptit\python\BTL ttcs\btl\rex.jpg"
image = cv2.imread(path)
cv2.imshow("Image", image)
cv2.waitKey(0)
#image = cv2.imwrite("newimage.jpg",image)

#show kích thước ảnh
print("width: {} pixels".format(image.shape[1]))
print("height: {} pixels".format(image.shape[0]))
print("channels: {}".format(image.shape[2]))

#dịch ảnh sang phải 25 và xuống dưới 50
M = np.float32([[1, 0, 25], [0, 1, 50]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted Down and Right", shifted)
cv2.waitKey(0)

canvas = np.zeros((300, 300, 3), dtype="uint8") # tạo cua sổ 300x300 px bang chuoi bit 8
green = (0, 255, 0) # tạo tuple RGB

# vẽ đường thẳng
cv2.line(canvas, (0, 0), (300, 300), green,3) # kẻ đường thẳng tu 0.0 den 300.300 màu xanh độ rộng 3px
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# vẽ hình chữ nhật
cv2.rectangle(canvas, (10, 10), (60, 60), green)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# vẽ hình tròn
cv2.circle(canvas, (50,50), 20, green, 3)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
