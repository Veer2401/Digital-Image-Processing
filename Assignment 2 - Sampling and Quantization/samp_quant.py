import numpy as np
import matplotlib.pyplot as plt 
from PIL import Image

image = Image.open("img.jpg").convert("L")
img = np.array(image)

def image_sampling(image, factor):
    sampled = image[::factor, ::factor]
    return sampled

def image_quantization(image,bits):
    levels = 2 ** bits

    step_size = 256 / levels

    quantization = np.floor(image /step_size) * step_size
    quantization = quantization.astype(np.uint8)

    return quantization

#sampling

sample2 = image_sampling(img,2)
sample4 = image_sampling(img,4)

#quantization

quant8 = image_quantization(img,8)
quant4 = image_quantization(img,4)
quant2 = image_quantization(img,2)

# Display Results

plt.figure(figsize=(14,8))

plt.subplot(2,3,1)
plt.imshow(img,cmap='gray')
plt.title("Original")
plt.axis('off')

plt.subplot(2,3,2)
plt.imshow(sample2,cmap='gray')
plt.title("Sampling Factor = 2")
plt.axis('off')

plt.subplot(2,3,3)
plt.imshow(sample4,cmap='gray')
plt.title("Sampling Factor = 4")
plt.axis('off')

plt.subplot(2,3,4)
plt.imshow(quant8,cmap='gray')
plt.title("8-bit Quantization")
plt.axis('off')

plt.subplot(2,3,5)
plt.imshow(quant4,cmap='gray')
plt.title("4-bit Quantization")
plt.axis('off')

plt.subplot(2,3,6)
plt.imshow(quant2,cmap='gray')
plt.title("2-bit Quantization")
plt.axis('off')

plt.tight_layout()
plt.show()