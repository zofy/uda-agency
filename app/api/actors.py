import flask

from app.api.app import ITEMS_PER_PAGE, LOGGER
from app.auth import auth
from app.db.models import Actor
from app.utils import paginate

actors_bp = flask.Blueprint('actors_bp', __name__)

####################
### Actors views ###
####################

@actors_bp.route('/actors')
@auth.requires_auth('get:actors')
def all_actors(payload):
    actors_count = Actor.query.count()
    actors = paginate(flask.request, Actor.query.all(), ITEMS_PER_PAGE)
    if not actors:
        flask.abort(404)
    return flask.jsonify({
        'success': True, 
        'actors': [a.format() for a in actors], 
        'total_actors_count': actors_count,
    })


@actors_bp.route('/actors/<int:actor_id>')
@auth.requires_auth('get:actors-details')
def get_actor(payload, actor_id: int):
    actor = Actor.query.filter(Actor.id == actor_id).one_or_none()
    if not actor:
        LOGGER.debug(f'Actor with id: {actor_id} not found.')
        flask.abort(404)
    return flask.jsonify({
        'success': True,
        'actor': actor.format(),
    })  


@actors_bp.route('/actors', methods=['POST'])
@auth.requires_auth('post:actors')
def create_actor(payload):
    data = flask.request.get_json()
    LOGGER.debug(f'Creating actor with: {data}')
    try:
        actor = Actor(**data)
        actor.insert()
    except Exception as e:
        LOGGER.exception(f'Failed to create a new actor with: {e}')
        flask.abort(422)
    else:
        return flask.jsonify({
            'success': True,
            'created_id': actor.id,
        })


@actors_bp.route('/actors/<int:actor_id>', methods=['DELETE'])
@auth.requires_auth('delete:actors')
def delete_actor(payload, actor_id: int):
    actor = Actor.query.filter(Actor.id == actor_id).one_or_none()
    LOGGER.debug(f'Deleting actor with id: {actor_id}')
    try:
        actor.delete()
    except Exception as e:
        LOGGER.exception(f'Failed to delete an actor with: {e}')
        flask.abort(422)
    else:
        return flask.jsonify({
            'success': True,
            'deleted_id': actor_id,
        })


@actors_bp.route('/actors/<int:actor_id>', methods=['PATCH'])
@auth.requires_auth('patch:actors')
def update_actor(payload, actor_id: int):
    actor = Actor.query.filter(Actor.id == actor_id).one_or_none()
    if not actor:
        flask.abort(404)
    data_to_update = flask.request.get_json()
    LOGGER.debug(f'Updating actor with: {data_to_update}')
    try:
        actor.update_by_mapping(data_to_update)
    except Exception as e:
        LOGGER.exception(f'Failed to update actor with: {e}')
        flask.abort(422)
    else:
        return flask.jsonify({
            'success': True,
            'updated_id': actor.id,
        })


#####################
### Handle Errors ###
#####################

@actors_bp.errorhandler(404)
def not_found(error):
    return flask.jsonify({
            "success": False, 
            "error": 404,
            "message": "resource not found",
            }), 404


@actors_bp.errorhandler(400)
def bad_request(error):
    return flask.jsonify({
            "success": False, 
            "error": 400,
            "message": "bad request",
            }), 400


@actors_bp.errorhandler(422)
def unprocessable(error):
    return flask.jsonify({
            "success": False, 
            "error": 422,
            "message": "could not process",
            }), 422


@actors_bp.errorhandler(500)
def server_error(error):
    return flask.jsonify({
            "success": False, 
            "error": 500,
            "message": "internal server error",
            }), 500


@actors_bp.errorhandler(401)
def unauthorized(error):
    return flask.jsonify({
            "success": False, 
            "error": 401,
            "message": "authentication failed",
            }), 401


@actors_bp.errorhandler(403)
def forbidden(error):
    return flask.jsonify({
            "success": False, 
            "error": 403,
            "message": "authorization failed",
            }), 403
