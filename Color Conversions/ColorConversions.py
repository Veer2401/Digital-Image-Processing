from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img_path = "/Users/veer/Desktop/image.jpg"

image = Image.open(img_path).convert("RGB")

rgb = np.array(image)

r = rgb[:, :, 0]
g = rgb[:, :, 1]
b = rgb[:, :, 2]

R = 0.299 * r
G = 0.587 * g
B = 0.114 * b

gray = R + G + B

gray = np.uint8(gray)

R_prime = r / 255.0
G_prime = g / 255.0
B_prime = b / 255.0

Cmax = np.maximum(np.maximum(R_prime, G_prime), B_prime)

Cmin = np.minimum(np.minimum(R_prime, G_prime), B_prime)

delta = Cmax - Cmin

H = np.zeros_like(Cmax)

mask = delta != 0

red_mask = (Cmax == R_prime) & mask

H[red_mask] = 60 * (
    ((G_prime[red_mask] - B_prime[red_mask]) /
     delta[red_mask]) % 6
)

green_mask = (Cmax == G_prime) & mask

H[green_mask] = 60 * (
    ((B_prime[green_mask] - R_prime[green_mask]) /
     delta[green_mask]) + 2
)

blue_mask = (Cmax == B_prime) & mask

H[blue_mask] = 60 * (
    ((R_prime[blue_mask] - G_prime[blue_mask]) /
     delta[blue_mask]) + 4
)

S = np.zeros_like(Cmax)

non_zero = Cmax != 0

S[non_zero] = delta[non_zero] / Cmax[non_zero]

V = Cmax

H_display = np.uint8(H / 360 * 255)

S_display = np.uint8(S * 255)

V_display = np.uint8(V * 255)

hsv = np.stack(
    (H_display, S_display, V_display),
    axis=2
)

plt.figure(figsize=(12, 5))

plt.subplot(1, 3, 1)

plt.imshow(rgb)

plt.title("Original RGB")

plt.axis("off")

plt.subplot(1, 3, 2)

plt.imshow(gray, cmap="gray")

plt.title("Grayscale")

plt.axis("off")

plt.subplot(1, 3, 3)

plt.imshow(hsv)

plt.title("HSV")

plt.axis("off")

plt.tight_layout()

plt.show()