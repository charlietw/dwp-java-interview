# Users near London


### Purpose and notes
This application consumes an API which returns a list of users and coordinates, and picks out the users which are either listed as being in London, or are showing to be within 50 miles of London, based on their current coordinates, and offers these as an API.

It calculates the distance between two coordinates using the [Haversine formula](https://en.wikipedia.org/wiki/Haversine_formula). 

This application makes use of the [geopy](https://geopy.readthedocs.io/en/stable/) library for validation of the distances only (it is not used to calculate distances), and the [requests](https://requests.readthedocs.io/en/master/) library for API consumption, as is recommended in the official Python documentation. 

In order to implement a consumable API, this application uses [Flask](https://flask.palletsprojects.com/en/1.1.x/).

For the purpose of this application, the coordinates of London were determined to be 51.509865, -0.118092, taken from www.latlong.net. 


### Requirements
+ Python 3.6+


### Setup

1. Download this code.

2. Install the required libraries (```pip install -r requirements.txt```), setting up an virtual environment first if you prefer.

3. Change directory to the location of the code and run it (``` python api.py ```).

4. Navigate to the API which will now be running locally (by default at 127.0.0.1:5000).


### Testing 

The main body of code (functions.py) has 92% test coverage. The lines which were not tested were the function to calculate distances using geopy (as it is only ever used in testing), and the lines which rejected duplicate records when calclating users within 50 miles of London, as there were no duplicate records in the data provided.