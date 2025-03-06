import requests

BASE_URL = "https://pokeapi.co/api/v2/"
def get_pokemon_info(name):
    url = f"{BASE_URL}pokemon/{name.lower()}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to retrieve data. HTTP Status Code: {response.status_code}")
        return None
pokemon_name = input("Enter the name of a Pokémon: ")#.strip()
pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info:
    print(f"\nPokémon Details:")
    print(f"Name: {pokemon_info.get('name')}")
    print(f"Weight: {pokemon_info.get('weight')}")
    print(f"ID: {pokemon_info.get('id')}")
else:
    print("Could not retrieve Pokémon data. Please check the name and try again.")
