import numpy as np

# Input Matrix A
n = int(input("Enter size of Matrix A: "))

print("Enter Matrix A:")
A = np.array([list(map(int, input().split())) for _ in range(n)])

# Structuring Element B
m = int(input("\nEnter size of Structuring Element B: "))

print("Enter Structuring Element B:")
B = np.array([list(map(int, input().split())) for _ in range(m)])


def erosion(A, B):
    n = A.shape[0]
    m = B.shape[0]
    result = np.zeros((n, n), dtype=int)

    pad = m // 2
    A_padded = np.pad(A, pad, mode='constant', constant_values=0)

    for i in range(n):
        for j in range(n):
            part = A_padded[i:i+m, j:j+m]

            if np.all(part[B == 1] == 1):
                result[i, j] = 1

    return result


def dilation(A, B):
    n = A.shape[0]
    m = B.shape[0]
    result = np.zeros((n, n), dtype=int)

    pad = m // 2
    A_padded = np.pad(A, pad, mode='constant', constant_values=0)

    for i in range(n):
        for j in range(n):
            part = A_padded[i:i+m, j:j+m]

            if np.any(part[B == 1] == 1):
                result[i, j] = 1

    return result


while True:

    print("\n--- MENU ---")
    print("1. Erosion")
    print("2. Dilation")
    print("3. Opening")
    print("4. Closing")
    print("5. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        print("\nErosion:")
        print(erosion(A, B))

    elif ch == 2:
        print("\nDilation:")
        print(dilation(A, B))

    elif ch == 3:
        print("\nOpening:")
        print(dilation(erosion(A, B), B))

    elif ch == 4:
        print("\nClosing:")
        print(erosion(dilation(A, B), B))

    elif ch == 5:
        break

    else:
        print("Invalid choice")