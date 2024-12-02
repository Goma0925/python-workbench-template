import json

import pandas as pd
from app.config.file import INPUT_DIR, OUTPUT_DIR


def read_geojson():
    input_file = INPUT_DIR.joinpath("zurich-route.geojson")
    data = {}
    with open(input_file, "r") as f:
        data = json.load(f)
    return data


def read_coordinates():
    input_file = INPUT_DIR.joinpath("coordinates.json")
    data = {}
    with open(input_file, "r") as f:
        data = json.load(f)
    return data


def save_geojson(data: dict):
    out_file = OUTPUT_DIR.joinpath("weather-data-route.geojson")
    with open(out_file, "w") as f:
        f.write(json.dumps(data))


def test_print():
    print("Hello")
