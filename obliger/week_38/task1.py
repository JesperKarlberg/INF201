# removes the bad sensor readings, and prints within the treashold. 

low_threshold = 0.000
high_threshold = 20.000

sensor_readings = [
    2.673, -3.876, 4.589, None, None, None, -6.111, 0.435, None,
0.005,2.444, 10.897, 0.019, 10.222, -0.543, None, 8.097, 0.962, None,1.005,
None, 0.765, 0.765, 0.765, 0.765, 7.937, -1.007, 4.405, None,None
]

#cleaned list

filtered_readings = []

for value in sensor_readings:
    if value is not None and low_threshold <= value <= high_threshold:
        filtered_readings.append(value)

print ("Filtered sensor readings:", filtered_readings)

print (f"valid readings: {len(filtered_readings)/len(sensor_readings)*100:.2f}%")
print (f"average readings: {sum(filtered_readings)/len(filtered_readings):.2f}")
print (f"removed readings: {len(sensor_readings) - len(filtered_readings)}")


