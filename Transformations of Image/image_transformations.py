from PIL import Image
import matplotlib.pyplot as plt

image_path = "horse.jpg"

image = Image.open(image_path)
resize = image.resize((300,300))
crop = image.crop((50,50,1100,1100))
flip = image.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
rotate = image.rotate(90)

plt.figure(figsize= (12,8))

plt.subplot(2,3,1)
plt.imshow(image)
plt.title("Original")
plt.axis("off")

plt.subplot(2,3,2)
plt.imshow(resize)
plt.title("Resized")
plt.axis("off")

plt.subplot(2,3,3)
plt.imshow(crop)
plt.title("Cropped")
plt.axis("off")

plt.subplot(2,3,4)
plt.imshow(flip)
plt.title("Flipped")
plt.axis("off")

plt.subplot(2,3,5)
plt.imshow(rotate)
plt.title("Rotated")
plt.axis("off")

plt.tight_layout()
plt.show()
