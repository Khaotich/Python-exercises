from StudentDB import StudentDB
import pytest

#pierwszy sposób pisania testów z incjowaniem zasobów np. baza danych
# db = None
# def setup_module(module):
#     print('---setup_module---')
#     global db
#     db = StudentDB()
#     db.connect("database.json")
#
# def teardown_module(module):
#     print('---teardown_module---')
#     db.close()
#
# def test_scoot():
#     data = db.getData('Scoot')
#     print(data)
#     assert data['id'] == 1
#     assert data['name'] == 'Scoot'
#     assert data['result'] == 'pass'

#drugi sposób incjowania
@pytest.fixture(scope='module')
def db():
    print('---setup_module---')
    db = StudentDB()
    db.connect("database.json")
    yield db
    print('---teardown_module---')
    db.close()

def test_scoot(db):
    data = db.getData('Scoot')
    assert data['id'] == 1
    assert data['name'] == 'Scoot'
    assert data['result'] == 'pass'

def test_mark(db):
    data = db.getData('Mark')
    assert data['id'] == 2
    assert data['name'] == 'Mark'
    assert data['result'] == 'fail'