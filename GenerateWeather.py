##########################
# Author : Ragesh Narayanan
# Python Version: 3.6.1
# This code generates fake weather data with Location, Latitude, Longitude, Local Time,
# Weather condition, Temperature, Pressure and Humidity
##########################

import utils


# Returns the full weather data for all cities
def generate_weather_data(cities):
    full_weather_data = []
    for city in cities:
        latitude, longitude = utils.get_lat_and_lon()
        altitude = utils.get_altitude()
        local_time = utils.get_local_time()
        temperature = utils.get_temperature()
        pressure = utils.get_pressure()
        weather_condition = utils.get_condition(temperature)
        humidity = utils.get_humidity()

        entry = utils.create_weather_entry(city, latitude, longitude, altitude, local_time, weather_condition,
                             temperature, pressure, humidity)
        full_weather_data.append(entry)
    return full_weather_data


if __name__ == '__main__':
    city_names = utils.read_cities()
    final_weather_data = generate_weather_data(city_names)
    utils.write_data(final_weather_data)