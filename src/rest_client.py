import requests, json, logging

import logging

logging.basicConfig(filename='test_result.log', encoding='utf-8')
logger = logging.getLogger(__name__)

class RestClient:
    def __init__(self, url_config) -> None:
         self.url_config = url_config
         self.url = None
         self.postId = None
         self.query = None
         self.response = None
         
    def sends(self):
        return self
    
    def posts(self, postId=""):
        self.postId = str(postId) if type(postId) != str else postId
        self.url = self.url_config['base_url'] + self.url_config['posts'].replace(":postId", self.postId)
        return self

    def comments(self, postId="", query=""):
        self.postId = str(postId) if type(postId) != str else postId
        if postId is not "":
            self.url = self.url_config['base_url'] + self.url_config['posts'].replace(":postId", self.postId) + self.url_config['comments']
        if query is not "":
            self.url = self.url_config['base_url'] + self.url_config['comments'] + query
        return self


    def get(self, params={}):
        url = self.url.replace(":postId", self.postId)
        response = requests.get(url, params=params)
        return response

    def post(self, body={}, headers={}):
        if not bool(headers):
            headers = {'Content-type': 'application/json; charset=UTF-8'}
        response = requests.post(self.url, data=json.dumps(body), headers=headers)
        return response

    def put(self, body={}, headers={}):
        if not bool(headers):
            headers = {'Content-type': 'application/json; charset=UTF-8'}
        response = requests.put(self.url, data=json.dumps(body), headers=headers)
        return response

    def delete(self):
        response = requests.delete(self.url)
        return response

    def sees(self, response={}):
        self.response = response
        return self

    def status_code(self, code=None):
        try:
            assert self.response.status_code == code
        except:
            logger.error(f'Expected: {code}, Actual: {self.response.status_code}')
            raise Exception("Test case failed")
        return self

    def body(self, expected_body={}):
        resp_json = self.response.json()
        assert resp_json == expected_body
        return self

    def count(self, expected_count=None):
        resp_json = self.response.json()
        assert len(resp_json) == expected_count
        return self
    



