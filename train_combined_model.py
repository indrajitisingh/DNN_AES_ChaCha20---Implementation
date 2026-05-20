import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical


# Load AES dataset
aes_data = pd.read_csv("dataset/aes_dataset.csv")

# Load ChaCha dataset
chacha_data = pd.read_csv("dataset/chacha_dataset.csv")


# Add labels
aes_data["algorithm"] = "AES"
chacha_data["algorithm"] = "ChaCha20"


# Combine datasets
combined_data = pd.concat([aes_data, chacha_data], ignore_index=True)


# Separate features and labels
X = combined_data.drop("algorithm", axis=1)

# Convert all values into numeric format
X = X.apply(pd.to_numeric, errors="coerce")

# Replace missing values with 0
X = X.fillna(0)

# Convert into float format for TensorFlow
X = X.astype("float32")

y = combined_data["algorithm"]


# Convert labels into numbers
label_encoder = LabelEncoder()

y_encoded = label_encoder.fit_transform(y)

y_categorical = to_categorical(y_encoded)


# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y_categorical,
    test_size=0.2,
    random_state=42
)


# Build DNN model
model = Sequential()

model.add(Dense(128, activation="relu", input_shape=(X.shape[1],)))

model.add(Dense(64, activation="relu"))

model.add(Dense(32, activation="relu"))

model.add(Dense(2, activation="softmax"))


# Compile model
model.compile(
    optimizer="adam",
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)


# Train model
history = model.fit(
    X_train,
    y_train,
    validation_data=(X_test, y_test),
    epochs=10,
    batch_size=32
)


# Evaluate model
loss, accuracy = model.evaluate(X_test, y_test)

print(f"\nCombined Model Accuracy: {accuracy * 100:.2f}%")


# Save model
model.save("combined_dnn_model.keras")

print("Combined AES vs ChaCha20 model saved successfully")