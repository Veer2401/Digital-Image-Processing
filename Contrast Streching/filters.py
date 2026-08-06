import numpy as np

image = []

print("Enter values for image: ")
for i in range(9):
    image.append(int(input()))

img = np.array(image).reshape(3,3)

def mean():
    mean = sum(image) / 9
    print("Mean:", mean)

def median():
    median = np.median(image)
    print("Median:", median)

def gaussian():
    gaussian = np.array([[1,2,1],
                         [2,4,2],
                         [1,2,1]])

    result = np.sum(img * gaussian) / 16
    print("Gaussian:", result)

def minimum():
    print("Minimum:", np.min(image))

def maximum():
    print("Maximum:", np.max(image))

def sobel():

    sx = np.array([[-1,0,1],
                   [-2,0,2],
                   [-1,0,1]])

    sy = np.array([[-1,-2,-1],
                   [0,0,0],
                   [1,2,1]])

    gx = np.sum(img * sx)
    gy = np.sum(img * sy)

    result = (gx**2 + gy**2) ** 0.5

    print("Horizontal =", gx)
    print("Vertical =", gy)
    print("Sobel =", result)

def prewitt():

    px = np.array([[-1,0,1],
                   [-1,0,1],
                   [-1,0,1]])

    py = np.array([[-1,-1,-1],
                   [0,0,0],
                   [1,1,1]])

    gx = np.sum(img * px)
    gy = np.sum(img * py)

    result = (gx**2 + gy**2) ** 0.5

    print("Horizontal =", gx)
    print("Vertical =", gy)
    print("Prewitt =", result)

while True:

    print("\n----- MENU -----")
    print("1. Mean")
    print("2. Median")
    print("3. Gaussian")
    print("4. Minimum")
    print("5. Maximum")
    print("6. Sobel")
    print("7. Prewitt")
    print("8. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        mean()

    elif choice == 2:
        median()

    elif choice == 3:
        gaussian()

    elif choice == 4:
        minimum()

    elif choice == 5:
        maximum()

    elif choice == 6:
        sobel()

    elif choice == 7:
        prewitt()

    elif choice == 8:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")