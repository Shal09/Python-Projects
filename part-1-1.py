import requests
import pandas as pd
import os

# Replace 'YOUR_API_KEY' with your actual WMATA API key
API_KEY = 'a777162bfc0a463ab6677306d460aa67'
URL = 'https://api.wmata.com/Rail.svc/json/jStations?LineCode=RD'

def fetch_red_line_stations(api_key):
    headers = {
        'api_key': api_key
    }
    response = requests.get(URL, headers=headers)
    if response.status_code == 200:
        return response.json().get('Stations', [])
    else:
        response.raise_for_status()

def main():
    stations = fetch_red_line_stations(API_KEY)

    # Create a DataFrame with only Code and Name fields
    stations_df = pd.DataFrame(stations, columns=['Code', 'Name'])

    # Sort the DataFrame by station code in ascending order
    stations_df = stations_df.sort_values(by='Code').reset_index(drop=True)

    # Save the resulting DataFrame as a CSV in the data/ directory
    output_dir = "data"
    output_file = "red-line-stations.csv"

    # Ensure the directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Save to CSV
    output_path = os.path.join(output_dir, output_file)
    stations_df.to_csv(output_path, index=False)

    print(f"Red Line stations saved to {output_path}")

if __name__ == "__main__":
    main()
