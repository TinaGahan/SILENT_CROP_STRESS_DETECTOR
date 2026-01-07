import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Load data
data = pd.read_csv("farm_data.csv")

X = data[["temperature", "soil_moisture"]]
Y = data["stress"]

# Train model
model = DecisionTreeClassifier()
model.fit(X, Y)

print("Silent Crop Stress Detector")
print("------------------------------")

# User input
temp = float(input("Enter temperature (°C): "))
moisture = float(input("Enter soil moisture (%): "))

# Prediction
prediction = model.predict([[temp, moisture]])

if prediction[0] == 1:
    print("Crop Stress Detected: Take Action!")
else:
    print("Crop is Healthy")