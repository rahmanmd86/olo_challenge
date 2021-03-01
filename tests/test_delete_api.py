from src.rest_client import RestClient

def test_delete_api_posts(url_config):
    expected_body = {}

    client = RestClient(url_config)
    response = client.sends().posts(postId=1).delete()
    
    client.sees(response).status_code(200).body(expected_body)
 