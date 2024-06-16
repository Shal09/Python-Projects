import requests
import json
import os

API_URL = 'https://rickandmortyapi.com/api/character'
OUTPUT_DIR = 'data'
OUTPUT_FILE = 'rick-and-morty-characters.json'

def fetch_all_characters():
    page = 1
    characters = []
    
    while True:
        response = requests.get(API_URL, params={'page': page})
        data = response.json()
        print(data)
        characters.extend(data['results'])
        
        if 'info' in data and data['info']['next']:
            page += 1
        else:
            break
    
    return characters

def save_characters_to_json(characters, output_path):
    with open(output_path, 'w') as json_file:
        json.dump(characters, json_file, indent=4)

def main():
    # Fetch all characters
    characters = fetch_all_characters()

    # If OUTPUT_DIR exits then good else it would create new folder as OUTPUT_DIR
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # print(characters)
    # Save the results to a JSON file
    output_path = os.path.join(OUTPUT_DIR, OUTPUT_FILE)
    save_characters_to_json(characters, output_path)
    print(f"Saved {len(characters)} characters to {output_path}")

if __name__ == "__main__":
    main()
