import numpy as np

gray_level = np.arange(8)

pixels = np.array([0,8,8,2,0,7,0,0])
total_pixels = sum(pixels)

pdf = pixels / total_pixels
cdf = np.cumsum(pdf)
skx7 = cdf * 7

histogram_level = np.round(skx7).astype(int)

print("Gray\tPixels\tPDF\tCDF\tNew Level")
for i in range(8):
    print(f"{gray_level[i]}\t{pixels[i]}\t{pdf[i]:.2f}\t{cdf[i]:.2f}\t{histogram_level[i]}")