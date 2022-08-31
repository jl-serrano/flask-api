from flask import Flask
import logging as logger
logger.basicConfig(level="DEBUG")

App = Flask(__name__)


if __name__ == "__main__":
    logger.debug("Starting Application...")

    from api import *
    App.run(debug=True, use_reloader=True)
