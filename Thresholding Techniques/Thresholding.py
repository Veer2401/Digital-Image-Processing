import numpy as np


# 1. manual

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


# 2. otsu


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


# 3. iterative


def iterative_threshold(matrix):

    pixels = matrix.flatten()

    T = np.mean(pixels)

    while True:

        C0 = pixels[pixels <= T]
        C1 = pixels[pixels > T]

        if len(C0) == 0 or len(C1) == 0:
            break

        mu0 = np.mean(C0)
        mu1 = np.mean(C1)

        new_T = (mu0 + mu1) / 2

        if new_T == T:
            break

        T = new_T

    result = np.zeros(9, dtype=int)

    for i in range(9):

        if pixels[i] > T:
            result[i] = 255
        else:
            result[i] = 0

    result = result.reshape(3, 3)

    print("\nOriginal Matrix:")
    print(matrix)

    print("\n1D Array:")
    print(pixels)

    print("\nIterative Threshold =", T)

    print("\nIterative Global Thresholding Result:")
    print(result)

# 4. mean 


def adaptive_mean_threshold(matrix):

    C = float(input("\nEnter C value: "))

    result = np.zeros((3, 3), dtype=int)

    for i in range(3):
        for j in range(3):

            total = 0
            count = 0

            # Calculate local sum directly
            for x in range(i - 1, i + 2):
                for y in range(j - 1, j + 2):

                    if 0 <= x < 3 and 0 <= y < 3:

                        total = total + matrix[x][y]
                        count = count + 1

            # Local Mean = Sum / Total Pixels
            mean = total / count

            # T(x,y) = Mean - C
            T = mean - C

            if matrix[i][j] >= T:
                result[i][j] = 255
            else:
                result[i][j] = 0

    print("\nOriginal Matrix:")
    print(matrix)

    print("\nC =", C)

    print("\nAdaptive Mean Thresholding Result:")
    print(result)



# 5. gaussian


def adaptive_gaussian_threshold(matrix):

    # Standard 3 x 3 Gaussian Kernel
    kernel = np.array([
        [1, 2, 1],
        [2, 4, 2],
        [1, 2, 1]
    ])

    result = np.zeros((3, 3), dtype=int)

    for i in range(3):
        for j in range(3):

            weighted_sum = 0
            weight_sum = 0

            for x in range(i - 1, i + 2):
                for y in range(j - 1, j + 2):

                    if 0 <= x < 3 and 0 <= y < 3:

                        kx = x - i + 1
                        ky = y - j + 1

                        weight = kernel[kx][ky]

                        weighted_sum = (
                            weighted_sum +
                            matrix[x][y] * weight
                        )

                        weight_sum = weight_sum + weight

            # Gaussian weighted mean
            T = weighted_sum / weight_sum

            if matrix[i][j] >= T:
                result[i][j] = 255
            else:
                result[i][j] = 0

    print("\nOriginal Matrix:")
    print(matrix)

    print("\nGaussian Kernel:")
    print(kernel)

    print("\nAdaptive Gaussian Thresholding Result:")
    print(result)


# 6. niblack


def niblack_threshold(matrix):

    k = float(input("\nEnter k value: "))

    result = np.zeros((3, 3), dtype=int)

    for i in range(3):
        for j in range(3):

            total = 0
            count = 0

            # Calculate local sum
            for x in range(i - 1, i + 2):
                for y in range(j - 1, j + 2):

                    if 0 <= x < 3 and 0 <= y < 3:

                        total = total + matrix[x][y]
                        count = count + 1

            # Local Mean
            mean = total / count

            # Calculate SD directly
            variance_sum = 0

            for x in range(i - 1, i + 2):
                for y in range(j - 1, j + 2):

                    if 0 <= x < 3 and 0 <= y < 3:

                        variance_sum = (
                            variance_sum +
                            (matrix[x][y] - mean) ** 2
                        )

            sd = np.sqrt(variance_sum / count)

            # Niblack formula
            T = mean + k * sd

            if matrix[i][j] >= T:
                result[i][j] = 255
            else:
                result[i][j] = 0

    print("\nOriginal Matrix:")
    print(matrix)

    print("\nk =", k)

    print("\nNiblack Thresholding Result:")
    print(result)



