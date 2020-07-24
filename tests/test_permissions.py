from .utils import TestAgencyMixin

JWTs = {
    'assistant': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImprZDBwdWhGSlBWdnc4ZHRFMzdtbCJ9.eyJpc3MiOiJodHRwczovL3VkYWNvZmZlZS5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYxMWIyNzE3YTcwM2EwMDEzODU3M2VhIiwiYXVkIjoiaHR0cDovL2FnZW5jeS5ldSIsImlhdCI6MTU5NTU5NDU1NiwiZXhwIjoxNTk1NjgwOTU2LCJhenAiOiJjR0RXdFc2M1oxVVhwMURTS3hHU3l3RTAwRmpBNjlpMSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDphY3RvcnMtZGV0YWlscyIsImdldDptb3ZpZXMiLCJnZXQ6bW92aWVzLWRldGFpbHMiXX0.dy42PLJDLYRrSn0JD_uhxMxuZBPtnByi9tT6l3PqjoE-eFJSX-scoPZuN-Q-GbMFYn6NlyrpZYQ0rJ8cU6qaMdLWyr-WPTKj2Ymts8slbjDk_HEXpPsZ1NotkwNA9AjbIHZy0FTFfac_wjLX_KewZcjl5sMbiVnApHPOwI54RAAo-jCGrRFfzis7FU95xccxukWdPvba9E-CdEJEnubNhg5NnF0-pNR7cIEeRTB533UsPX_6jWMUWaj11mrIXEbzzizwWcd2ZvHWrffyr6NOWv7kb1DlWquHe1-I1nFmr_QBA18TJfKysaPcSRuiwEL4r17e81humHZ_lMunoGsffA',
    'director': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImprZDBwdWhGSlBWdnc4ZHRFMzdtbCJ9.eyJpc3MiOiJodHRwczovL3VkYWNvZmZlZS5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYxMWIzNTQxYmE4ZjMwMDE5YjNlYWI4IiwiYXVkIjoiaHR0cDovL2FnZW5jeS5ldSIsImlhdCI6MTU5NTU5NDU4NSwiZXhwIjoxNTk1NjgwOTg1LCJhenAiOiJjR0RXdFc2M1oxVVhwMURTS3hHU3l3RTAwRmpBNjlpMSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImdldDphY3RvcnMiLCJnZXQ6YWN0b3JzLWRldGFpbHMiLCJnZXQ6bW92aWVzIiwiZ2V0Om1vdmllcy1kZXRhaWxzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiXX0.cHs3iuYphTk5hmYoD6Pz0ofRh2K18Voqbk_mF1F8w1EpEdvfbV0WC3F-5KmLbUwbzVINgP8uUja7BvSd0Y7N2HA35ahgwfY8TF-Y0acFNOQ04zgT7QEJru_W6cGjIZJQ7ODBthJpa0wbTZoK63jUNNEtXVqSi5GO8kJNo33IT4QJ5bWl82d65ZBKt6Wg-yLRyrkc6fI4w3bn7zTBOQ2J6Cy4dVpWWIJnFuSG1rJ_sJzWyubsd84mHLCSX3ki5MFf2r2518EAdu2OxMRpJ7dsXPFf2gEbvBUVc5vbHVvEXLMm_RJNyqEvknkBQl5LMsMdU0b3x2FdR4BKbm16G-UPQQ',
    'producer': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImprZDBwdWhGSlBWdnc4ZHRFMzdtbCJ9.eyJpc3MiOiJodHRwczovL3VkYWNvZmZlZS5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYxMWIzOWQxYmE4ZjMwMDE5YjNlYWVmIiwiYXVkIjoiaHR0cDovL2FnZW5jeS5ldSIsImlhdCI6MTU5NTU5NDYxNSwiZXhwIjoxNTk1NjgxMDE1LCJhenAiOiJjR0RXdFc2M1oxVVhwMURTS3hHU3l3RTAwRmpBNjlpMSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0OmFjdG9ycy1kZXRhaWxzIiwiZ2V0Om1vdmllcyIsImdldDptb3ZpZXMtZGV0YWlscyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiXX0.ckLNDEwmQZweYuaAls60Cx-ct945lPEYsiaXnvp6oyEDBo6feem4DAaJyxGRS5Vxj0c1pXKPlsZZVb2V1wrJwWVsNpp0csHVImdh6pzNe-rbJbQhrqHcjmxRzwI9eUiZ84y_OJDi2GZ8l5HKUXKq3y4FLhKy8ywg0y6yKnoxspzuUvioJh-JX_swaweAJOCOfoW6ECgMiSLPEtzLUXk4VtPchgMWgr0KA3Dp0TsFVHn2yicNuVdHV77J2ypGjNLXbQyYVfOIkJJT4x2x7uOVEGW4Iu5JYuqPpnHJL-aUvjZJAEU6l6hPYPDEkfMqSq99kOziGgcGlpN9MSckFzJD_A',
}


