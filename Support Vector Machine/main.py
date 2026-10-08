import numpy as np
import matplotlib.pyplot as plt

# Dataset
X = np.array([
    [1, 2],
    [2, 3],
    [2, 4],
    [3, 3],
    [3, 5],
    [4, 4],

    [6, 1],
    [7, 2],
    [7, 3],
    [8, 2],
    [8, 4],
    [9, 3]
])

y = np.array([
    -1, -1, -1, -1, -1, -1,
     1,  1,  1,  1,  1,  1
])


# Train SVM
def train_svm(X, y):
    w = np.zeros(2)
    b = 0

    for epoch in range(1000):
        for i in range(len(X)):

            if y[i] * (np.dot(X[i], w) + b) < 1:
                w = w - 0.001 * (0.02 * w - y[i] * X[i])
                b = b + 0.001 * y[i]
            else:
                w = w - 0.001 * 0.02 * w

    return w, b


# Train
w, b = train_svm(X, y)

print("Weights:", w)
print("Bias:", b)


# Prediction
prediction = np.sign(np.dot(X, w) + b)

print("\nActual Labels:")
print(y)

print("\nPredicted Labels:")
print(prediction)


# Accuracy
accuracy = np.mean(prediction == y) * 100

print("\nAccuracy:", accuracy, "%")


# Plot
plt.scatter(X[y == -1, 0], X[y == -1, 1], label="Class -1")
plt.scatter(X[y == 1, 0], X[y == 1, 1], label="Class +1")

x = np.linspace(0, 10, 100)
line = -(w[0] * x + b) / w[1]

plt.plot(x, line, label="Decision Boundary")

plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.title("Linear SVM")
plt.legend()
plt.grid()
plt.show()