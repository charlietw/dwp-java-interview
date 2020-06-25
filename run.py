import requests # for easy high level API calls, as recommended in Python documentation
import math # for sqrt function


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
    all_users = requests.get('https://bpdts-test-app.herokuapp.com/users')
    return all_users.json()


def get_london_users():
    """
    Calls API, filtering by London, to retrieve London users
    """
    london_users = requests.get('https://bpdts-test-app.herokuapp.com/city/London/users')
    return all_users.json()


def within_50_miles(user_lat, user_lon, location_lat, location_lon):
    """
    Takes user coordinates ('user_lat', and 'user_lon') and target
    coordinates ('location_lat' and 'location_lon'), and returns
    a boolean based on whether the user is within 50 miles of the location
    """
    lat_diff = location_lat - user_lat # determines difference in latitude
    lon_diff = location_lon - user_lon # determines difference in longitude
    distance = math.sqrt(
        (lat_diff * lat_diff) + (lon_diff * lon_diff)
        ) # square root of the lat_diff squared plus the lon_diff squared
    return distance


def get_users_near_london():
    pass


def run():
    london_lat = 51.509865
    london_lon = -0.118092 # taken from 
    users = get_users()
    count = 0
    for u in users:
        # print(u["latitude"], u["longitude"])
        distance = within_50_miles(
            float(u["latitude"]),
            float(u["longitude"]), # convert from string to float
            london_lat,
            london_lon)
        if distance < 50:
            count += 1
    print(count)
    # print(within_50_miles(
    #     37.792,-122.419,-33.878, 151.265)*111.139)


run()




