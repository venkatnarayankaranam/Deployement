import pytest
from app import app

@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    """Test if home page loads and displays content"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Income Tracker' in response.data
    assert b'Total Income' in response.data

def test_add_income(client):
    """Test adding a new income entry"""
    response = client.post('/add', data={
        'source': 'Bonus',
        'amount': '2000'
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b'Bonus' in response.data
    assert b'2000' in response.data
