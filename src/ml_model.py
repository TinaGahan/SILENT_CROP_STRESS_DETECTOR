import pandas as pd
from sklearn.tree import DecisionTreeClassifier

data = pd.read_csv("farm_data.csv")

X = data[["temperature", "soil_moisture"]]
y = data["stress"]

model = DecisionTreeClassifier()
model.fit(X, y)

test_data = [[37, 22]]  # hot + low moisture
prediction = model.predict(test_data)

if prediction[0] == 1:
    print("Crop Stress Detected")
else:
    print("Crop is Healthy")