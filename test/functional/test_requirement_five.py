import json
import sys

sys.path.append('src')
import Handler


def test_get_top_sold_products():
    response = Handler.get_top_sold_products({'queryStringParameters': {'sort': 'ASC'}}, {})
    response_body = json.loads(response['body'])
    assert 'statusCode' in response
    assert 'body' in response
    assert response['statusCode'] == 200
    assert response_body[0].get('total') == 1
