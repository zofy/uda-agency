import json
from unittest.mock import patch

from app.api import app

from .utils import TestAgencyMixin, actors_data, movies_data


class TestAgency(TestAgencyMixin):
    """Tests api of uda-agency"""

    @classmethod
    def setUpClass(cls):
        # mock requires_auth
        cls.patchers = [
            patch("app.auth.auth.get_token_auth_header"),
            patch("app.auth.auth.verify_decode_jwt"),
            patch("app.auth.auth.check_permissions"),
        ]
        for patcher in cls.patchers:
            patcher.start()

    @classmethod
    def tearDownClass(cls):
        for patcher in cls.patchers:
            patcher.stop()

    ##############################################
    #                Actors tests                #
    ##############################################

    def test_get_paginated_actors(self):
        res = self.client().get("/actors?page=1")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["success"])
        self.assertTrue(len(data["actors"]))
        self.assertEqual(data["total_actors_count"], len(actors_data))
        self.assertLessEqual(len(data["actors"]), app.ITEMS_PER_PAGE)

        # non existing page
        res = self.client().get("/actors?page=1000")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data["success"])
        self.assertEqual(data["message"], "resource not found")

    def test_get_actor(self):
        res = self.client().get("/actors/1")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["success"])
        actor = data["actor"]
        self.assertEqual(actor["id"], 1)
        self.assertEqual(actor["first_name"], "Anya")
        self.assertEqual(actor["gender"], "FEMALE")

    def test_actor_not_found(self):
        res = self.client().get("/actors/1000")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data["success"])
        self.assertEqual(data["message"], "resource not found")

    def test_create_actor(self):
        res = self.client().get("/actors")
        count_before = json.loads(res.data)["total_actors_count"]

        data = {"first_name": "Matt", "last_name": "Gail", "age": 42,
                "gender": "MALE"}
        res = self.client().post("/actors", json=data)
        res_data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(res_data["created_id"], len(actors_data) + 1)
        res = self.client().get("/actors")
        count_after = json.loads(res.data)["total_actors_count"]
        self.assertEqual(count_after, count_before + 1)

    def test_fail_to_create_actor(self):
        # gender is missing
        data = {"first_name": "Matt", "last_name": "Gail", "age": 42}
        res = self.client().post("/actors", json=data)
        res_data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertFalse(res_data["success"])

    def test_method_not_allowed(self):
        res = self.client().delete("/actors")
        self.assertEqual(res.status_code, 405)

    def test_delete_actor(self):
        res = self.client().get("/actors")
        count_before = json.loads(res.data)["total_actors_count"]
        self.assertTrue(count_before > 0)

        res = self.client().delete("/actors/1")
        res_data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res_data["deleted_id"], 1)

        res = self.client().get("/actors")
        count_after = json.loads(res.data)["total_actors_count"]
        self.assertEqual(count_after, count_before - 1)

    def test_delete_non_existing_actor(self):
        res = self.client().delete("/actors/1000")
        res_data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertFalse(res_data["success"])
        self.assertEqual(res_data["message"], "could not process")

    def test_update_actor(self):
        actor_id = 3
        # get actor with id = 3
        res = self.client().get(f"/actors/{actor_id}")
        actor = json.loads(res.data)["actor"]
        self.assertEqual(actor["first_name"], "Ema")

        # update first_name of the actor
        actor.pop("id")
        actor["first_name"] = "Emanuela"
        res = self.client().patch(f"/actors/{actor_id}", json=actor)
        self.assertEqual(res.status_code, 200)
        res_data = json.loads(res.data)
        self.assertTrue(res_data["success"])
        self.assertEqual(res_data["updated_id"], actor_id)

        # get actor with id = 3 again
        res = self.client().get(f"/actors/{actor_id}")
        updated_actor = json.loads(res.data)["actor"]
        updated_actor.pop("id")

        self.assertEqual(updated_actor["first_name"], "Emanuela")
        self.assertDictEqual(actor, updated_actor)

    def test_fail_to_update_actor(self):
        res = self.client().patch("/actors/1", json={"weight": 80})
        self.assertEqual(res.status_code, 422)
        res_data = json.loads(res.data)
        self.assertFalse(res_data["success"])
        self.assertEqual(res_data["message"], "could not process")

    def test_update_non_existing_actor(self):
        data = {"last_name": "Bubak"}
        res = self.client().patch("/actors/1000", json=data)
        self.assertEqual(res.status_code, 404)
        res_data = json.loads(res.data)
        self.assertFalse(res_data["success"])
        self.assertEqual(res_data["message"], "resource not found")

    ##############################################
    #                Movies tests                #
    ##############################################

    def test_get_paginated_movies(self):
        res = self.client().get("/movies?page=1")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["success"])
        self.assertTrue(len(data["movies"]))
        self.assertEqual(data["total_movies_count"], len(movies_data))
        self.assertLessEqual(len(data["movies"]), app.ITEMS_PER_PAGE)

        # non existing page
        res = self.client().get("/movies?page=1000")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data["success"])
        self.assertEqual(data["message"], "resource not found")

    def test_get_movie(self):
        res = self.client().get("/movies/1")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["success"])
        movie = data["movie"]
        self.assertEqual(movie["id"], 1)
        self.assertEqual(movie["title"], "Lions Heart")

    def test_movie_not_found(self):
        res = self.client().get("/movies/1000")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data["success"])
        self.assertEqual(data["message"], "resource not found")

    def test_create_movie(self):
        res = self.client().get("/movies")
        count_before = json.loads(res.data)["total_movies_count"]
        data = {"title": "Brand New", "release_date": "2033-03-11"}
        res = self.client().post("/movies", json=data)
        res_data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(res_data["created_id"], len(movies_data) + 1)
        res = self.client().get("/movies")
        count_after = json.loads(res.data)["total_movies_count"]
        self.assertEqual(count_after, count_before + 1)

    def test_fail_to_create_movie(self):
        # release_date is missing
        data = {"title": "Missing Release Date"}
        res = self.client().post("/movies", json=data)
        res_data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertFalse(res_data["success"])

    def test_delete_movie(self):
        res = self.client().get("/movies")
        count_before = json.loads(res.data)["total_movies_count"]
        self.assertTrue(count_before > 0)

        res = self.client().delete("/movies/1")
        res_data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res_data["deleted_id"], 1)

        res = self.client().get("/movies")
        count_after = json.loads(res.data)["total_movies_count"]
        self.assertEqual(count_after, count_before - 1)

    def test_delete_non_existing_movie(self):
        res = self.client().delete("/movies/1000")
        res_data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertFalse(res_data["success"])
        self.assertEqual(res_data["message"], "could not process")

    def test_update_movie(self):
        movie_id = 2
        # get movie with id = 2
        res = self.client().get(f"/movies/{movie_id}")
        movie = json.loads(res.data)["movie"]
        self.assertEqual(movie["title"], "The Old Guard")

        # update title of the movie
        to_update = {"title": "The New Guard"}
        res = self.client().patch(f"/movies/{movie_id}", json=to_update)
        self.assertEqual(res.status_code, 200)
        res_data = json.loads(res.data)
        self.assertTrue(res_data["success"])
        self.assertEqual(res_data["updated_id"], movie_id)

        # get movie with id = 2 again
        res = self.client().get(f"/movies/{movie_id}")
        updated_movie = json.loads(res.data)["movie"]

        self.assertEqual(updated_movie["title"], "The New Guard")
        self.assertEqual(updated_movie["release_date"], movie["release_date"])

    def test_fail_to_update_movie(self):
        res = self.client().patch("/movies/1", json={"rank": 5})
        self.assertEqual(res.status_code, 422)
        res_data = json.loads(res.data)
        self.assertFalse(res_data["success"])
        self.assertEqual(res_data["message"], "could not process")

    def test_update_non_existing_movie(self):
        data = {"title": "Bad"}
        res = self.client().patch("/movies/1000", json=data)
        self.assertEqual(res.status_code, 404)
        res_data = json.loads(res.data)
        self.assertFalse(res_data["success"])
        self.assertEqual(res_data["message"], "resource not found")
