import requests  # for high level API calls, as recommended in Python docs
from math import radians, cos, sin, asin, sqrt  # for sqrt function and radians
from geopy import distance as geopydistance  # for testing


def get_instructions():
    """
    Calls API and requests instructions. Returns the response
    """
    request = requests.get('https://bpdts-test-app.herokuapp.com/instructions')
    return request


def user_cleaning(users):
    """
    Converts strings in API call returns to float so that it
    doesn't have to be repeated in the rest of the code.
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
    Retrieves and cleans users, returning JSON list
    """
    all_users = get_users().json()
    return user_cleaning(all_users)


def get_london_users():
    """
    Calls API, filtering by London, to retrieve London users.
    """
    london_users = requests.get(
        'https://bpdts-test-app.herokuapp.com/city/London/users')
    return london_users


def get_london_users_json():
    """
    Retrieves and cleans London users, return JSON list
    """
    london_users = get_london_users().json()
    return user_cleaning(london_users)


def calculate_distance(user_lat, user_lon, location_lat, location_lon):
    """
    Takes user coordinates ('user_lat', and 'user_lon') and target
    coordinates ('location_lat' and 'location_lon'), and returns the
    distance, in miles, between the two.
    This function initially used Pythagoras' Theorem, but later replaced
    it with Haversine formula implementation in Python found online, as
    it was more accurate.
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
    This function is only used for debugging/testing purposes,
    to ensure accuracy of the 'calculate_distance' function.
    """
    user_location = (user_lat, user_lon)  # geopy requires tuples
    london = (location_lat, location_lon)
    return geopydistance.distance(user_location, london).miles


def discrepency_between_calcs(distance_1, distance_2):
    """
    Returns discrepency between two distances
    """
    return (distance_1 / distance_2) * 100


def within_50_miles(user_lat, user_lon, location_lat, location_lon):
    """
    Takes user location and another location and returns a boolean based
    on whether the user is within 50 miles of that location.
    """
    distance = calculate_distance(
        user_lat,
        user_lon,
        location_lat,
        location_lon,
        )

    if distance <= 50:
        return True
    return False


def get_users_near_london(users, london_lat, london_lon):
    """
    Function to retrieve users who are either listed as in London,
    or whose current coordinates are within 50 miles of London
    """
    users_near_london = get_london_users_json()  # initial list
    for u in users:  # if a user is within 50 miles of London...
        if within_50_miles(
            u["latitude"],
            u["longitude"],
            london_lat,
            london_lon):
                new_record = True  # sets a flag to check against
                for l in users_near_london:
                    if u == l:  # If the record is already present...
                        new_record = False  # mark the flag
                        break  # stop looping.
                if new_record:
                    users_near_london.append(u)  # if not then append
    return users_near_london


def return_users_near_london():
    london_lat, london_lon = 51.509865, -0.118092  # from www.latlong.net
    users = get_users_json()  # retrieves all users
    london_users = get_users_near_london(  # then narrows down
        users,
        london_lat,
        london_lon)

    return london_users