import requests


def get_instructions():
    """
    Calls API and requests instructions. Returns the response
    """
    request = requests.get('https://bpdts-test-app.herokuapp.com/instructions')
    return request


def get_users():
    """
    Calls API to retrieve all users
    """
    pass

def get_london_users():
    """
    Calls API, filtering by London, to retrieve London users
    """
    pass

def within_50_miles(user, location_lat, location_lon):
    """
    Takes 'user', an record containing coordinates, and 
    coordinates ('location_lat' and 'location_lon'), and returns
    a boolean based on whether the user is within 50 miles of the location
    """
    pass

def get_users_near_london():
    pass

def run():
    pass



