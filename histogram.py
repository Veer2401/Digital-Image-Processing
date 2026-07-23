import numpy as np
import matplotlib.pyplot as plt

gray_level = np.arange(8)

pixels = []

print("Enter number of pixels: ")

for i in range(len(gray_level)):
    value = int(input(f"Gray level {gray_level[i]}: "))
    pixels.append(value)

total_pixels = sum(pixels)

pdf = []

for i in range(len(pixels)):
    pdf.append(pixels[i] / total_pixels)

cdf = []
cumulative = 0

for i in range(len(pdf)):
    cumulative += pdf[i]
    cdf.append(cumulative)


skx7 = []

for i in range(len(cdf)):
    skx7.append(cdf[i] * 7)

histogram_levels = []
for i in range(len(skx7)):
    histogram_levels.append(round(skx7[i]))


print("\nGray\tPixels\tPDF\tCDF\tSk×7\tNew Level")

for i in range(len(gray_level)):
    print(f"{gray_level[i]}\t{pixels[i]}\t{pdf[i]:.2f}\t{cdf[i]:.2f}\t{skx7[i]:.2f}\t{histogram_levels[i]}")


original_histogram = []

for i in range(len(gray_level)):
    for j in range(pixels[i]):
        original_histogram.append(gray_level[i])

new_histogram = []

for i in range(len(histogram_levels)):
    for j in range(pixels[i]):
        new_histogram.append(histogram_levels[i])


#original histogram

plt.hist(original_histogram, bins=8, range=(0,8), edgecolor='green')
plt.title("Original Histogram")
plt.xlabel("Gray Level")
plt.ylabel("Number of pixels")
plt.show()

#new histogram

plt.hist(new_histogram, bins=8, range=(0,8), edgecolor='black')
plt.title("New Histogram")
plt.xlabel("Gray Level")
plt.ylabel("Number of pixels")
plt.show()




