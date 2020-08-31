import json
import sys

sys.path.append('src')
import Handler


def test_order_distribution():
    response = Handler.get_inventory_distribution({}, {})
    response_body = json.loads(response['body'])
    assert 'statusCode' in response
    assert 'body' in response
    assert response['statusCode'] == 200
    assert len(response_body['orders']) == 15
