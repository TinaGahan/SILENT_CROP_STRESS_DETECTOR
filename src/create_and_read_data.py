import pandas as pd

data = {
    "temperature": [38, 36, 28, 30, 40, 33],
    "soil_moisture": [20, 25, 60, 50, 15, 35],
    "stress": [1, 1, 0, 0, 1, 0]
}

df = pd.DataFrame(data)
df.to_csv("farm_data.csv", index=False)
print("CSV created successfully")

loaded_data = pd.read_csv("farm_data.csv", encoding='utf-8')
print("Data Loaded Successfully")
print(loaded_data)