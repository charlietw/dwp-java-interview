import unittest
from functions import *
from run import *


class TestInstructions(unittest.TestCase):
    """
    Asserts that the API can be called successfully
    """

    def setUp(self):
        pass

    def test_api_call(self):
        r = get_instructions()
        self.assertEqual(r.status_code, 200)

    def tearDown(self):
        pass


class TestUsers(unittest.TestCase):
    """
    Asserts that the API can be called successfully to get users
    """

    def setUp(self):
        pass

    def test_api_call(self):
        r = get_users()
        self.assertEqual(r.status_code, 200)

    def tearDown(self):
        pass


class TestLondonUsers(unittest.TestCase):
    """
    Asserts that the API can be called successfully to get users in London
    """

    def setUp(self):
        pass

    def test_api_call(self):
        r = get_london_users()
        self.assertEqual(r.status_code, 200)

    def tearDown(self):
        pass


class TestWithin50Miles(unittest.TestCase):
    """
    Asserts that the function to compare two coords works correctly
    """

    def setUp(self):
        pass

    def test_true_comparison(self):
        r = within_50_miles(user, 10, 20) # to be replaced with actual coordinates within 50 miles
        self.assertEqual(r, True)

    def test_false_comparison(self):
        r = within_50_miles(user, 10, 20) # to be replaced with actual coordinates outside of 50 miles
        self.assertEqual(r, False)

    def tearDown(self):
        pass


class TestUsersNearLondon(unittest.TestCase):
    """
    Asserts that the function to locate users near London returns expected results
    """

    def setUp(self):
        pass

    def get_users_near_london(self):
        r = get_users_near_london() # to be replaced with actual coordinates within 50 miles
        self.assertIsNotNone(r)


    def tearDown(self):
        pass




if __name__ == '__main__':
    unittest.main()