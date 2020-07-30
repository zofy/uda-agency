from .utils import TestAgencyMixin

JWTs = {
    "assistant": (
        "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImprZDBwdWhGSlBWd"
        "nc4ZHRFMzdtbCJ9.eyJpc3MiOiJodHRwczovL3VkYWNvZmZlZS5ldS5hdXRoMC5jb20v"
        "Iiwic3ViIjoiYXV0aDB8NWYxMWIyNzE3YTcwM2EwMDEzODU3M2VhIiwiYXVkIjoiaHR0"
        "cDovL2FnZW5jeS5ldSIsImlhdCI6MTU5NjExODM5MywiZXhwIjoxNTk2MjA0NzkzLCJh"
        "enAiOiJjR0RXdFc2M1oxVVhwMURTS3hHU3l3RTAwRmpBNjlpMSIsInNjb3BlIjoiIiwi"
        "cGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDphY3RvcnMtZGV0YWlscyIsImdl"
        "dDptb3ZpZXMiLCJnZXQ6bW92aWVzLWRldGFpbHMiXX0.AJ_CKt7aoQiK9pRfpkyUvYA3"
        "paA2vf-EIr0SgWYjH15WpQAGwoYjIB9LL0LBAXmcbMzegMJdPryhHOim8yeJ2RSC0C-Y"
        "fS-PmXw5qTA_jENFXv7EAPbX8MgJFmTW2alvzBpQQTXCpr6jNx6n2gphSLs_dcb_wUvm"
        "eGP6RNDrTD7nPuerUzfWcFfigjAbgVVMEH5hP0ypsc88HVUW2LVtTyt1qh57dhOvU1mb"
        "ShqxAPUKdRd43gOY94DeHtovzKJpA5WlYvKMYuVTi-SpC7HtrN22i2t-tSGPMIwxhG_k"
        "oiafIZUTq1KRm75Ehv2LzqSZwHZCPPtOYNp4kiLUet3Sdw"
    ),
    "director": (
        "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImprZDBwdWhGSlBWd"
        "nc4ZHRFMzdtbCJ9.eyJpc3MiOiJodHRwczovL3VkYWNvZmZlZS5ldS5hdXRoMC5jb20v"
        "Iiwic3ViIjoiYXV0aDB8NWYxMWIzNTQxYmE4ZjMwMDE5YjNlYWI4IiwiYXVkIjoiaHR0"
        "cDovL2FnZW5jeS5ldSIsImlhdCI6MTU5NjEyMTYwMiwiZXhwIjoxNTk2MjA4MDAyLCJh"
        "enAiOiJjR0RXdFc2M1oxVVhwMURTS3hHU3l3RTAwRmpBNjlpMSIsInNjb3BlIjoiIiwi"
        "cGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImdldDphY3RvcnMiLCJnZXQ6YWN0"
        "b3JzLWRldGFpbHMiLCJnZXQ6bW92aWVzIiwiZ2V0Om1vdmllcy1kZXRhaWxzIiwicGF0"
        "Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiXX0.F3EJY_rhLlDg"
        "vYXxe8CYeWf1-hybd56aGK1gIEnJhdYuGIlc67FGDGc9erAKLh44rVkYUL_IVKak4NTJ"
        "2qBuH0CTvJg_IUPHC8GLaBPinqQJIqzfivvya277Qvb9IuiCSfNz8IJYzUZAvU69iK7e"
        "1LpHJyukPVAx-P8GIiS_9jS-Zf6RNgtfDPwPjExcS1zyqbbJCHV0OMGdOLPgwv5BulqI"
        "rbAYentQzOa41do792yG5YAG9PZSGp1rs9LTaVDu-YFrXftA5Ws_PrvaMZ697kn_pIL0"
        "iziT_cgZO8h8wIufDTj1xIrJ-zOS6j8SEvNnjnNZRErsiH4eeNqwcn9oCQ"
    ),
    "producer": (
        "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImprZDBwdWhGSlBWd"
        "nc4ZHRFMzdtbCJ9.eyJpc3MiOiJodHRwczovL3VkYWNvZmZlZS5ldS5hdXRoMC5jb20v"
        "Iiwic3ViIjoiYXV0aDB8NWYxMWIzOWQxYmE4ZjMwMDE5YjNlYWVmIiwiYXVkIjoiaHR0"
        "cDovL2FnZW5jeS5ldSIsImlhdCI6MTU5NjEzODMwOCwiZXhwIjoxNTk2MjI0NzA4LCJh"
        "enAiOiJjR0RXdFc2M1oxVVhwMURTS3hHU3l3RTAwRmpBNjlpMSIsInNjb3BlIjoiIiwi"
        "cGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6"
        "YWN0b3JzIiwiZ2V0OmFjdG9ycy1kZXRhaWxzIiwiZ2V0Om1vdmllcyIsImdldDptb3Zp"
        "ZXMtZGV0YWlscyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0"
        "b3JzIiwicG9zdDptb3ZpZXMiXX0.anj4v3N5NP8pMyC-1jHEiOzQ-4wvB87Pevax1J15"
        "JjNMZn9mz5JeSs1ULbm7qqfnPDFQBRAsMM6DYmD7AbUFXxbzXfihAyx00T4QCn7P3X5a"
        "d7SzvknBgEqP_GY6GbwpyXtQ1SE4qYb8c7rwUFaRqC9A1auYema-GtFx_xDKHHMUl-Jz"
        "fdTrL52cwMVal1gv3zSRhhfTTBGFNnlrmDBf4r7rggriATwij131kiepVcDu8fIPjUck"
        "hRpTzq6FvnGQQnFXiRUeyySFPO_-Y3muQNdl6UYpnq3b6T9hr78791X0KY0aSjwjPyiT"
        "-FYuoE9M0ldS3YdWUGJ1Od9Q_DHDVQ"
    ),
}


