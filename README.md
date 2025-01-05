
In this assignment, we will gather data from an API using requests and then we will do some data manipulation with Pandas. You have to create the API calls using the endpoints urls, headers, and query parameters.

**Problem 1
**In this problem, you will use data from the Washington Metropolitan Area Transit Authority API. There are several servoce endpoints depending on the task to be performed. You can explore the various services here You need to get an API key for this first part:

Sign up and get a confirmation email
After you sign up, navigate to the Products page and subscribe to the Default Tier. (don't worry, it's free.)
Make a note of the API key, since you will need it.
Part 1.1
Use the JSON - Station List API for this part.

**Write a script called part-1-1.py that performs the following tasks:
**
Retrieves all stations for the Red Line using requests
Creates a Pandas DataFrame with the only these two fields: Code, and Name
Sorts the DataFrame by station code in ascending order
Saves the resulting dataframe as a CSV in a file called red-line-stations.csv in the data/ directory
Part 1.2
Use the JSON - Path Between Stations API for this part.

**Write a script called part-1-2.py that performs the following tasks:
**
Loads the DataFrame you created in part 1.1
Creates two variables (retrieve these values from the DataFrame)
start with the station code for Glenmont
end with the station code for Shady Grove
Calls the API with appropriate start and end parameters to get all stations within the path from start to end
Stores the results into a Pandas DataFrame with the following fields: LineCode, StationCode, StationName, SeqNum, and DistanceToPrev
Sorts the DataFrame by sequence number ascending
Saves the resulting DataFrame as a CSV in a file called red-line-sequence.csv in the data/ directory
Calculates the total lenght of the path
Finds the pair of stations with the shortest path between them
Problem 2
For this problam, you will work with the Rick and Morty API. Rick and Morty is a popular cartoon.

Specifically, you will work with the Character. Read the documentation to get familiar with the API.

**Write a script aclled problem-2.py that performs the following tasks:
**
Write a function that uses iterators and generators to retrieve all characters (and therefore all pages)
Run the function to get the data
Saves the results in JSON format in a file called data/rick-and-morty-characters.json


