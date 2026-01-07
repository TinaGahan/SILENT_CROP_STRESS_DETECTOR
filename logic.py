temperature = 38 #celsius
soil_moisture = 20 #in percentage

if temperature > 35 and soil_moisture < 30:
	print("crop is stressed : water deficiency")
else:
	print("crop is healthy!")
