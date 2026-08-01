from PIL import Image

# Input image path
image_path = r"C:\Users\Student\Desktop\tiger.jpg"

# Resize Image
def resize_image(size):
    image = Image.open(image_path)
    resized_image = image.resize(size)

    output_path = r"C:\Users\Student\Desktop\resized.jpg"
    resized_image.save(output_path)

    print("Image resized and saved to:", output_path)


# Crop Image
def crop_image(crop_box):
    image = Image.open(image_path)
    cropped_image = image.crop(crop_box)

    output_path = r"C:\Users\Student\Desktop\cropped.jpg"
    cropped_image.save(output_path)

    print("Image cropped and saved to:", output_path)


# Flip Image
def flip_image(direction):
    image = Image.open(image_path)

    if direction.lower() == "horizontal":
        flipped_image = image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)

    elif direction.lower() == "vertical":
        flipped_image = image.transpose(Image.Transpose.FLIP_TOP_BOTTOM)

    else:
        print("Direction should be either 'horizontal' or 'vertical'.")
        return

    output_path = r"C:\Users\Student\Desktop\flipped.jpg"
    flipped_image.save(output_path)

    print("Image flipped and saved to:", output_path)


# Rotate Image
def rotate_image(angle):
    image = Image.open(image_path)
    rotated_image = image.rotate(angle)

    output_path = r"C:\Users\Student\Desktop\rotated.jpg"
    rotated_image.save(output_path)

    print("Image rotated and saved to:", output_path)


# Function Calls
resize_image((100, 300))
crop_image((50, 50, 1100, 1100))
flip_image("vertical")
rotate_image(90)