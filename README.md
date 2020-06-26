# hours-tracking


### Purpose
This app consumes an API which returns a list of users and coordinates, and picks out the users which are either listed as being in London, or are showing to be within 50 miles of London, based on their current coordinates.

It calculates the distance between two coordinates using the [Haversine formula](https://en.wikipedia.org/wiki/Haversine_formula). 

This app makes use of the [geopy](https://geopy.readthedocs.io/en/stable/) library for validation of the distances only (it is not used to calculate distances), and the [requests](https://requests.readthedocs.io/en/master/) library for API consumption, as is recommended in the official Python documentation. 


### Requirements
+ Python 3.6+


### Setup

1. Download this code.

2. Install the required libraries (```pip install -r requirements.txt```), setting up an virtual environment first if you prefer.

3. Change directory to the location of the code and run it! (``` python run.py ```).


### Testing coverage

The main body of code has 92% test coverage. The lines which were not tested were the function to calculate distances using geopy (as it is only ever used in testing), and the lines which rejected duplicate records when calclating users within 50 miles of London, as there were no duplicate records in the data provided.