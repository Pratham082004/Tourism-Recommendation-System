"""
Service layer for interacting with the OpenTripMap external API.

Handles geographic data. including coordinates, raduis-based attraction discovery
and detailed point of interest information.
"""

import requests
from config import Config
from utils.logger import logger

class Opentripmap_service:

    """ Service class for OpenTripMap API communication. """

    BASE_URL = "https://api.opentripmap.com/0.1/en/places"

    @staticmethod
    def fetch_cordinates(city):
        """ Fetches geographic coordinates for a given city. """
        url = f"{Opentripmap_service.BASE_URL}/geoname"
        params = {
            "name": city,
            "apikey": Config.OPENTRIP_API_KEY
        }

        logger.debug("OpenTripMap: fetch_cordinates url=%s name=%s", url, city)
        response = requests.get(url, params=params)

        if response.status_code != 200:
            logger.error("OpenTripMap fetch_cordinates failed status=%s", response.status_code)
            raise Exception("Unable to fetch city coordinates.")
        
        return response.json()

    
    @staticmethod
    def fetch_nearby_attaractions(lat,lon,radius=8000,limit=5):
        """ Fetches point of interests within a specific raduis. """
        url = f"{Opentripmap_service.BASE_URL}/radius"
        params = {
            "radius": radius,
            "lon": lon,
            "lat": lat,
            "limit": limit,
            "format": "json",
            "apikey": Config.OPENTRIP_API_KEY
        }
        logger.debug("OpenTripMap: fetch_nearby_attaractions lat=%s lon=%s radius=%s limit=%s", lat, lon, radius, limit)
        response = requests.get(url,params=params)

        if response.status_code != 200:
            logger.error("OpenTripMap fetch_nearby_attaractions failed status=%s", response.status_code)
            raise Exception("Unable to fetch nearby attractions.")
        return response.json()


    @staticmethod
    def fetch_place_details(xid):
        """ Fetches details for a specific attraction. """
        url = f"{Opentripmap_service.BASE_URL}/xid/{xid}"
        params = {"apikey": Config.OPENTRIP_API_KEY}

        logger.debug("OpenTripMap: fetch_place_details xid=%s", xid)
        response = requests.get(url, params=params)

        if response.status_code != 200:
            logger.error("OpenTripMap fetch_place_details failed status=%s", response.status_code)
            raise Exception("Unable to fetch place details.")

        return response.json()

