import json
import os
dir_path = os.path.dirname(os.path.realpath(__file__))

COMMON_PORTS_FILE = dir_path + '/ports.json'

common_ports = None
with open(COMMON_PORTS_FILE) as ports_json:
    d = json.load(ports_json)
    common_ports = d['ports']
