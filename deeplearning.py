import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Sample login data
# Features: [failed login attempts, unfamiliar location (0 = No, 1 = Yes)]
X = np.array([
    [0, 0],
    [1, 0],
    [2, 0],
    [1, 1],
    [5, 1],
    [8, 1],
    [10, 1],
    [7, 0],
    [3, 1],
    [0, 1]
], dtype=float)

# Labels: 0 = Normal, 1 = Suspicious
y = np.array([0, 0, 0, 0, 1, 1, 1, 1, 0, 0])

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

# Scale the input features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Create the ANN
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(2,)),
    tf.keras.layers.Dense(8, activation="relu"),
    tf.keras.layers.Dense(4, activation="relu"),
    tf.keras.layers.Dense(1, activation="sigmoid")
])

# Configure the model for training
model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

# Train the ANN
model.fit(X_train, y_train, epochs=50, verbose=0)

# Evaluate the model on test data
loss, accuracy = model.evaluate(X_test, y_test, verbose=0)
print("Test Accuracy:", round(accuracy * 100, 2), "%")

# Predict on a new login
new_login = np.array([[8, 1]], dtype=float)
new_login_scaled = scaler.transform(new_login)

probability = model.predict(new_login_scaled, verbose=0)[0][0]

if probability >= 0.5:
    print("Suspicious Login")
else:
    print("Normal Login")

print("Suspicious probability:", round(float(probability) * 100, 2), "%")op
