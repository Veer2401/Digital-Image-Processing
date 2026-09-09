import numpy as np

# manual 
def manual_threshold(matrix):

    T = int(input("\nEnter threshold value: "))

    pixels = matrix.flatten()

    result = np.zeros(9, dtype=int)

    for i in range(9):

        if pixels[i] >= T:
            result[i] = 255
        else:
            result[i] = 0

    result = result.reshape(3, 3)

    print("\nOriginal Matrix:")
    print(matrix)

    print("\n1D Array:")
    print(pixels)

    print("\nThreshold T =", T)

    print("\nManual Thresholding Result:")
    print(result)


# otsu
def otsu_threshold(matrix):

    pixels = matrix.flatten()

    N = len(pixels)

    max_variance = -1
    best_threshold = 0

    for t in range(256):

        C0 = pixels[pixels <= t]
        C1 = pixels[pixels > t]

        if len(C0) == 0 or len(C1) == 0:
            continue

        omega0 = len(C0) / N
        omega1 = len(C1) / N

        sum0 = np.sum(C0)
        sum1 = np.sum(C1)

        mu0 = sum0 / len(C0)
        mu1 = sum1 / len(C1)

        between_class_variance = (
            omega0 * omega1 * (mu0 - mu1) ** 2
        )

        if between_class_variance > max_variance:

            max_variance = between_class_variance
            best_threshold = t

    result = np.zeros(9, dtype=int)

    for i in range(9):

        if pixels[i] > best_threshold:
            result[i] = 255
        else:
            result[i] = 0

    result = result.reshape(3, 3)

    print("\nOriginal Matrix:")
    print(matrix)

    print("\n1D Array:")
    print(pixels)

    print("\nOtsu Threshold =", best_threshold)

    print("\nMaximum Between-Class Variance =", max_variance)

    print("\nOtsu Thresholding Result:")
    print(result)


# mean adaptive
def adaptive_mean_threshold(matrix):

    C = 5

    result = np.zeros((3, 3), dtype=int)

    for i in range(3):
        for j in range(3):

            window = []

            for x in range(i - 1, i + 2):
                for y in range(j - 1, j + 2):

                    if 0 <= x < 3 and 0 <= y < 3:
                        window.append(matrix[x][y])

            window = np.array(window)

            local_mean = np.mean(window)

            local_threshold = local_mean - C

            if matrix[i][j] >= local_threshold:
                result[i][j] = 255
            else:
                result[i][j] = 0

    print("\nOriginal Matrix:")
    print(matrix)

    print("\nC =", C)

    print("\nAdaptive Mean Thresholding Result:")
    print(result)


# input 3x3 matrix
matrix = np.zeros((3, 3), dtype=int)

print("Enter the 3x3 matrix values:")

for i in range(3):
    for j in range(3):
        matrix[i][j] = int(
            input(f"Enter value [{i}][{j}]: ")
        )


# menu
while True:

    print("\n==============================")
    print("       THRESHOLDING MENU")
    print("==============================")
    print("1. Manual Thresholding")
    print("2. Otsu Thresholding")
    print("3. Adaptive Mean Thresholding")
    print("4. Exit")
    print("==============================")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        manual_threshold(matrix)

    elif choice == 2:

        otsu_threshold(matrix)

    elif choice == 3:

        adaptive_mean_threshold(matrix)

    elif choice == 4:

        print("\nProgram ended.")
        break

    else:

        print("\nInvalid choice. Please enter 1, 2, 3 or 4.")