# 7. sauvola


def sauvola_threshold(matrix):

    k = float(input("\nEnter k value: "))

    R = float(input("\nEnter R value: "))

    result = np.zeros((3, 3), dtype=int)

    for i in range(3):
        for j in range(3):

            total = 0
            count = 0

            # Calculate local sum
            for x in range(i - 1, i + 2):
                for y in range(j - 1, j + 2):

                    if 0 <= x < 3 and 0 <= y < 3:

                        total = total + matrix[x][y]
                        count = count + 1

            # Local Mean
            mean = total / count

            # Calculate SD directly
            variance_sum = 0

            for x in range(i - 1, i + 2):
                for y in range(j - 1, j + 2):

                    if 0 <= x < 3 and 0 <= y < 3:

                        variance_sum = (
                            variance_sum +
                            (matrix[x][y] - mean) ** 2
                        )

            sd = np.sqrt(variance_sum / count)

            # Sauvola formula
            T = mean * (1 + k * (sd / R - 1))

            if matrix[i][j] >= T:
                result[i][j] = 255
            else:
                result[i][j] = 0

    print("\nOriginal Matrix:")
    print(matrix)

    print("\nk =", k)

    print("R =", R)

    print("\nSauvola Thresholding Result:")
    print(result)


# =========================================================
# INPUT 3 x 3 MATRIX
# =========================================================

matrix = np.zeros((3, 3), dtype=int)

print("Enter the 3x3 matrix values:")

for i in range(3):
    for j in range(3):

        matrix[i][j] = int(
            input(f"Enter value [{i}][{j}]: ")
        )


# =========================================================
# MAIN MENU
# =========================================================

while True:

    print("\n======================================")
    print("          THRESHOLDING MENU")
    print("======================================")
    print("1. Global Thresholding")
    print("2. Adaptive Thresholding")
    print("3. Exit")
    print("======================================")

    choice = int(input("Enter your choice: "))


    # =====================================================
    # GLOBAL MENU
    # =====================================================

    if choice == 1:

        while True:

            print("\n---------- GLOBAL THRESHOLDING ----------")
            print("1. Manual Thresholding")
            print("2. Otsu Thresholding")
            print("3. Iterative Global Thresholding")
            print("4. Back")
            print("-----------------------------------------")

            sub_choice = int(input("Enter your choice: "))

            if sub_choice == 1:

                manual_threshold(matrix)

            elif sub_choice == 2:

                otsu_threshold(matrix)

            elif sub_choice == 3:

                iterative_threshold(matrix)

            elif sub_choice == 4:

                break

            else:

                print("\nInvalid choice. Please enter 1 to 4.")


    # =====================================================
    # ADAPTIVE MENU
    # =====================================================

    elif choice == 2:

        while True:

            print("\n---------- ADAPTIVE THRESHOLDING ----------")
            print("1. Mean Thresholding")
            print("2. Gaussian Thresholding")
            print("3. Niblack Thresholding")
            print("4. Sauvola Thresholding")
            print("5. Back")
            print("-------------------------------------------")

            sub_choice = int(input("Enter your choice: "))

            if sub_choice == 1:

                adaptive_mean_threshold(matrix)

            elif sub_choice == 2:

                adaptive_gaussian_threshold(matrix)

            elif sub_choice == 3:

                niblack_threshold(matrix)

            elif sub_choice == 4:

                sauvola_threshold(matrix)

            elif sub_choice == 5:

                break

            else:

                print("\nInvalid choice. Please enter 1 to 5.")


    # =====================================================
    # EXIT
    # =====================================================

    elif choice == 3:

        print("\nProgram ended.")
        break

    else:

        print("\nInvalid choice. Please enter 1, 2 or 3.")
