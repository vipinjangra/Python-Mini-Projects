# import library
import cv2

# image reading
img = cv2.imread("python.jpg")

# image outlines
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5)
outlines = cv2.adaptiveThreshold(gray, 255,
                                 cv2.ADAPTIVE_THRESH_MEAN_C,
                                 cv2.THRESH_BINARY, 9, 9)

# make cartoon of your image
color = cv2.bilateralFilter(img, 9, 250, 250)
cartoon = cv2.bitwise_and(color, color, mask=outlines)

cv2.imshow("Original Image", img)
cv2.imshow("Outlines", outlines)
cv2.imshow("Cartoon", cartoon)
cv2.waitKey(0)
cv2.destroyAllWindows()
