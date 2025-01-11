import json
import csv

class DataStorage:
    @staticmethod
    def save_to_json(data, filename="projects.json"):
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)

    @staticmethod
    def save_to_csv(data, filename="projects.csv"):
        if data:
            keys = data[0].keys()
            with open(filename, "w", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=keys)
                writer.writeheader()
                writer.writerows(data)
  
