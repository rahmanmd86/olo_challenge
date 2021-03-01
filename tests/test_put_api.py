from src.rest_client import RestClient

def test_put_api_posts(url_config):
    body = {'title': 'foo', 'body': 'bar', 'userId': 1}
    expected_body = {'title': 'foo', 'body': 'bar', 'userId': 1, 'id': 1}

    client = RestClient(url_config)
    response = client.sends().posts(postId=1).put(body)
    
    client.sees(response).status_code(200).body(expected_body)

def test_put_api_posts_empty_payload(url_config):
    body = {}
    expected_body = {'id': 1}

    client = RestClient(url_config)
    response = client.sends().posts(postId=1).put(body)
    
    client.sees(response).status_code(200).body(expected_body)

def test_put_api_posts_invalid_postId(url_config):
    body = {'title': 'foo', 'body': 'bar', 'userId': 1}
    expected_body = {'error': 'id: 101 not found'}

    client = RestClient(url_config)
    response = client.sends().posts(postId=101).put(body)
    
    client.sees(response).status_code(404).body(expected_body)
 