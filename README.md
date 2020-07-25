# Capstone Project Uda-Agency API Backend

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Database Setup
In Postgres create database called `agency` run:
```bash
python manage.py db upgrade
```

## Running the server

From within the `uda-agency` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
python run.py
```

## API Reference

### Endpoints:
- GET '/'
- GET '/login'
- GET '/logout'
- GET '/actors'
- GET '/movies'
- GET '/actors/{int:actor_id}'
- GET '/movies/{int:movie_id}'
- POST '/actors'
- POST '/movies'
- PATCH '/actors/{int:actor_id}'
- PATCH '/movies/{int:movie_id}'
- DELETE '/actors/{int:actor_id}'
- DELETE '/movie/{int:movie_id}'


### GET '/'
    Index page for the uda-agency. On this pgae user can login/logout. After successful login, jwt is
    displayed on the page.
- Request Arguments: `None`
- Returns: `None`

### GET '/login'
    This redirects user to the auth0 login page.

### GET '/logout'
    This logs out user, clears the session.

### GET '/actors'
    Fetches list of paginated actors. If there are no actors, `404` response is returned.
- Request Arguments: `None`
- Returns: JSON with the following keys:
    - `success`: true/false
    - `actors`: list of formated actors (paginated)
    - `total_actors_count`: total number of questions

```python
{
    "actors": [
        {
            "age": 26,
            "first_name": "Anya",
            "gender": "FEMALE",
            "id": 2,
            "last_name": "Barrick"
        },
        {
            "age": 22,
            "first_name": "John",
            "gender": "MALE",
            "id": 3,
            "last_name": "Wick"
        },
    ],
    "success": true,
    "total_actors_count": 2
}
```

### GET '/movies'
    Fetches list of paginated movies. If there are no movies, `404` response is returned.
- Request Arguments: `None`
- Returns: JSON with the following keys:
    - `success`: true/false
    - `movies`: list of formated movies (paginated)
    - `total_movies_count`: total number of movies

```python
{
    "movies": [
        {
            "id": 1,
            "title": "The Lion",
            "release_date": "Fri, 24 Jul 2020 23:58:36 GMT",
        },
    ],
    "success": true,
    "total_movies_count": 1
}
```

### GET '/actors/{int:actor_id}'
    Returns formatted actor given by provided `actor_id`. If no actor with specified id is found, `404` response is returned.
- Request Arguments: `actor_id[int]`
- Returns: JSON with the following keys:
    - `success`: true/false
    - `actor`: formated actor

```python
{
    "actor": {
        "age": 26,
        "first_name": "Anya",
        "gender": "FEMALE",
        "id": 2,
        "last_name": "Barrick"
    },
    "success": true
}
```

### GET '/movies/{int:movie_id}'
    Returns formatted movie given by provided `movie_id`. If no movie with specified id is found, `404` response is returned.
- Request Arguments: `movie_id[int]`
- Returns: JSON with the following keys:
    - `success`: true/false
    - `actor`: formated movie

```python
{
    "movie": {
        "id": 1,
        "title": "The Lion",
        "release_date": "Fri, 24 Jul 2020 23:58:36 GMT",
    },
    "success": true
}
```

### DELETE '/actors/{int:actor_id}'
    Deletes actor with a given id. If no such actor exists, `422` is returned.
- Request Arguments: `actor_id[int]`
- Returns: JSON with the following keys:
    - `success`: true/false
    - `deleted_id`: id of a deleted actor

### DELETE '/movies/{int:movie_id}'
    Deletes movie with a given id. If no such movie exists, `422` is returned.
- Request Arguments: `movie_id[int]`
- Returns: JSON with the following keys:
    - `success`: true/false
    - `deleted_id`: id of a deleted movie

### POST '/actors'
    Creates an actor. If invalid data are provided: `422` response is returned.
- Request Arguments: JSON containing (all required):
    - `first_name`
    - `last_name`
    - `age`
    - `gender`
- Returns JSON with the following keys:
    - `success`: true/false
    - `created_id`: id of created actor

### POST '/movies'
    Creates a movie. If invalid data are provided: `422` response is returned.
    In case of missing required params, `400` is returned.
- Request Arguments: JSON containing (all required):
    - `title`
    - `release_date` (in the format: `YYYY-MM-DD`)
- Returns JSON with the following keys:
    - `success`: true/false
    - `created_id`: id of created movie

### PATCH '/actors/{int:actor_id}'
    Updates an actor. If invalid data are provided: `422` response is returned.
    In case of non-existing actor, `404` is returned.
- Request Arguments: JSON containing (all optional):
    - `first_name`
    - `last_name`
    - `age`
    - `gender`
- Returns JSON with the following keys:
    - `success`: true/false
    - `updated_id`: id of created actor

### PATCH '/movies/{int:movie_id}'
    Updates a movie. If invalid data are provided: `422` response is returned.
    In case of non-existing movie, `404` is returned.
- Request Arguments: JSON containing (all optional):
    - `title`
    - `release_date` (in the format: `YYYY-MM-DD`)
- Returns JSON with the following keys:
    - `success`: true/false
    - `updated_id`: id of created actor


## Testing
To run the tests make sure to have valid `JWTs` in the `tests/test_permissions.py`.
In order to obtain valid tokens, navigate to: `https://uda-agency.herokuapp.com/` and login with
different roles:

#### Roles credentials:
- `assistant`: assistant@agency.com [UDACITY_fullstack]
- `director`: director@agency.com [UDACITY_fullstack]
- `producer`: producer@agency.com [UDACITY_fullstack]

After successful login, you'll see token displayed on the page.
With all of the valid tokens, run:
```
python test_app.py
```