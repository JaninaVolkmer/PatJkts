import json

class Jackets:
    def __init__(self, style_id, category, name, fit, features, materials, processes, colour):
        self.style_id = style_id
        self.category = category
        self.name = name
        self.fit = fit
        self.feature1 = features['feature1']
        self.feature2 = features['feature2']
        self.feature3 = features['feature3']
        self.materials = materials
        self.processes = processes
        self.colour = colour
    
    @classmethod 
    def from_json(cls, json_string):
        json_dict = json.loads(json_string)
        return cls(**json_dict)
    
    # representation function to see what happens
    def __repr__(self):
        return f"{self.name}"
    
json_string = '''{
        "style_id": "24406",
        "category": "Windbreaker",
        "name": "Dirt Roamer Jacket",
        "fit": "Slim fit",
        "features": {
            "feature1": "Stowable, Helmet-Compatible Hood",
            "feature2": "Built-In Stow Pocket",
            "feature3": "Compressible and Packable"
        },
        "materials": "Stretchy, Breathable Recycled Shell Fabric",
        "processes": "Fair Trade",
        "colour": "Pantone/ Farrow"
    }
'''

# Create Jackets Object
#jacket = Jackets.from_json(json_string)
#print(jacket)
#print(jacket.materials)
#print(jacket.name)
#print(jacket.fit)

# open json and loop over each individuel json objects that gets created
# 'r' = read
jackets_list = []
with open('jackets.json', 'r') as json_file:
    jacket_data = json.loads(json_file.read())
    for j in jacket_data:
        jackets_list.append(Jackets(**j))

print(jackets_list)
