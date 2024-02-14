import cv2

img1 = cv2.imread('/home/reny/Downloads/lemur.png')
img2 = cv2.imread('/home/reny/Downloads/flag.png')

xor_img = cv2.bitwise_xor(img1, img2)

cv2.imshow('Bitwise XOR Image', xor_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
