import pytest 
from app import create_app, db 
 
@pytest.fixture 
def app(): 
    app = create_app() 
    app.config['TESTING'] = True 
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:' 
    return app 
 
def test_index_page(client): 
    response = client.get('/') 
    assert response.status_code == 302 
