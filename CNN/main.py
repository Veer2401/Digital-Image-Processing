import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
from tensorflow.keras import layers, models

# loading cifar dataset
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()

# object names
class_names = [
    "Airplane", "Automobile", "Bird", "Cat", "Deer",
    "Dog", "Frog", "Horse", "Ship", "Truck"
]

print("Dataset: CIFAR-10")
print("Original training images:", len(x_train))
print("Testing images:", len(x_test))
print("Number of classes:", len(class_names))

# reducing training dataset to save time
x_train = x_train[:10000]
y_train = y_train[:10000]

print("Images used for training and validation:", len(x_train))

# normalizing pixel values
x_train = x_train.astype("float32") / 255.0
x_test = x_test.astype("float32") / 255.0

# cnn process
model = models.Sequential([
    # Input layer for 32x32 colored images
    layers.Input(shape=(32, 32, 3)),

    layers.Conv2D(32, (3, 3), activation="relu"),
    layers.MaxPooling2D((2, 2)),

    layers.Conv2D(64, (3, 3), activation="relu"),
    layers.MaxPooling2D((2, 2)),

    layers.Conv2D(128, (3, 3), activation="relu"),

    layers.Flatten(),
    layers.Dense(128, activation="relu"),

    layers.Dense(10, activation="softmax")
])

model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

model.summary()

# training the cnn model
history = model.fit(
    x_train,
    y_train,
    epochs=5,
    batch_size=64,
    validation_split=0.1
)

# evaluating model performance
test_loss, test_accuracy = model.evaluate(x_test, y_test)

print("\nModel Performance")
print("Test Loss:", test_loss)
print("Test Accuracy:", test_accuracy * 100, "%")

# predicting classes for five test images
predictions = model.predict(x_test[:5])

plt.figure(figsize=(12, 5))

for i in range(5):
    actual_label = int(y_test[i][0])
    predicted_label = int(np.argmax(predictions[i]))

    plt.subplot(1, 5, i + 1)
    plt.imshow(x_test[i])

    plt.title(
        "Actual: " + class_names[actual_label] +
        "\nPredicted: " + class_names[predicted_label],
        fontsize=9
    )

    plt.axis("off")

plt.tight_layout()
plt.show()

# plotting training and validation accuracy
plt.figure(figsize=(8, 5))

plt.plot(history.history["accuracy"], label="Training Accuracy")
plt.plot(history.history["val_accuracy"], label="Validation Accuracy")

plt.title("CNN Training and Validation Accuracy")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.legend()
plt.grid(True)
plt.show()

# plotting training and validation loss
plt.figure(figsize=(8, 5))

plt.plot(history.history["loss"], label="Training Loss")
plt.plot(history.history["val_loss"], label="Validation Loss")

plt.title("CNN Training and Validation Loss")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.legend()
plt.grid(True)
plt.show()