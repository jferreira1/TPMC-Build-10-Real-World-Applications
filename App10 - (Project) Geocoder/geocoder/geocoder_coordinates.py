from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderServiceError
import pandas as pd

def get_Latitude(addr):
    geolocator = Nominatim(user_agent='jferreira_geocoder', timeout=1)
    try:
        return geolocator.geocode(addr, language='pt').latitude
    except Exception as e:
        return exception_Latitude_Longitude(e)

def get_Longitude(addr):
    geolocator = Nominatim(user_agent='jferreira_geocoder')
    try:
        return geolocator.geocode(addr, language='pt').longitude
    except Exception as e:
        return exception_Latitude_Longitude(e)
    

def exception_Latitude_Longitude(e):
    if type(e) == GeocoderTimedOut:
        lat_lon = lat_lon_message_error()
        return lat_lon
    elif type(e) == GeocoderServiceError:
        lat_lon = lat_lon_message_error()
        return lat_lon
    elif type(e) == AttributeError:
        lat_lon = lat_lon_message_error()
        return lat_lon

def lat_lon_message_error():
    message = 'Not Found'
    return message

def csv_coordinates(file):
    with open('./geocoder/address.csv') as file:
        df = pd.read_csv(file)
        df.columns = map(str.lower, df.columns)
        df['latitude'] = df.address.apply(get_Latitude)
        df['longitude'] = df.address.apply(get_Longitude)
        df.to_csv('./geocoder/addresses_updated.csv', index=True)
        return df