class TestAgencyRoles(TestAgencyMixin):
    """Test permissions of uda-agency"""

    def test_assistant_role(self):
        headers = {'Authorization': JWTs['assistant']}
        res = self.client().get('/actors', headers=headers)
        self.assertEqual(res.status_code, 200)

        res = self.client().get('/actors/1', headers=headers)
        self.assertEqual(res.status_code, 200)

        res = self.client().post('/actors', headers=headers, json={})
        self.assertEqual(res.status_code, 403)

        res = self.client().patch('/actors/1', headers=headers, json={})
        self.assertEqual(res.status_code, 403)

        res = self.client().delete('/actors/1', headers=headers)
        self.assertEqual(res.status_code, 403)

        res = self.client().get('/movies', headers=headers)
        self.assertEqual(res.status_code, 200)

        res = self.client().get('/movies/1', headers=headers)
        self.assertEqual(res.status_code, 200)

        res = self.client().post('/movies', headers=headers, json={})
        self.assertEqual(res.status_code, 403)

        res = self.client().patch('/movies/1', headers=headers, json={})
        self.assertEqual(res.status_code, 403)

        res = self.client().delete('/movies/1', headers=headers)
        self.assertEqual(res.status_code, 403)

    def test_director_role(self):
        headers = {'Authorization': JWTs['director']}
        res = self.client().get('/actors', headers=headers)
        self.assertEqual(res.status_code, 200)

        res = self.client().get('/actors/1', headers=headers)
        self.assertEqual(res.status_code, 200)

        data = {'first_name': 'Matt', 'last_name': 'Gail', 'age': 42, 
                'gender': 'MALE'}
        res = self.client().post('/actors', headers=headers, json=data)
        self.assertEqual(res.status_code, 200)

        res = self.client().patch('/actors/1', headers=headers, json={})
        self.assertEqual(res.status_code, 200)

        res = self.client().delete('/actors/1', headers=headers)
        self.assertEqual(res.status_code, 200)

        res = self.client().get('/movies', headers=headers)
        self.assertEqual(res.status_code, 200)

        res = self.client().get('/movies/1', headers=headers)
        self.assertEqual(res.status_code, 200)

        res = self.client().post('/movies', headers=headers, json={})
        self.assertEqual(res.status_code, 403)

        res = self.client().patch('/movies/1', headers=headers, json={})
        self.assertEqual(res.status_code, 200)

        res = self.client().delete('/movies/1', headers=headers)
        self.assertEqual(res.status_code, 403)


    def test_producer_role(self):
        headers = {'Authorization': JWTs['producer']}
        res = self.client().get('/actors', headers=headers)
        self.assertEqual(res.status_code, 200)

        res = self.client().get('/actors/1', headers=headers)
        self.assertEqual(res.status_code, 200)

        data = {'first_name': 'Matt', 'last_name': 'Gail', 'age': 42, 
                'gender': 'MALE'}
        res = self.client().post('/actors', headers=headers, json=data)
        self.assertEqual(res.status_code, 200)

        res = self.client().patch('/actors/1', headers=headers, json={})
        self.assertEqual(res.status_code, 200)

        res = self.client().delete('/actors/1', headers=headers)
        self.assertEqual(res.status_code, 200)

        res = self.client().get('/movies', headers=headers)
        self.assertEqual(res.status_code, 200)

        res = self.client().get('/movies/1', headers=headers)
        self.assertEqual(res.status_code, 200)

        data = {'title': 'Brand New', 'release_date': '2033-03-11'}
        res = self.client().post('/movies', headers=headers, json=data)
        self.assertEqual(res.status_code, 200)

        res = self.client().patch('/movies/1', headers=headers, json={})
        self.assertEqual(res.status_code, 200)

        res = self.client().delete('/movies/1', headers=headers)
        self.assertEqual(res.status_code, 200)
