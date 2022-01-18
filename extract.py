"""Extract data on near-Earth objects and close approaches from CSV and JSON files."""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    
    with open(neo_csv_path, 'r') as f:
        neos = []
        neoreader = csv.reader(f)
        h = next(neoreader)
        for neo in neoreader:
            neos.append(NearEarthObject(designation = neo[h.index('pdes')], 
                                                        name = neo[h.index('name')], 
                                                        diameter = neo[h.index('diameter')],
                                                        hazardous= neo[h.index('pha')]))
    return neos



def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param neo_csv_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    with open(cad_json_path, 'r') as f:
        cads = []
        cadreader = json.load(f)
        h = cadreader['fields']
        for cad in cadreader['data']:
            cads.append(CloseApproach(designation = cad[h.index('des')],
                                        time = cad[h.index('cd')],
                                        distance = cad[h.index('dist')],
                                        velocity = cad[h.index('v_rel')]))
    return cads
