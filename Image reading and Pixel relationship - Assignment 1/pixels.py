import numpy as n

image = n.array([
    [10,23,54,90,67],
    [67,44,55,67,21],
    [9,51,32,99,85],
    [10,20,40,65,88],
    [27,44,49,76,39],
])

print("Matrix of image: ")
print(image)

#center pixel
x,y = 2,2

print("Center pixel: ")
print(f"Position {x},{y}")
print(f"Value: {image[x,y]}")

#4-neighbourhood
n4 = [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]

#diagonal pixels
nd = [(x-1,y-1),(x-1,y+1),(x+1,y-1),(x+1,y+1)]

#8-neighbourhood
n8 = n4+nd

print("4 Neighbours: ")

for i,j in n4:
    print(f"{i},{j} = {image[i,j]}")

print("\n")
print("Diagonal pixels: ")

for i,j in nd:
    print(f"{i},{j} = {image[i,j]}")

print("\n")
print("8 neighbourhood ")

for i,j in n8:
    print(f"{i},{j} = {image[i,j]}")

print("\n")