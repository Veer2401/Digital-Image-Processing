import tensorflow as tf
from tensorflow.keras import datasets, models, layers
import matplotlib.pyplot as plt

(x_train, y_train), (x_test, y_test) = datasets.mnist.load_data()

print("Training images:", x_train.shape)
print("Testing images:", x_test.shape)


x_train = x_train / 255.0
x_test = x_test / 255.0

# creating the feed forward network
model = models.Sequential([
    layers.Flatten(input_shape=(28, 28)),
    layers.Dense(128, activation='relu'),
    layers.Dense(10, activation='softmax')
])

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)


model.summary()

model.fit(x_train, y_train, epochs=5, batch_size=32)

test_loss, test_accuracy = model.evaluate(x_test, y_test)

print("Test Loss:", test_loss)
print("Test Accuracy:", test_accuracy * 100, "%")

#testing 5 images
predictions = model.predict(x_test[:5])

for i in range(5):
    print("Image", i + 1)
    print("Actual Digit:", y_test[i])
    print("Predicted Digit:", predictions[i].argmax())
    print()

# Display the five handwritten images
plt.figure(figsize=(12, 4))

for i in range(5):
    plt.subplot(1, 5, i + 1)
    plt.imshow(x_test[i], cmap='gray')
    plt.title(
        "Actual: " + str(y_test[i]) +
        "\nPredicted: " + str(predictions[i].argmax())
    )
    plt.axis('off')

plt.tight_layout()
plt.show()
