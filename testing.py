import unittest
from run import *
from geopy import distance as geopydistance  # for testing


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


class TestDistanceCalculation(unittest.TestCase):
    """
    Asserts that the function to compare two coords works correctly
    """

    def setUp(self):
        self.users = get_users_json()

    def test_with_example_data(self):
        """
        Takes all positive, whole integers as coordinates and
        compares with geopy
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
        self.assertTrue(diff < 105)
        self.assertTrue(diff > 95)  # asserts that deviation < 5%

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
        p1 = (x_1, y_1)  # formatting for geopy
        p2 = (x_2, y_2)
        distance_geopy = geopydistance.distance(p1, p2).miles
        diff = discrepency_between_calcs(distance, distance_geopy)
        self.assertTrue(diff < 105)
        self.assertTrue(diff > 95)  # asserts that deviation is < 5%

    def test_all_data(self):
        """
        Gets disrecepency for all data in source and asserts that no
        difference is > 5% from what is calculated by geopy.
        """
        count = 0  # count of inaccurate calculations
        london_lat = 51.509865
        london_lon = -0.118092
        london = (london_lat, london_lon)  # formatting for geopy
        for u in self.users:
            user_lat = u["latitude"]
            user_lon = u["longitude"]
            user = (user_lat, user_lon)  # formatting for geopy
            distance = calculate_distance(
                user_lat,
                user_lon,
                london_lat,
                london_lon)
            distance_geopy = geopydistance.distance(
                user,
                london).miles  # geopy calc
            diff = discrepency_between_calcs(distance, distance_geopy)
            if diff > 105 or diff < 95:  # if discrepency is > 5% then flag it
                count += 1
        print("count:", count)
        self.assertTrue(count == 0)  # to pass the test they all must be < 5%


class TestWithin50Miles(unittest.TestCase):
    """
    Asserts that the 'within 5 miles' function works as expected
    """

    def test_true_with_nearby(self):
        """
        Tests with coordinates very close together
        """
        lat_1 = 51.509865
        lon_1 = -0.118092
        lat_2 = 51.709865
        lon_2 = -0.118092
        self.assertTrue(within_50_miles(
            lat_1, lon_1, lat_2, lon_2)
        )

    def test_true_with_identical(self):
        """
        Tests with two identical coordinates
        """
        lat_1 = 51.509865
        lon_1 = -0.118092
        lat_2 = 51.509865
        lon_2 = -0.118092
        self.assertTrue(within_50_miles(
            lat_1, lon_1, lat_2, lon_2)
        )

    def test_false(self):
        """
        Tests with two identical coordinates
        """
        lat_1 = 51.509865
        lon_1 = -0.118092
        lat_2 = 55.509865
        lon_2 = -0.118092
        self.assertFalse(within_50_miles(
            lat_1, lon_1, lat_2, lon_2)
        )


class TestUsersNearLondon(unittest.TestCase):
    """
    Asserts that the function to locate users near
    London returns expected results.
    """

    def get_users_near_london(self):
        r = get_users_near_london()
        self.assertIsNotNone(r)

if __name__ == '__main__':
    unittest.main()
