import requests # for easy high level API calls, as recommended in Python documentation
from math import radians, cos, sin, asin, sqrt # for sqrt function and radians
from geopy import distance as geopydistance # for testing


def get_instructions():
    """
    Calls API and requests instructions. Returns the response
    """
    request = requests.get('https://bpdts-test-app.herokuapp.com/instructions')
    return request


def user_cleaning(users):
    """
    Converts string to float upon retrieval so that it doesn't have to be done
    in the rest of the code.
    """
    for u in users:
        u["longitude"] = float(u["longitude"])
        u["latitude"] = float(u["latitude"])
    return users


def get_users():
    """
    Calls API to retrieve all users
    """
    all_users = requests.get('https://bpdts-test-app.herokuapp.com/users')
    return all_users


def get_users_json():
    """
    Retrieves and cleanes users, returning JSON list
    """
    all_users = get_users().json()
    return user_cleaning(all_users)



def get_london_users():
    """
    Calls API, filtering by London, to retrieve London users
    """
    london_users = requests.get('https://bpdts-test-app.herokuapp.com/city/London/users')
    return london_users


def calculate_distance(user_lat, user_lon, location_lat, location_lon):
    """
    Takes user coordinates ('user_lat', and 'user_lon') and target
    coordinates ('location_lat' and 'location_lon'), and calculates the
    distance in miles between the two.
    This function initially used Pythagoras Theorum, but later replaced it with
    Haversine formula implementation in Python found online as it was more accurate.
    """
    # convert decimal degrees to radians 
    user_lat = radians(user_lat)
    user_lon = radians(user_lon)
    location_lat = radians(location_lat)
    location_lon = radians(location_lon)
     
    # haversine formula taken from:
    # https://kanoki.org/2019/02/14/how-to-find-distance-between-two-points-based-on-latitude-and-longitude-using-python-and-sql/
    dlon = location_lon - user_lon 
    dlat = location_lat - user_lat 
    a = sin(dlat/2)**2 + cos(user_lat) * cos(location_lat) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 3890.0 
    return c * r


def calculate_distance_geopy(user_lat, user_lon, location_lat, location_lon):
    """
    Takes user coordinates ('user_lat', and 'user_lon') and target
    coordinates ('location_lat' and 'location_lon'), and calculates the
    distance in miles between the two using geopy.
    """
    # tuples for geopy
    user_location = (user_lat, user_lon)
    london = (location_lat, location_lon)
    return geopydistance.distance(user_location, london).miles


def discrepency_between_calcs(distance_1, distance_2):
    """
    Returns discrepency between two distances
    """
    return (distance_1 / distance_2) * 100


def within_50_miles(user, location_lat, location_lon):
    """
    Takes user and returns a boolean based on whether the user
    is within 50 miles of the location.
    """
    distance = calculate_distance(
        user["latitude"],
        user["longitude"],
        location_lat,
        location_lon,
        )

    geopy_distance = calculate_distance_geopy(
        user["latitude"],
        user["longitude"],
        location_lat,
        location_lon,
        )

    if distance <= 50:
        return True
    return False


def get_users_near_london():
    pass


def run():
    london_lat, london_lon = 51.509865, -0.118092
    users = get_users_json()
    count = 0
    for u in users:
        if within_50_miles(
            u,
            london_lat,
            london_lon):
            count += 1

    print(count)

run()

