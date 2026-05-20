import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical


# Load AES dataset
aes_data = pd.read_csv("dataset/aes_dataset.csv")

# Add label column
aes_data["label"] = "AES"


# Convert hexadecimal values into numeric format
feature_columns = aes_data.columns[:-1]

for column in feature_columns:
    aes_data[column] = aes_data[column].apply(lambda x: int(str(x), 16))

# Prepare features and labels
X = aes_data.drop("label", axis=1).astype("float32")

y = aes_data["label"]


# Encode labels
label_encoder = LabelEncoder()

y_encoded = label_encoder.fit_transform(y)

y_categorical = to_categorical(y_encoded)


# Split dataset
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

model.add(Dense(y_categorical.shape[1], activation="softmax"))


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
    epochs=10,
    batch_size=32,
    validation_data=(X_test, y_test)
)


# Evaluate model
loss, accuracy = model.evaluate(X_test, y_test)

print(f"\nModel Accuracy: {accuracy * 100:.2f}%")

# Save model
model.save("aes_dnn_model.h5")

print("AES DNN model saved successfully")