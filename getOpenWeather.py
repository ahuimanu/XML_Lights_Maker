from operator import eq
import re
import os
import click
import requests
from dotenv import load_dotenv

# tutorial reference: https://dbader.org/blog/mastering-click-advanced-python-command-line-apps
# census geocoder


# get API key
load_dotenv()
APIKEY = os.getenv('APIKEY')

class OpenWeatherMapApiKey(click.ParamType):
    name = 'api-key'

    def convert(self, value, param, ctx):
        found = re.match(r'[0-9a-f]{32}', value)

        #api key invalid
        if not found:
            self.fail(f'{value} is not a valid 32-char hex string', param, ctx)

        return value

def current_weather(lat, lon, api_key=APIKEY):
    # open weather map: https://openweathermap.org/current#one

    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={APIKEY}&units=metric'
    response = requests.get(url)
    weather_data = response.json()
    description = weather_data['weather'][0]['description']
    temperature = weather_data['main']['temp']

    return f"temperature: {temperature} C, description: {description}"
    

def get_geocode(location):
    """
    geolocation from OSM and nominatum: https://nominatim.org/release-docs/develop/api/Search/
    """
    lat = ''
    lon = ''

    url = f'https://nominatim.openstreetmap.org/search?q={location}&format=json'

    response = requests.get(url)
    locations = response.json()
    place = locations[0]['display_name']
    lat = locations[0]['lat']
    lon = locations[0]['lat']
    output = f"position for: {place} lat:{lat} lon:{lon}"
    click.echo(output)
    return lat, lon

@click.command()
@click.argument('location')
def main(location):
    lat, lon = get_geocode(location)
    weather = current_weather(lat, lon, APIKEY)
    click.echo(weather)

if __name__ == '__main__':
    main()