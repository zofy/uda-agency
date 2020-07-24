import logging
import os
from typing import Dict, Optional

import flask
from flask_cors import CORS

from app import utils
from app.api import actors, app, movies
from app.db import models


def create_app(
    log_path: str, logger: logging.Logger, config: Optional[Dict] = None):
  """Creates a Flask app based on a configuration."""
  APP = flask.Flask(__name__, template_folder='app/templates/', static_folder='app/static/')
  utils.setup_logger(log_path, logger)
  if config is None:
    APP.config.from_object('config')
  else:
    APP.config.from_mapping(config)
  CORS(APP)
  APP.register_blueprint(app.agency_bp)
  APP.register_blueprint(actors.actors_bp)
  APP.register_blueprint(movies.movies_bp)
  return APP


APP = create_app('agency.log', app.LOGGER)
models.db.init_app(APP)


if __name__ == '__main__':
  APP.run(host='127.0.0.1', port=5000, debug=True)
