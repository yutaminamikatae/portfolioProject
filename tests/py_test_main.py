import pytest
from apps.minimalapp.app import app
def test_flask_sample():
    client = app.test_client()
    result = client.get('/')
    assert b'flask test12' == result.data