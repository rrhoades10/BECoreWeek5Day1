import requests
import json

# json takes the form of a python dictionary

pokemon = {
    "name": "Pikachu",
    "type": "Electric",
    "level": 100
}

print(pokemon['name'])

poke_type = pokemon['type']
print(poke_type)
# json presents information in key-value pairs

# nested dictionary for trainers

trainers = {
    "trainer": {
        "name": "Ash",
        "age": 10
    },
    "trainer2": {
        "name": "Ryan",
        "age": 32,
        "pokemon": ["Heracross", "Charmander", "Vaporeon", "Diglett"]
    }
}

# print(trainers['trainer']['name'])
# for poke in trainers['trainer2']['pokemon']:
#     print(poke)

# making requests to the pokeapi
def poke_api_call():
    response = requests.get("https://pokeapi.co/api/v2/pokemon/heracross")
    json_data = response.text

    # converting response text to a python dictionary via JSON
    # poke_data = json.loads(json_data)
    poke_data = response.json()

    # print(poke_data)

    # access data
    print(poke_data["name"]) #accessing the name key from the pokeapi
    print(poke_data["types"])
    

# poke_api_call()

def poke_dump():
    pokemon_data = {
        "name": "Bulbasaur",
        "type": "Grass/Poison",
        "abilities": ["Overgrow", "Chlorophyll"]
    }

    # convert python dictionary to text
    json_output = json.dumps(pokemon_data)
    print(json_output)
    print(type(json_output))

# poke_dump()


# creating a Pokemon class
# and set that pokemon's attributes through an api call
class Pokemon():
    def __init__(self, name):
        self.name = name
        self.types = []
        self.abilities = []
        # self.special_ability = ""
        # poke_api_call
        self.poke_api_call()

    def poke_api_call(self):
        r = requests.get(f"https://pokeapi.co/api/v2/pokemon/{self.name.lower()}")
        if r.status_code == 200:
            pokemon = r.json()
        else:
            print(f"Please check the spelling and try again!: {r.status_code}")
            return
        
        self.name = pokemon['name']
        self.types = [type_['type']['name'] for type_ in pokemon['types']]
        self.abilities = [pokebility['ability']['name'] for pokebility in pokemon['abilities']]
        # self.special_ability = pokemon['abilities'][0]['ability']['name']
        print(f"{self.name} has been caught!")

my_pokemon = Pokemon("charmander")
print(my_pokemon.abilities)    

    

#  types: [
#     {
#         slot: 1,
#         type: {
# name: "bug",
# url: "https://pokeapi.co/api/v2/type/7/"
# }
# },
# {
# slot: 2,
# type: {
# name: "fighting",
# url: "https://pokeapi.co/api/v2/type/2/"
# }
# }
# ]


