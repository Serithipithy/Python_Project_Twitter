"""Map Generator Service

This script allows the user to put a pin on a map based on coordinates
using the folium library using the json file named "tweets_info.json"
that must be included in a folder "data". Every pin will have a popup
when the user clicks on it and will contain different information
about a tweet.

This tool accepts just json files

This script requires that `folium` be installed within the Python
environment you are running this script in.

This file can also be imported as a module and contains the following
functions:

    * mark_on_map - marks the pin on the map
    * generate_map - populates the map with in information from the
    json file
"""
import json

import folium as folium

"""
    Global settings
"""
map = folium.Map(location=[45, 0], zoom_start=2, tiles='cartodbdark_matter')
tooltip = "Click for more info"


def mark_on_map(info):
    """
    Marks the pin on the map with the additional information: author,
    date and content

    Parameters
    ----------
    :param info: list
        The list that contains the coordinates and other information
        needed to be plotted on the map
    """
    if info["coordinates"][0] != 0 or info["coordinates"][1] != 0:
        folium.Marker([info["coordinates"][0], info["coordinates"][1]],
                      popup=folium.Popup(
                          html='<style type="text/css" scoped> .leaflet-popup-content-wrapper { width: 250px }</style>'
                               f'<h5><strong>{info["author"]}\'s tweet</strong></h5>'
                               f'</br>'
                               f'<small>'
                               f'Created on: {info["date"]["day"]}.{info["date"]["month"]}.{info["date"]["year"]}'
                               f'</small> '
                               f'</br>'
                               f'<h6><strong>{info["text"]}</strong></h6>',
                      ),
                      tooltip=tooltip,
                      icon=folium.Icon(icon="globe", color="lightblue")).add_to(map)


def generate_map():
    """
    Populates the map with in information from the json file. The
    generated file will be located in a folder named "data" and it
    will contain the map html

    """
    with open("./data/tweets_info.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        for chunk in data["info"]:
            mark_on_map(chunk)
        map.save("../data/tweets_map.html")