class TestAgencyRoles(TestAgencyMixin):
    """Test permissions of uda-agency"""

    def test_assistant_role(self):
        headers = {"Authorization": JWTs["assistant"]}
        res = self.client().get("/actors", headers=headers)
        self.assertEqual(res.status_code, 200)

        res = self.client().get("/actors/1", headers=headers)
        self.assertEqual(res.status_code, 200)

        res = self.client().post("/actors", headers=headers, json={})
        self.assertEqual(res.status_code, 403)

        res = self.client().patch("/actors/1", headers=headers, json={})
        self.assertEqual(res.status_code, 403)

        res = self.client().delete("/actors/1", headers=headers)
        self.assertEqual(res.status_code, 403)

        res = self.client().get("/movies", headers=headers)
        self.assertEqual(res.status_code, 200)

        res = self.client().get("/movies/1", headers=headers)
        self.assertEqual(res.status_code, 200)

        res = self.client().post("/movies", headers=headers, json={})
        self.assertEqual(res.status_code, 403)

        res = self.client().patch("/movies/1", headers=headers, json={})
        self.assertEqual(res.status_code, 403)

        res = self.client().delete("/movies/1", headers=headers)
        self.assertEqual(res.status_code, 403)

    def test_director_role(self):
        headers = {"Authorization": JWTs["director"]}
        res = self.client().get("/actors", headers=headers)
        self.assertEqual(res.status_code, 200)

        res = self.client().get("/actors/1", headers=headers)
        self.assertEqual(res.status_code, 200)

        data = {"first_name": "Matt", "last_name": "Gail", "age": 42,
                "gender": "MALE"}
        res = self.client().post("/actors", headers=headers, json=data)
        self.assertEqual(res.status_code, 200)

        res = self.client().patch("/actors/1", headers=headers, json={})
        self.assertEqual(res.status_code, 200)

        res = self.client().delete("/actors/1", headers=headers)
        self.assertEqual(res.status_code, 200)

        res = self.client().get("/movies", headers=headers)
        self.assertEqual(res.status_code, 200)

        res = self.client().get("/movies/1", headers=headers)
        self.assertEqual(res.status_code, 200)

        res = self.client().post("/movies", headers=headers, json={})
        self.assertEqual(res.status_code, 403)

        res = self.client().patch("/movies/1", headers=headers, json={})
        self.assertEqual(res.status_code, 200)

        res = self.client().delete("/movies/1", headers=headers)
        self.assertEqual(res.status_code, 403)

    def test_producer_role(self):
        headers = {"Authorization": JWTs["producer"]}
        res = self.client().get("/actors", headers=headers)
        self.assertEqual(res.status_code, 200)

        res = self.client().get("/actors/1", headers=headers)
        self.assertEqual(res.status_code, 200)

        data = {"first_name": "Matt", "last_name": "Gail", "age": 42,
                "gender": "MALE"}
        res = self.client().post("/actors", headers=headers, json=data)
        self.assertEqual(res.status_code, 200)

        res = self.client().patch("/actors/1", headers=headers, json={})
        self.assertEqual(res.status_code, 200)

        res = self.client().delete("/actors/1", headers=headers)
        self.assertEqual(res.status_code, 200)

        res = self.client().get("/movies", headers=headers)
        self.assertEqual(res.status_code, 200)

        res = self.client().get("/movies/1", headers=headers)
        self.assertEqual(res.status_code, 200)

        data = {"title": "Brand New", "release_date": "2033-03-11"}
        res = self.client().post("/movies", headers=headers, json=data)
        self.assertEqual(res.status_code, 200)

        res = self.client().patch("/movies/1", headers=headers, json={})
        self.assertEqual(res.status_code, 200)

        res = self.client().delete("/movies/1", headers=headers)
        self.assertEqual(res.status_code, 200)
