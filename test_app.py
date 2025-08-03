import pytest
from app import app

@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Income Tracker' in response.data

def test_add_income(client):
    response = client.post('/add', data={
        'source': 'Bonus',
        'amount': '2000'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b'Bonus' in response.data
    assert b'2000' in response.data
