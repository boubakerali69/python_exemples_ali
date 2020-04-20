import json

values = []

def read_values_from_json():
    
    with open("charatere.json") as f:
        data = json.load(f)
        print(data)
        for entry in data:
            values.append(entry["nom"])
    #return values 
    
#programme pricipal

read_values_from_json()
print(values)

