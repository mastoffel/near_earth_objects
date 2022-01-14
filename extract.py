"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    
    with open(neo_csv_path, 'r') as f:
        neos = {}
        neoreader = csv.reader(f)
        h = next(neoreader)
        for neo in neoreader:
            neos[neo[h.index('pdes')]] = NearEarthObject(designation = neo[h.index('pdes')], 
                                                        name = neo[h.index('name')], 
                                                        diameter = neo[h.index('diameter')],
                                                        hazardous= neo[h.index('pha')]) 
    return neos



def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param neo_csv_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    with open(cad_json_path, 'r') as f:
        cadreader = json.load(f)
    return cadreader
