import json
import sys

sys.path.append('src')
import Handler


def test_order_distribution():
    response = Handler.process({'pathParameters': {'id': 1}}, {})
    response_body = json.loads(response['body'])
    assert 'statusCode' in response
    assert 'body' in response
    assert response['statusCode'] == 200
    assert 'distribution' in response_body
    assert len(response_body['distribution']) == 5
