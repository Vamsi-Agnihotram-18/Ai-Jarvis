import os
import io
import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_upload_txt_file(client):
    data = {
        'file': (io.BytesIO(b"This is a test document."), 'test.txt')
    }
    response = client.post('/upload', content_type='multipart/form-data', data=data)
    assert response.status_code == 200
    assert 'id' in response.get_json()

def test_query_without_file(client):
    response = client.post('/query', json={'query': 'What is this?'})
    assert response.status_code == 200
    assert 'answer' in response.get_json()

# Integration: Upload then query
def test_upload_and_query(client):
    data = {
        'file': (io.BytesIO(b"AI is transforming technology."), 'ai.txt')
    }
    upload_resp = client.post('/upload', content_type='multipart/form-data', data=data)
    file_id = upload_resp.get_json()['id']

    query_resp = client.post('/query', json={'query': 'What is AI?', 'file_id': file_id})
    assert query_resp.status_code == 200
    assert 'answer' in query_resp.get_json()