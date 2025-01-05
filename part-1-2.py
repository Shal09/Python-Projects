import requests
import pandas as pd
import os

# Replace 'YOUR_API_KEY' with your actual WMATA API key
API_KEY = 'a77_API KEY'

# URLs for WMATA API
STATIONS_URL = 'https://api.wmata.com/Rail.svc/json/jStations?LineCode=RD'
PATH_URL = 'https://api.wmata.com/Rail.svc/json/jPath'

def fetch_red_line_stations(api_key):
    headers = {
        'api_key': api_key
    }
    response = requests.get(STATIONS_URL, headers=headers)
    if response.status_code == 200:
        return response.json().get('Stations', [])
    else:
        response.raise_for_status()

def fetch_path(api_key, from_station_code, to_station_code):
    headers = {
        'api_key': api_key
    }
    params = {
        'FromStationCode': from_station_code,
        'ToStationCode': to_station_code
    }
    response = requests.get(PATH_URL, headers=headers, params=params)
    if response.status_code == 200:
        return response.json().get('Path', [])
    else:
        response.raise_for_status()

def main():
    # Fetch all Red Line stations
    stations = fetch_red_line_stations(API_KEY)
    stations_df = pd.DataFrame(stations, columns=['Code', 'Name'])

    # Get station codes for Glenmont and Shady Grove
    start_station_code = stations_df.loc[stations_df['Name'] == 'Glenmont', 'Code'].values[0]
    end_station_code = stations_df.loc[stations_df['Name'] == 'Shady Grove', 'Code'].values[0]

    # Fetch path from Glenmont to Shady Grove
    path = fetch_path(API_KEY, start_station_code, end_station_code)
    path_df = pd.DataFrame(path, columns=['LineCode', 'StationCode', 'StationName', 'SeqNum', 'DistanceToPrev'])

    # Sort the DataFrame by sequence number in ascending order
    path_df = path_df.sort_values(by='SeqNum').reset_index(drop=True)

    # Save the resulting DataFrame as a CSV in the data/ directory
    output_dir = "data"
    output_file = "red-line-sequence.csv"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, output_file)
    path_df.to_csv(output_path, index=False)
    print(f"Path from Glenmont to Shady Grove saved to {output_path}")

    # Calculate the total length of the path
    total_length = path_df['DistanceToPrev'].sum()
    print(f"Total length of the path: {total_length} miles")

    # Find the pair of stations with the shortest path between them
    # min_distance = path_df['DistanceToPrev'].min()
    min_dist = path_df['DistanceToPrev'].max()
    for x in path_df['DistanceToPrev']:
        if x == 0:
            continue

        else:
            if x < min_dist: 
                min_dist = x
    
    shortest_path = path_df[path_df['DistanceToPrev'] == min_dist]

    print("\nPair of stations with the shortest path between them: ")
    for index, row in shortest_path.iterrows():
        if index > 0:
            previous_station = path_df.loc[index - 1, 'StationName'] 

    current_station = row['StationName']
   
    print(f"Distance({previous_station}, {current_station}) = {row['DistanceToPrev']} miles")


if __name__ == "__main__":
    main()
