import sys

from flask import Flask
from config import Config

from api import ApiModule
from auth import *

app = Flask(__name__)

if __name__ == '__main__':
    config = Config(sys.argv[1])
    print("URLs:", app.url_map)

    api = ApiModule(app, config)

    credentials[config.auth["user"]] = config.auth["pwd"]

    app.run(host=config.host['bind'],
            port=config.host['port'],
            debug=config.host['debug'])