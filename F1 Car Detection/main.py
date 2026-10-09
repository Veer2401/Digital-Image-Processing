
import cv2
import glob
import os
import numpy as np

from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_score, recall_score

# 1. Load and preprocess training images

X, y = [], []

for folder, label in [
    ("data/car", 1),
    ("data/background", 0)
]:
    paths = []

    for ext in ("jpg", "jpeg", "png", "JPG", "JPEG", "PNG"):
        paths.extend(glob.glob(os.path.join(folder, f"*.{ext}")))

    for path in paths:
        img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

        if img is not None:
            X.append(cv2.resize(img, (96, 48)))
            y.append(label)
        else:
            print("Could not read:", path)

print("Car training images:", y.count(1))
print("Background training images:", y.count(0))

if y.count(1) < 2 or y.count(0) < 2:
    raise ValueError("Need at least 2 training images per class.")

# 2. Split the dataset

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.33,
    random_state=42,
    stratify=y
)

# 3. Compare four HOG configurations

configurations = [
    (4, 9),
    (8, 9),
    (8, 6),
    (8, 12)
]

print("\nHOG Parameter Comparison")

for cell, bins in configurations:
    hog_test = cv2.HOGDescriptor(
        (96, 48),
        (2 * cell, 2 * cell),
        (cell, cell),
        (cell, cell),
        bins
    )

    train_features = np.array([
        np.asarray(hog_test.compute(img)).flatten()
        for img in X_train
    ])

    test_features = np.array([
        np.asarray(hog_test.compute(img)).flatten()
        for img in X_test
    ])

    clf = LinearSVC(
        C=1.0,
        class_weight="balanced",
        max_iter=10000,
        random_state=42
    )

    clf.fit(train_features, y_train)
    predictions = clf.predict(test_features)

    TP = sum(a == 1 and b == 1 for a, b in zip(y_test, predictions))
    TN = sum(a == 0 and b == 0 for a, b in zip(y_test, predictions))
    FP = sum(a == 0 and b == 1 for a, b in zip(y_test, predictions))
    FN = sum(a == 1 and b == 0 for a, b in zip(y_test, predictions))

    precision = precision_score(y_test, predictions, zero_division=0)
    recall = recall_score(y_test, predictions, zero_division=0)

    f1 = (
        2 * precision * recall / (precision + recall)
        if precision + recall > 0 else 0
    )

    error_rate = (FP + FN) / len(y_test)

    print(f"\nCell size: {cell}x{cell}, Bins: {bins}")
    print(f"TP={TP}, TN={TN}, FP={FP}, FN={FN}")
    print(f"Precision: {precision:.3f}")
    print(f"Recall: {recall:.3f}")
    print(f"F1-score: {f1:.3f}")
    print(f"Error rate: {error_rate:.3f}")

# 4. Train the final HOG and SVM model

hog = cv2.HOGDescriptor(
    (96, 48),
    (16, 16),
    (8, 8),
    (8, 8),
    9
)

train_features = np.array([
    np.asarray(hog.compute(img)).flatten()
    for img in X_train
])

model = LinearSVC(
    C=1.0,
    class_weight="balanced",
    max_iter=10000,
    random_state=42
)

model.fit(train_features, y_train)

# 5. Set the classification threshold

# This threshold must be validated on separate labelled images.
# A higher threshold reduces positive predictions but may miss cars.
threshold = 0.5

# 6. Classify both test images

test_images = [
    "data/test_images/car1.jpg",
    "data/test_images/background2.jpg"
]

os.makedirs("results", exist_ok=True)

for image_path in test_images:
    image = cv2.imread(image_path)

    if image is None:
        print("Could not load:", os.path.abspath(image_path))
        continue

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.resize(gray, (96, 48))

    feature = np.asarray(hog.compute(gray)).reshape(1, -1)
    score = float(model.decision_function(feature)[0])

    prediction = 1 if score > threshold else 0

    if prediction == 1:
        label = "F1 Car Detected"
        color = (0, 255, 0)
    else:
        label = "No Car Detected"
        color = (0, 0, 255)

    print("\nTest image:", os.path.abspath(image_path))
    print("Prediction value:", prediction)
    print("SVM score:", round(score, 4))
    print("Prediction:", label)

    cv2.putText(
        image,
        label,
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        color,
        2
    )

    output_name = os.path.splitext(os.path.basename(image_path))[0]
    output_path = os.path.abspath(
        os.path.join("results", output_name + "_result.jpg")
    )

    if cv2.imwrite(output_path, image):
        print("Saved:", output_path)
    else:
        print("Failed to save:", output_path)

    cv2.imshow(label, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 7. Finish

print("\nAll test images processed.")
