import numpy as np

# 1. CONTOUR DETECTION

def contour_detection(matrix):

    print("\n---------- CONTOUR DETECTION ----------")
    print("1. Sobel")
    print("2. Prewitt")
    print("---------------------------------------")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        Gx = np.array([
            [-1, 0, 1],
            [-2, 0, 2],
            [-1, 0, 1]
        ])

        Gy = np.array([
            [-1, -2, -1],
            [0, 0, 0],
            [1, 2, 1]
        ])

        gx = 0
        gy = 0

        for i in range(3):
            for j in range(3):
                gx = gx + matrix[i][j] * Gx[i][j]
                gy = gy + matrix[i][j] * Gy[i][j]

        magnitude = np.sqrt(gx ** 2 + gy ** 2)

        result = np.zeros((3, 3), dtype=int)

        result[1][1] = int(magnitude)

        print("\nOriginal Matrix:")
        print(matrix)

        print("\nSobel Gx Kernel:")
        print(Gx)

        print("\nSobel Gy Kernel:")
        print(Gy)

        print("\nGx =", gx)
        print("Gy =", gy)

        print("\nGradient Magnitude =", magnitude)

        print("\nSobel Contour Result:")
        print(result)

    elif choice == 2:

        Gx = np.array([
            [-1, 0, 1],
            [-1, 0, 1],
            [-1, 0, 1]
        ])

        Gy = np.array([
            [-1, -1, -1],
            [0, 0, 0],
            [1, 1, 1]
        ])

        gx = 0
        gy = 0

        for i in range(3):
            for j in range(3):
                gx = gx + matrix[i][j] * Gx[i][j]
                gy = gy + matrix[i][j] * Gy[i][j]

        magnitude = np.sqrt(gx ** 2 + gy ** 2)

        result = np.zeros((3, 3), dtype=int)

        result[1][1] = int(magnitude)

        print("\nOriginal Matrix:")
        print(matrix)

        print("\nPrewitt Gx Kernel:")
        print(Gx)

        print("\nPrewitt Gy Kernel:")
        print(Gy)

        print("\nGx =", gx)
        print("Gy =", gy)

        print("\nGradient Magnitude =", magnitude)

        print("\nPrewitt Contour Result:")
        print(result)

    else:
        print("\nInvalid choice. Please enter 1 or 2.")


# 2. WATERSHED SEGMENTATION

def watershed_segmentation(matrix):

    threshold = float(
        input("\nEnter region growing threshold: ")
    )

    center = matrix[1][1]

    result = np.zeros((3, 3), dtype=int)

    result[1][1] = 255

    top_difference = abs(matrix[0][1] - center)
    bottom_difference = abs(matrix[2][1] - center)
    left_difference = abs(matrix[1][0] - center)
    right_difference = abs(matrix[1][2] - center)

    if top_difference <= threshold:
        result[0][1] = 255

    if bottom_difference <= threshold:
        result[2][1] = 255

    if left_difference <= threshold:
        result[1][0] = 255

    if right_difference <= threshold:
        result[1][2] = 255

    print("\nOriginal Matrix:")
    print(matrix)

    print("\nCenter Pixel =", center)

    print("\nTop Difference =", top_difference)
    print("Bottom Difference =", bottom_difference)
    print("Left Difference =", left_difference)
    print("Right Difference =", right_difference)

    print("\nRegion Growing Threshold =", threshold)

    print("\nWatershed Segmentation Result:")
    print(result)


# INPUT 3x3 MATRIX

matrix = np.zeros((3, 3), dtype=int)

print("Enter the 3x3 matrix values:")

for i in range(3):
    for j in range(3):
        matrix[i][j] = int(
            input(f"Enter value [{i}][{j}]: ")
        )


# MAIN MENU

while True:

    print("\n======================================")
    print("       IMAGE SEGMENTATION MENU")
    print("======================================")
    print("1. Contour Detection")
    print("2. Watershed Segmentation")
    print("3. Exit")
    print("======================================")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        contour_detection(matrix)

    elif choice == 2:

        watershed_segmentation(matrix)

    elif choice == 3:

        print("\nProgram ended.")
        break

    else:

        print("\nInvalid choice. Please enter 1 to 3.")