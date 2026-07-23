import cv2

img = cv2.imread("/Users/veer/Desktop/image.jpg")

if img is None:
    print("Image was not found!")

else:
    cv2.imshow("Image ", img)
    cv2.imwrite

     # Save the image
    output_path = "/Users/veer/Desktop/saved_image.jpg"
    cv2.imwrite(output_path, img)

    print("Image saved successfully at:")
    print(output_path)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
