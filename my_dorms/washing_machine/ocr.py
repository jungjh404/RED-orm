import pytesseract
import cv2
import imutils
import numpy as np
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract'

img = cv2.imread("test.png")
# hsv = img.copy()
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower_red = np.array([0,0,0])
upper_red = np.array([0,255,255])

lower_green = np.array([0,150,0])
upper_green = np.array([80,255,255])

# mask = cv2.inRange(hsv, lower_red, upper_red)
mask = cv2.inRange(hsv, lower_green, upper_green)
cv2.imshow("img", mask)
cv2.waitKey(0)

res = cv2.bitwise_and(img, img, mask=mask)

res = cv2.GaussianBlur(res,(13,13), 0)
edged = cv2.Canny(res, 100, 200)
dilate = cv2.dilate(edged, None, iterations=4)
erode = cv2.erode(dilate, None, iterations=4)
cv2.imshow("img", dilate)
cv2.waitKey(0)
cv2.imshow("img", erode)
cv2.waitKey(0)
mask2 = np.ones(img.shape[:2], dtype="uint8") * 255

# cnts = cv2.findContours(erode.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
# print(cnts)
# cnts = cnts[0] if imutils.is_cv2() else cnts[1]

# orig = img.copy()
# for c in cnts:
#     # if the contour is not sufficiently large, ignore it
#     if cv2.contourArea(c) < 600:
#         cv2.drawContours(mask2, [c], -1, 0, -1)
#         continue

newimage = cv2.bitwise_and(erode.copy(), dilate.copy(), mask=mask2)
# Again perform dilation and erosion
newimage = cv2.dilate(newimage,None, iterations=7)
newimage = cv2.erode(newimage,None, iterations=5)
ret,newimage = cv2.threshold(newimage,0,255,cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)

print(pytesseract.image_to_string(newimage))
print(pytesseract.image_to_string(newimage, lang="kor"))
print(pytesseract.image_to_string(newimage, lang="letsgodigital", config="--psm 6 --oem 3 -c tessedit_char_whitelist=-01234567890XYZ:"))


cv2.imshow("img", newimage)
cv2.waitKey(0)
# print(pytesseract.image_to_string(Image.open("./test.png"), lang="kor", config="--psm 6 --oem 3 -c tessedit_char_whitelist=-01234567890XYZ: "))
# print(pytesseract.image_to_string(Image.fromarray(img), lang="kor", config="--psm 6 --oem 3 -c tessedit_char_whitelist=-01234567890XYZ:"))
# print(pytesseract.image_to_string(Image.fromarray(img), lang="letsgodigital", config="--psm 6 --oem 3 -c tessedit_char_whitelist=-01234567890XYZ:"))

