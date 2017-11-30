##########################
# Author: Ragesh Narayanan
# Utility functions for generating fake weather data
##########################

import random
import os
import sys
from datetime import timedelta
import StaticVariables as SV


# Returns random temperature
def get_temperature():
    temperature = random.randint(SV.MinTemperature, SV.MaxTemperature)
    return temperature


# Returns random latitude and longitude
def get_lat_and_lon():
    latitude = "{0:.6f}".format(random.uniform(SV.MinLatitude, SV.MaxLatitude))
    longitude = "{0:.6f}".format(random.uniform(SV.MinLongitude, SV.MaxLongitude))
    return latitude, longitude


# Returns random Altitude
def get_altitude():
    altitude = "{0:.2f}".format(random.uniform(SV.MinAltitude, SV.MaxAltitude))
    return altitude


# Returns random date/time
def get_local_time():
    hours = random.randint(0, 24)
    minutes = random.randint(0, 60)
    seconds = random.randint(0, 60)
    local_time = SV.Day + timedelta(hours=hours, minutes=minutes, seconds=seconds)
    return local_time


# Return weather condition based on temperature provided
def get_condition(temperature):
    temp = int(temperature)
    if (temp < 10):
        return "Snow"
    elif (temp > 10 and temp < 30):
        return "Rain"
    else:
        return "Sunny"


# Returns random pressure value
def get_pressure():
    pressure = "{0:.1f}".format(random.uniform(SV.MinPressure, SV.MaxPressure))
    return pressure


# Returns random humidity
def get_humidity():
    humidity = int(random.uniform(SV.MinHumidity, SV.MaxHumidity))
    return humidity


# Reads the text file with city names
def read_cities():
    cities = []
    input_path = 'input/cities'
    if os.path.exists(input_path):
        f = open(input_path, "r")
        for city_name in f:
            city_name = city_name.strip()
            cities.append(city_name)
        f.close()
        return cities
    else:
        print("Input file doesn't exists")
        sys.exit(1)


# Writes the weather data to output file
def write_data(data):
    output_path = "output/weather_data_output"
    if not os.path.exists(output_path):
        print("Output file doesn't exists")
    else:
        f = open(output_path, "w")
        for entry in data:
            f.write(entry + "\n")
        f.close()


# Returns a string combining all the data for a particular city
def create_weather_entry(city=None, latitude=None, longitude=None, altitude=None,
                         local_time=None, weather_condition=None, temperature=None,
                         pressure=None, humidity=None):

    full_entry = city + " | " + str(latitude) + "," + str(longitude) + "," + str(altitude) + " | " + local_time.isoformat() \
                 + " | " + weather_condition + " | " + str(temperature) + " | " + str(pressure) + " | " + str(humidity)
    return full_entry
