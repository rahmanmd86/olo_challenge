from src.rest_client import RestClient

def test_post_api_posts(url_config):
    body = {'title': 'foo', 'body': 'bar', 'userId': 1}
    expected_body = {'title': 'foo', 'body': 'bar', 'userId': 1, 'id': 101}

    client = RestClient(url_config)
    response = client.sends().posts().post(body)
    
    client.sees(response).status_code(201).body(expected_body)

def test_post_api_posts_empty_payload(url_config):
    body = {}
    expected_body = {'id': 101}

    client = RestClient(url_config)
    response = client.sends().posts().post(body)
    
    client.sees(response).status_code(201).body(expected_body)

def test_post_api_comments_by_postId(url_config):
    body = {"name": "Foo","email": "Foo@bar.biz","body": "Foo is not bar"}
    expected_body = {"name": "Foo", "email": "Foo@bar.biz", "body": "Foo is not bar", "postId": "1","id": 501}

    client = RestClient(url_config)
    response = client.sends().comments(postId=1).post(body)
    
    client.sees(response).status_code(201).body(expected_body)

def test_post_api_posts_empty_payload(url_config):
    body = {}
    expected_body = {'postId': '1','id': 501}

    client = RestClient(url_config)
    response = client.sends().comments(postId=1).post(body)
    
    client.sees(response).status_code(201).body(expected_body)

 