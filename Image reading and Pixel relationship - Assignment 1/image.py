import cv2

img = cv2.imread("/Users/veer/Desktop/image.jpg")

if img is None:
    print("Image was not found!")

else:
    cv2.imshow("Image ", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()