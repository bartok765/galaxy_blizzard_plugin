import pathlib
import json

with open(pathlib.Path(__file__).parent / "manifest.json", 'r') as manifest:
    __version__ = json.load(manifest)['version']
