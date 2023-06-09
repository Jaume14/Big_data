import csv
import json
import os

# Establim els fitxers que volem unir
folder_path = 'datasets/song-info'
json_files = [file for file in os.listdir(folder_path) if file.endswith('.json')]

# Creem la llista on emmagatzemarem les dades
combined_data = []

# Processem cada JSON
for json_file in json_files:
    json_path = os.path.join(folder_path, json_file)
    with open(json_path, 'r') as file:
        data = json.load(file)

    # Afegim el nom de la playlist a la qual pertany cada cançó
    for entry in data:
        entry['file_name'] = json_file

    # Afegim les dades a la llista final
    combined_data.extend(data)

# Creem el header
column_headers = list(combined_data[0].keys())

# Desem les dades finals en un fitxer CSV
output_file = 'combined_data.csv'
output_path = os.path.join(folder_path, output_file)
with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(column_headers)
    for entry in combined_data:
        writer.writerow(entry.values())

print(f"Combined data saved to {output_file}.")
