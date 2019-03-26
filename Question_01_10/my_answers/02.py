import cv2
import numpy as np

img = cv2.imread("../imori.jpg").astype(np.float)
b = img[:, :, 0].copy()
g = img[:, :, 1].copy()
r = img[:, :, 2].copy()

out = 0.2126 * r + 0.7152 * g + 0.0722 * b
out = out.astype(np.uint8)

cv2.imwrite("out_02.jpg", out)
cv2.imshow("result", out)
cv2.waitKey(0)
cv2.destroyAllWindows()