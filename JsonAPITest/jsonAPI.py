import unittest
import json
import requests
from faker import Faker
from random import randint
fake = Faker()

class TestJsonPlaceHolder(unittest.TestCase):
    
    base_url = "https://jsonplaceholder.typicode.com"
    userId = randint(1,11)
    postId = randint(1,100)
    
    def setUp(self):
        print("Running", self._testMethodName)

    def test_get_users(self):
        route = self.base_url + f"/users/{self.userId}"
        response = requests.get(route)
        print(f"UserID #{self.userId} email: " + response.json()['email'])
        assert response.status_code == 200
        
    def test_get_user_posts(self):
        route = self.base_url + f"/users/{self.userId}/posts"
        response = requests.get(route)
        for post in response.json():
            postID = post['id']
            self.assertTrue(1 <= postID <= 100)
            print(f"Post ID is valid {postID}")
        assert response.status_code == 200

    def test_create_post(self):
        route = self.base_url + "/posts"
        headers = {'Content-Type': 'application/json'}
        payload = json.dumps({
            "title": "Greeting",
            "body": "Hello there!",
            "userId": self.userId
        })
        response = requests.post(route, headers=headers, data=payload)
        assert response.status_code == 201
    
if __name__ == '__main__':
    
    def suite():
        suite = unittest.TestSuite()
        suite.addTest(TestJsonPlaceHolder('test_get_users'))
        suite.addTest(TestJsonPlaceHolder('test_get_user_posts'))
        suite.addTest(TestJsonPlaceHolder('test_create_post'))
        return suite

    runner = unittest.TextTestRunner(failfast=True)
    runner.run(suite())
