import requests

# Base url for the API route
base_url = "https://pokeapi.co/api/v2"

def get_pokemon_info(name):
    global base_url
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)

    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"failed to retrieve the data {response.status_code}")
    

pokemon_name = "charmander"
pokemon_info = get_pokemon_info(pokemon_name)


if pokemon_info:
    print(f"Name: {pokemon_info["name"]}")
    print(f"ID: {pokemon_info["id"]}")
    print(f"Height: {pokemon_info["height"]}")
    print(f"Weight: {pokemon_info["weight"]}")


    # Loop through all abilities and print their names
    for ability in pokemon_info['abilities']:
        print(ability['ability']['name'])