from src.rest_client import RestClient

def test_get_posts_api_by_id(url_config):
    client = RestClient(url_config)
    response = client.sends().posts(postId=1).get()
    expected_body = {
        'userId': 1, 
        'id': 1, 
        'title': 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit', 
        'body': 'quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto'
    }

    client.sees(response).status_code(200).body(expected_body)
    
def test_get_posts_api_all(url_config):
    client = RestClient(url_config)
    response = client.sends().posts().get()

    client.sees(response).status_code(200).count(100)

def test_get_posts_api_invalid_postId(url_config):
    client = RestClient(url_config)
    response = client.sends().posts(postId=101).get()
    expected_body = {}

    client.sees(response).status_code(404).body(expected_body)
    
def test_get_comments_by_postId(url_config):
    client = RestClient(url_config)
    response = client.sends().comments(postId=1).get()

    client.sees(response).status_code(200).count(5)

def test_get_comments_by_postId_query(url_config):
    client = RestClient(url_config)
    response = client.sends().comments(query="?postId=1").get()

    client.sees(response).status_code(200).count(5)
    
