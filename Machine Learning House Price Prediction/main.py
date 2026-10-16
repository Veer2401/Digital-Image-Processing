import numpy as np
import matplotlib.pyplot as plt

with open("train.csv", "r", encoding="utf-8") as file:
    headers = file.readline().strip().split(",")

area_index = headers.index("GrLivArea")
price_index = headers.index("SalePrice")

data = np.genfromtxt(
    "train.csv",
    delimiter=",",
    skip_header=1,
    usecols=(area_index, price_index),
    dtype=float,
    filling_values=np.nan
)

x = data[:, 0] 
y = data[:, 1]  

valid = np.isfinite(x) & np.isfinite(y)
x = x[valid]
y = y[valid]

n = len(x)
if n == 0:
    raise ValueError("No data found in the csv file")

sum_x = np.sum(x)
sum_y = np.sum(y)
sum_xy = np.sum(x*y)
sum_x2 = np.sum(x ** 2)

#calculating slope (m)
denominator = (n * sum_x2) - (sum_x ** 2)

if denominator == 0:
    raise ValueError(" All X values are identical!")

m = ((n * sum_xy) - (sum_x * sum_y)) / denominator

#calculating intercept (c)
c = ((sum_y * sum_x2) - (sum_x * sum_xy)) / denominator

print("=" * 45)
print(" LINEAR REGRESSION - HOUSE PRICE PREDICTION")
print("=" * 45)

print("\nNumber of houses:", n)
print("Sum of X:", sum_x)
print("Sum of Y:", sum_y)
print("Sum of XY:", sum_xy)
print("Sum of X squared:", sum_x2)

print("\nSlope (m):", round(m, 4))
print("Intercept (c):", round(c, 4))

print("\nRegression Equation:")
print(f"SalePrice = {m:.4f} * GrLivArea + ({c:.4f})")

predicted_y = (m * x) + c

print("\n===== SAMPLE PREDICTIONS =====")

for i in range(min(10, n)):
    print(
        f"Area: {x[i]:.0f} sq ft | "
        f"Actual Price: ${y[i]:,.2f} | "
        f"Predicted Price: ${predicted_y[i]:,.2f}"
    )

#original graph
plt.figure(figsize=(10, 6))

plt.scatter(x, y, color="blue", s=25, label="Original Data")

plt.title("Original House Price Dataset")
plt.xlabel("House Area (sq ft)")
plt.ylabel("Sale Price ($)")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.5)

plt.tight_layout()
plt.show()

#linear regression
plt.figure(figsize=(10, 6))

# Original actual prices
plt.scatter(
    x, y,
    color="blue",
    s=25,
    alpha=0.5,
    label="Actual Prices"
)

# Predicted prices from y = mx + c
plt.scatter(
    x, predicted_y,
    color="green",
    s=20,
    label="Predicted Prices"
)

# Best-fit regression line
x_line = np.linspace(np.min(x), np.max(x), 300)
y_line = m * x_line + c

plt.plot(
    x_line, y_line,
    color="red",
    linewidth=2,
    label="Regression Line"
)

plt.title("House Prices After Linear Regression")
plt.xlabel("House Area (sq ft)")
plt.ylabel("Sale Price ($)")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.5)

plt.tight_layout()
plt.show()





