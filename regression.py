# Step 1: Define the dataset (House Size in square feet vs. Price in $1000s)
house_sizes = [600, 800, 1000, 1200, 1400, 1600, 1800, 2000]
house_prices = [150, 180, 200, 220, 250, 280, 300, 320]

# Step 2: Calculate the mean of X (house_sizes) and Y (house_prices)
def calculate_mean(values):
    total = sum(values)  # Sum of all values
    count = len(values)  # Number of values
    return total / count  # Mean formula

X_mean = calculate_mean(house_sizes)
Y_mean = calculate_mean(house_prices)

# Step 3: Calculate slope (m) using the formula
def calculate_slope(X, Y, X_mean, Y_mean):
    numerator = sum((X[i] - X_mean) * (Y[i] - Y_mean) for i in range(len(X)))  # ∑(Xi - X̄)(Yi - Ȳ)
    denominator = sum((X[i] - X_mean) ** 2 for i in range(len(X)))  # ∑(Xi - X̄)²
    return numerator / denominator  # m = numerator / denominator

m = calculate_slope(house_sizes, house_prices, X_mean, Y_mean)

# Step 4: Calculate intercept (b) using formula: b = Ȳ - m * X̄
b = Y_mean - (m * X_mean)

# Step 5: Define the prediction function Y = mX + b
def predict(X):
    return m * X + b

# Step 6: Make predictions
test_house_size = 1700  # Predict price for a house of 1700 sq. ft.
predicted_price = predict(test_house_size)

# Step 7: Print results
print(f"Equation of Line: Y = {m:.2f}X + {b:.2f}")
print(f"Predicted Price for {test_house_size} sq. ft. house: ${predicted_price:.2f}K")

# Step 8: Calculate Mean Squared Error (MSE)
def mean_squared_error(X, Y):
    errors = [(Y[i] - predict(X[i])) ** 2 for i in range(len(X))]  # (Yi - Ŷi)²
    return sum(errors) / len(Y)  # MSE formula

mse = mean_squared_error(house_sizes, house_prices)
print(f"Mean Squared Error: {mse:.2f}")
