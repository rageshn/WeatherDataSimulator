##########################
# Author: Ragesh Narayanan
# Unit test cases for the weather data
##########################

import unittest
import utils
import re


class WeatherDataTestCase(unittest.TestCase):

    # Checks whether the method returns both latitude and longitude
    def test_lat_lon(self):
        self.assertEqual(len(utils.get_lat_and_lon()), 2)

    # Checks whether latitude is in proper format
    def test_latitude_format(self):
        latitude_regex = "^(\\+|-)?(?:90(?:(?:\\.0{1,6})?)|(?:[0-9]|[1-8][0-9])(?:(?:\\.[0-9]{1,6})?))$"
        latitude, longitude = utils.get_lat_and_lon()
        self.assertEqual(bool(re.match(latitude_regex, latitude)), True)

    # Checks whether longitude is in proper format
    def test_longitude_format(self):
        longitude_regex = "^(\\+|-)?(?:180(?:(?:\\.0{1,6})?)|(?:[0-9]|[1-9][0-9]|1[0-7][0-9])(?:(?:\\.[0-9]{1,6})?))$"
        latitude, longitude = utils.get_lat_and_lon()
        self.assertEqual(bool(re.match(longitude_regex, longitude)), True)

    # Checks whether the altitude is within range
    def test_altitude(self):
        alt = utils.get_altitude()
        self.assertGreater(float(alt), 0)
        self.assertLess(float(alt), 5000)

    # Checks whether the temperature is within range
    def test_temperature(self):
        temp = utils.get_temperature()
        self.assertGreater(float(temp), -10)
        self.assertLess(float(temp), 50)

    # Checks whether the weather condition is returned properly
    def test_condition(self):
        snow = utils.get_condition(-10)
        self.assertEqual(snow.lower(), "snow")

        rain = utils.get_condition(25)
        self.assertEqual(rain.lower(), "rain")

        sunny = utils.get_condition(40)
        self.assertEqual(sunny.lower(), "sunny")

    # Checks whether the temperature is within range
    def test_pressure(self):
        pressure = utils.get_pressure()
        self.assertEqual(350 < float(pressure) < 1000, True)

    # Checks whether the temperature is within range
    def test_humidity(self):
        humidity = utils.get_humidity()
        self.assertEqual(0 < float(humidity) < 100, True)

    # Checks whether the input file has at least 1 city
    def test_cities_count(self):
        cities = utils.read_cities()
        self.assertEqual(len(cities) > 1, True)


if __name__ == '__main__':
    WeatherDataTestCase.main()
