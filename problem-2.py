import pandas as pd
from datetime import datetime
import os

def convert_to_time(time_str):
    # Define the format of the input string
    time_format = "%I:%M %p"
    
    # Use strptime to parse the time string into a datetime object
    time_obj = datetime.strptime(time_str, time_format)
    
    # Extract the time part of the datetime object
    return time_obj.time()


def tidy_three_hour(city_state):
    file_path = '/Users/shalini/Documents/AdvancedPythonSummer /Assignment 2/' + city_state + '.csv'

    # Read in the CSV file as a DataFrame
    df = pd.read_csv(file_path)
  
    # Add city and state columns
    city, state = city_state.split(',')
    city = city.replace('+', ' ').title()
    state = state.upper()
    df['city'] = city
    df['state'] = state

    daily_metrics = ['maxtempC', 'mintempC','moonrise', 'moonset','sunrise', 'sunset', 
                    'sunHour', 'uvIndex', 'uvIndex.1','totalSnow_cm','moon_illumination']
    
    rem = city_state + '_'
    for i in range(len(daily_metrics)):
        daily_metrics[i] = rem + daily_metrics[i]

    df.drop(columns=[col for col in daily_metrics if col in df.columns], inplace=True)
    
    # somethings
    dfcolLen = len(df.columns)
    lent = len(city_state) + 1
    tempList = []
    tempName = []
    myMap = {}
    for x in df.columns:
        temp = x
        tempName.append(temp)
        if (x == "date_time" or x == "city" or x == "state"):
            tempList.append(temp)
            continue
        temp = temp[lent:]
        tempList.append(temp)
    
    for i in range(dfcolLen):
        myMap[tempName[i]] = tempList[i]
    df.rename(columns=myMap, inplace=True)
        
    # Rename columns according to the specified fields
    column_renames = {
        'date_time': 'date_time',
        'DewPointC': 'dew_point_c',
        'FeelsLikeC': 'feels_like_c',
        'HeatIndexC': 'head_index_c',
        'WindChillC': 'wind_chill',
        'WindGustKmph': 'wind_gust_mph',
        'cloudcover': 'cloud_cover',
        'humidity': 'humidity',
        'precipMM': 'precipitation_mm',
        'pressure': 'pressure',
        'tempC': 'temperature_c',
        'visibility': 'visibility',
        'winddirDegree': 'wind_dir_deg',
        'windspeedKmph': 'wind_speed_mph'
    }    
    
    """
    for x in column_renames:
        stri = '\'' + x + '\','
        print (stri, end = ' ')

  """
    

    df.rename(columns=column_renames, inplace=True)
    df['wind_speed_mph'] = df['wind_speed_mph'] * 0.62137
    df['wind_gust_mph'] = df['wind_gust_mph'] * 0.62137
    # Round each number to 6 decimal places
    df['wind_gust_mph'] = [round(num, 6) for num in df['wind_gust_mph']]
    df['wind_speed_mph'] = [round(num, 6) for num in df['wind_speed_mph']]

    new_order = ['date_time', 'city','state','dew_point_c','feels_like_c','head_index_c','wind_chill','wind_gust_mph', 
                'cloud_cover','humidity','precipitation_mm','pressure','temperature_c','visibility', 'wind_dir_deg','wind_speed_mph']
    
    df = df[new_order]

    return df


def tidy_daily(city_state):
    file_path = '/Users/shalini/Documents/AdvancedPythonSummer /Assignment 2/'+ city_state + '.csv'
    # Read in the CSV file as a DataFrame
    df = pd.read_csv(file_path)
    
    # Add city and state columns
    city, state = city_state.split(',')
    city = city.replace('+', ' ').title()
    state = state.upper()
    df['city'] = city
    df['state'] = state


    daily_metrics = ['date_time', 'DewPointC', 'FeelsLikeC', 'HeatIndexC', 'WindChillC', 'WindGustKmph', 'cloudcover', 'humidity', 
                    'precipMM', 'pressure', 'tempC', 'visibility', 'winddirDegree', 'windspeedKmph', 'uvIndex', 'uvIndex.1','moon_illumination']
    rem = city_state + '_'
    for i in range(len(daily_metrics)):
        daily_metrics[i] = rem + daily_metrics[i]

    df.drop(columns=[col for col in daily_metrics if col in df.columns], inplace=True)

    # somethings
    dfcolLen = len(df.columns)
    lent = len(city_state) + 1
    tempList = []
    tempName = []
    myMap = {}
    for x in df.columns:
        temp = x
        tempName.append(temp)
        if (x == "date_time" or x == "city" or x == "state"):
            tempList.append(temp)
            continue
        temp = temp[lent:]
        tempList.append(temp)
    

    for i in range(dfcolLen):
        myMap[tempName[i]] = tempList[i]

    df.rename(columns=myMap, inplace=True)
        
    # Rename columns according to the specified fields
    column_renames = {
        'date_time': 'date',
        'maxtempC': 'max_temp_c',
        'mintempC': 'min_temp_c',
        'totalSnow_cm': 'total_snow_cm',
        'sunHour': 'sun_hours',
        'moonrise': 'moonrise',
        'moonset': 'moonset',
        'sunrise': 'sunrise',
        'sunset': 'sunset'
    }  
    df.rename(columns=column_renames, inplace=True)


    # Convert time columns from string to time format and filtering some values
    time_columns = ['moonrise', 'moonset', 'sunrise', 'sunset']
    values_to_filter = ['No moonrise', 'No moonset', 'No sunrise', 'No sunset']
    df = df[~df[time_columns].isin(values_to_filter).any(axis=1)]
    for col in time_columns:
        bob = []
        for x in df[col]:
            bob.append(convert_to_time(x))
        df[col] = bob


    # taking help from lisa
    lisa = []
    for x in df['date']:
        strx = x
        strx = strx[:11]
        lisa.append(strx)

    df['date'] = lisa
    new_order = ['date', 'city', 'state', 'max_temp_c','min_temp_c','total_snow_cm','sun_hours',
                'moonrise','moonset','sunrise','sunset']
    df = df[new_order]

    return df


def process():
    files = ['albany,ny','new+york,ny' ,'boston,ma','springfield,ma','chicago,il','springfield,il'
            ,'los+angeles,ca', 'san+francisco,ca']
    
    # Combine results of tidy_three_hour() for all files
    three_hr_dfs = [tidy_three_hour(file) for file in files]
    three_hr_df = pd.concat(three_hr_dfs)

    # Combine results of tidy_daily() for all files
    daily_dfs = [tidy_daily(file) for file in files]
    daily_df = pd.concat(daily_dfs)

    # Sort both DataFrames by city, state, date_time
    three_hr_df = three_hr_df.sort_values(by=['city','state','date_time'])
    daily_df = daily_df.sort_values(by=['city','state','date'])

    # Ensure the 'data/' directory exists
    os.makedirs('data', exist_ok=True)

    # Save the sorted DataFrames as CSV without index
    three_hr_df.to_csv('data/three_hr_df.csv', index=False)
    daily_df.to_csv('data/daily_df.csv', index=False)


def main():
    process()


if __name__ == "__main__":
    main()


### CHECK TIME STAMP EVERY THREE HOURS 2.1