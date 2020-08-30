import sys

sys.path.append('src')
import handler


def test_check_active_accounts():
    response = handler.process({}, {})
    assert 'statusCode' in response
    assert 'body' in response
    assert response['statusCode'] == 200
