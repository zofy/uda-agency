import logging
import urllib
from datetime import datetime

import flask

from app.auth import auth
from app.utils import paginate

ITEMS_PER_PAGE = 5
LOGGER = logging.getLogger(__name__)
agency_bp = flask.Blueprint("agency_bp", __name__)


@agency_bp.route("/login")
def login():
    params = {
        "audience": auth.API_AUDIENCE,
        "response_type": "token",
        "client_id": auth.API_CLIENT_ID,
        "redirect_uri": flask.url_for("agency_bp.index", _external=True),
    }
    url = auth.API_BASE_URL + "/authorize?" + urllib.parse.urlencode(params)
    return flask.redirect(url)


@agency_bp.route("/logout")
def logout():
    flask.session.clear()
    params = {
        "client_id": auth.API_CLIENT_ID,
        "returnTo": flask.url_for("agency_bp.index", _external=True),
    }
    url = auth.API_BASE_URL + "/v2/logout?" + urllib.parse.urlencode(params)
    return flask.redirect(url)


@agency_bp.route("/")
def index():
    return flask.render_template("index.html")


#####################
#   Handle Errors   #
#####################


@agency_bp.errorhandler(404)
def not_found(error):
    return (
        flask.jsonify(
            {"success": False, "error": 404, "message": "resource not found"}
        ),
        404,
    )


@agency_bp.errorhandler(400)
def bad_request(error):
    return (
        flask.jsonify({
            "success": False, "error": 400, "message": "bad request"
        }), 400,
    )


@agency_bp.errorhandler(500)
def server_error(error):
    return (
        flask.jsonify({
            "success": False, "error": 500, "message": "internal server error"
        }), 500,
    )
