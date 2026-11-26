import pandas as pd
import yaml
import json



#   Les inn konfigurasjonen
config_path = r"C:\Users\Fredrik Olstad\Desktop\skole\inf201\obliger\week_40\config.yml"

with open(config_path, "r") as f:
    config = yaml.safe_load(f)

print(f"Leste config fra: {config_path}")
print(f"Maks dager siden kalibrering: {config['max_days_since_calibration']}")
print(f"Output-fil: {config['output_file']}")

max_days = config["max_days_since_calibration"]
output_file = config["output_file"]



#   Les inn data fra Excel og CSV
sensors_path = r"C:\Users\Fredrik Olstad\Desktop\skole\inf201\obliger\week_40\sensors.xlsx"
calib_path   = r"C:\Users\Fredrik Olstad\Desktop\skole\inf201\obliger\week_40\calibrations.csv"

sensors_df = pd.read_excel(sensors_path)
calib_df = pd.read_csv(calib_path)

print(f"Leste sensors.xlsx og calibrations.csv")



#   Slå sammen dataene på sensor_id
merged = pd.merge(calib_df, sensors_df, on="sensor_id")


#   Filtrer sensorer som er over grensen
overdue = merged[merged["days_since_calibration"] > max_days]


#   Eksporter til JSON
result = overdue.to_dict(orient="records")

with open(output_file, "w") as f:
    json.dump(result, f, indent=2)



print(f"Ferdig {len(result)} sensorer er over {max_days} dager siden kalibrering.")
print(f"JSON-fil lagret som: {output_file}")
