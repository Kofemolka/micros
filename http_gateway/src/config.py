import json

class Config(object):
    def __init__(self, config_file_name):
        with open(config_file_name) as config_file:
            self.__dict__ = json.load(config_file)