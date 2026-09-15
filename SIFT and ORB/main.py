import numpy as np
import matplotlib.pyplot as plt

# image path
file1 = "/Users/veer/Desktop/image1.jpeg"
file2 = "/Users/veer/Desktop/image2.jpeg"

def read_image(file):
    img = plt.imread(file)

    if img.ndim == 3:
        img = np.mean(img[:, :, :3], axis=2)

    if img.max() <= 1:
        img = img * 255

    return img


# sift
def sift(img):
    blur = np.zeros_like(img)
    p = np.pad(img, 2, mode="edge")

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            blur[i, j] = np.mean(p[i:i+5, j:j+5])

    dog = img - blur
    points = []

    for i in range(1, img.shape[0]-1):
        for j in range(1, img.shape[1]-1):
            if abs(dog[i,j]) > 10:
                points.append((i,j))

    return points


def sift_desc(img, points):
    desc = []

    for x, y in points:
        gx = img[x, y+1] - img[x, y-1]
        gy = img[x+1, y] - img[x-1, y]
        desc.append([gx, gy])

    return np.array(desc)


# orb
def orb(img):
    points = []

    for i in range(1, img.shape[0]-1):
        for j in range(1, img.shape[1]-1):

            c = img[i,j]

            n = [
                img[i-1,j], img[i+1,j],
                img[i,j-1], img[i,j+1]
            ]

            if sum(abs(x-c) > 20 for x in n) >= 3:
                points.append((i,j))

    return points


def orb_desc(img, points):
    desc = []

    for x, y in points:
        block = img[x-1:x+2, y-1:y+2]
        desc.append(block.flatten() > block.mean())

    return np.array(desc)


def match(p1, p2, d1, d2, method):

    matches = []

    for i in range(len(d1)):

        if method == "SIFT":
            distance = np.linalg.norm(d2-d1[i], axis=1)
        else:
            distance = np.sum(d2 != d1[i], axis=1)

        j = np.argmin(distance)
        matches.append((p1[i], p2[j], distance[j]))

    return matches


def show(img1, img2, matches, title):

    w = img1.shape[1]

    out = np.zeros(
        (max(img1.shape[0], img2.shape[0]),
         img1.shape[1] + img2.shape[1])
    )

    out[:img1.shape[0], :img1.shape[1]] = img1
    out[:img2.shape[0], w:] = img2

    plt.imshow(out, cmap="gray")

    for a, b, d in matches:
        plt.plot(
            [a[1], b[1] + w],
            [a[0], b[0]]
        )

    plt.title(title)
    plt.axis("off")
    plt.show()


# main
img1 = read_image(file1)
img2 = read_image(file2)

print("1. SIFT")
print("2. ORB")
print("3. Both")

choice = int(input("Enter choice: "))


if choice == 1 or choice == 3:

    p1 = sift(img1)
    p2 = sift(img2)

    d1 = sift_desc(img1, p1)
    d2 = sift_desc(img2, p2)

    m = match(p1, p2, d1, d2, "SIFT")

    print("SIFT keypoints:", len(p1), len(p2))
    print("SIFT correspondences:", len(m))

    show(img1, img2, m, "SIFT Correspondences")


if choice == 2 or choice == 3:

    p1 = orb(img1)
    p2 = orb(img2)

    d1 = orb_desc(img1, p1)
    d2 = orb_desc(img2, p2)

    m = match(p1, p2, d1, d2, "ORB")

    print("ORB keypoints:", len(p1), len(p2))
    print("ORB correspondences:", len(m))

    show(img1, img2, m, "ORB Correspondences")