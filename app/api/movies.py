from datetime import datetime

import flask

from app.api.app import ITEMS_PER_PAGE, LOGGER
from app.auth import auth
from app.db.models import DATE_FORMAT, Movie
from app.utils import paginate

movies_bp = flask.Blueprint("movies_bp", __name__)


####################
#   Movies views   #
####################


@movies_bp.route("/movies")
@auth.requires_auth("get:movies")
def all_movies(payload):
    movies_count = Movie.query.count()
    movies = paginate(flask.request, Movie.query.all(), ITEMS_PER_PAGE)
    if not movies:
        flask.abort(404)
    return flask.jsonify(
        {
            "success": True,
            "movies": [m.format() for m in movies],
            "total_movies_count": movies_count,
        }
    )


@movies_bp.route("/movies/<int:movie_id>")
@auth.requires_auth("get:movies-details")
def get_movie(payload, movie_id: int):
    movie = Movie.query.filter(Movie.id == movie_id).one_or_none()
    if not movie:
        LOGGER.debug(f"Movie with id: {movie_id} not found.")
        flask.abort(404)
    return flask.jsonify({"success": True, "movie": movie.format()})


@movies_bp.route("/movies", methods=["POST"])
@auth.requires_auth("post:movies")
def create_movie(payload):
    data = flask.request.get_json()
    if "title" not in data or "release_date" not in data:
        flask.abort(400)
    release_date = data["release_date"]
    movie_data = {
        "title": data["title"],
        "release_date": datetime.strptime(release_date, DATE_FORMAT),
    }
    LOGGER.debug(f"Creating movie with: {movie_data}")
    try:
        movie = Movie(**movie_data)
        movie.insert()
    except Exception as e:
        LOGGER.exception(f"Failed to create a movie with: {e}")
        flask.abort(422)
    else:
        return flask.jsonify({"success": True, "created_id": movie.id})


@movies_bp.route("/movies/<int:movie_id>", methods=["DELETE"])
@auth.requires_auth("delete:movies")
def delete_movie(payload, movie_id):
    movie = Movie.query.filter(Movie.id == movie_id).one_or_none()
    LOGGER.debug(f"Deleting movie with id: {movie_id}")
    try:
        movie.delete()
    except Exception as e:
        LOGGER.exception(f"Failed to delete a movie with: {e}")
        flask.abort(422)
    else:
        return flask.jsonify({"success": True, "deleted_id": movie_id})


@movies_bp.route("/movies/<int:movie_id>", methods=["PATCH"])
@auth.requires_auth("patch:movies")
def update_movie(payload, movie_id: int):
    movie = Movie.query.filter(Movie.id == movie_id).one_or_none()
    if not movie:
        flask.abort(404)
    data_to_update = flask.request.get_json()
    LOGGER.debug(f"Updating movie with: {data_to_update}")
    try:
        movie.update_by_mapping(data_to_update)
    except Exception as e:
        LOGGER.exception(f"Failed to update movie with: {e}")
        flask.abort(422)
    else:
        return flask.jsonify({"success": True, "updated_id": movie.id})


#####################
#   Handle Errors   #
#####################


@movies_bp.errorhandler(404)
def not_found(error):
    return (
        flask.jsonify(
            {"success": False, "error": 404, "message": "resource not found"}
        ),
        404,
    )


@movies_bp.errorhandler(400)
def bad_request(error):
    return (
        flask.jsonify({
            "success": False, "error": 400, "message": "bad request"
        }),
        400,
    )


@movies_bp.errorhandler(422)
def unprocessable(error):
    return (
        flask.jsonify(
            {"success": False, "error": 422, "message": "could not process"}
        ),
        422,
    )


@movies_bp.errorhandler(500)
def server_error(error):
    return (
        flask.jsonify({
            "success": False, "error": 500, "message": "internal server error"
        }),
        500,
    )


@movies_bp.errorhandler(401)
def unauthorized(error):
    return (
        flask.jsonify({
            "success": False, "error": 401, "message": "authentication failed"
        }),
        401,
    )


@movies_bp.errorhandler(403)
def forbidden(error):
    return (
        flask.jsonify({
            "success": False, "error": 403, "message": "authorization failed"
        }),
        403,
    )
