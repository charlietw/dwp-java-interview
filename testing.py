import unittest
from run import *
from geopy import distance as geopydistance # for testing


class TestInstructions(unittest.TestCase):
    """
    Asserts that the API can be called successfully
    """

    def test_api_call(self):
        r = get_instructions()
        self.assertEqual(r.status_code, 200)


class TestUsers(unittest.TestCase):
    """
    Asserts that the API can be called successfully to get users
    """

    def test_api_call(self):
        r = get_users()
        self.assertEqual(r.status_code, 200)


class TestLondonUsers(unittest.TestCase):
    """
    Asserts that the API can be called successfully to get users in London
    """

    def test_api_call(self):
        r = get_london_users()
        self.assertEqual(r.status_code, 200)


class TestWithin50Miles(unittest.TestCase):
    """
    Asserts that the function to compare two coords works correctly
    """

    def setUp(self):
        self.users = get_users_json()


    def test_with_example_data(self):
        """
        Takes all positive, whole integers as coordinates and compares with geopy
        """
        x_1 = 4
        y_1 = 1
        x_2 = 6
        y_2 = 6

        p1 = [x_1, y_1]
        p2 = [x_2, y_2] 
        distance = calculate_distance(p1[0], p1[1], p2[0], p2[1])

        p1 = (x_1, y_1)
        p2 = (x_2, y_2)
        distance_geopy = geopydistance.distance(p1, p2).miles
        diff = discrepency_between_calcs(distance, distance_geopy)
        print("distance is ", distance)
        print("geopy distance is ", distance_geopy)
        print("difference is ", diff)
        self.assertTrue(diff < 105)
        self.assertTrue(diff > 95) # asserts that deviation is less than 5% either side


    def test_with_example_data_negative(self):
        """
        Takes coordinates and compares with geopy. 
        Exposes bug when using a negative latitude (fixed).
        """
        x_1 = 51.65539
        y_1 = 0.05725
        x_2 = 51.509865
        y_2 = -0.118092
        p1 = [x_1, y_1]
        p2 = [x_2, y_2] 
        distance = calculate_distance(p1[0], p1[1], p2[0], p2[1])
        p1 = (x_1, y_1) # formatting for geopy
        p2 = (x_2, y_2)
        distance_geopy = geopydistance.distance(p1, p2).miles
        diff = discrepency_between_calcs(distance, distance_geopy)
        self.assertTrue(diff < 105)
        self.assertTrue(diff > 95) # asserts that deviation is less than 5% either side


    def test_all_data(self):
        """
        Gets disrecepency for all data in source and asserts that no
        difference is > 5% from what is calculated by geopy.
        """
        count = 0 # count of inaccurate calculations
        london_lat = 51.509865
        london_lon = -0.118092
        london = (london_lat, london_lon) # formatting for geopy
        for u in self.users:
            user_lat = u["latitude"]
            user_lon = u["longitude"]
            user = (user_lat, user_lon) # formatting for geopy
            distance = calculate_distance(user_lat, user_lon, london_lat, london_lon)
            distance_geopy = geopydistance.distance(user, london).miles # geopy calc
            diff = discrepency_between_calcs(distance, distance_geopy)
            if diff > 105 or diff < 95: # if discrepency is > 5% then flag it
                print("diff:", diff, "coords: ", user)
                count += 1
        print("count:", count)
        self.assertTrue(count == 0) # to pass the test they all have to be < 5%





class TestUsersNearLondon(unittest.TestCase):
    """
    Asserts that the function to locate users near London returns expected results
    """

    def get_users_near_london(self):
        r = get_users_near_london() # to be replaced with actual coordinates within 50 miles
        self.assertIsNotNone(r)



if __name__ == '__main__':
    unittest.main()