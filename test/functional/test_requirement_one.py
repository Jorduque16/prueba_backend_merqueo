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
    assert response_body['distribution'][0].get('provider_name') == 'inventory'
    assert response_body['distribution'][1].get('provider_name') == 'Ruby'
    assert response_body['distribution'][2].get('provider_name') == 'default'
    assert response_body['distribution'][3].get('provider_name') == 'Ruby'
    assert response_body['distribution'][4].get('provider_name') == 'inventory'
