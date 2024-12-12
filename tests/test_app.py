import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    return app.test_client()

def test_optimize_warehouse_multiple_tasks(client):
    sample_data = [
        {"TASK_ID": "task1", "DURATION": 25, "NUMBER_OF_CAMPAIGNS": 120},
        {"TASK_ID": "task2", "DURATION": 15, "NUMBER_OF_CAMPAIGNS": 50},
        {"TASK_ID": "task3", "DURATION": 5, "NUMBER_OF_CAMPAIGNS": 30}
    ]
    response = client.post('/optimize-warehouse', json=sample_data)
    assert response.status_code == 200
    result = response.get_json()
    assert result['task1'] == 'X-Large'
    assert result['task2'] == 'Medium'
    assert result['task3'] == 'Small'

def test_empty_input(client):
    response = client.post('/optimize-warehouse', json=[])
    assert response.status_code == 400

def test_boundary_conditions(client):
    sample_data = [
        {"TASK_ID": "task1", "DURATION": 10, "NUMBER_OF_CAMPAIGNS": 50},
        {"TASK_ID": "task2", "DURATION": 20, "NUMBER_OF_CAMPAIGNS": 50}
    ]
    response = client.post('/optimize-warehouse', json=sample_data)
    assert response.status_code == 200
    result = response.get_json()
    assert result['task1'] == 'Medium'
    assert result['task2'] == 'Medium'

def test_large_input(client):
    sample_data = [
        {"TASK_ID": f"task{i}", "DURATION": 10 + i, "NUMBER_OF_CAMPAIGNS": 100 + i}
        for i in range(1000)
    ]
    response = client.post('/optimize-warehouse', json=sample_data)
    assert response.status_code == 200
    result = response.get_json()
    assert len(result) == 1000  # Ensure all tasks are processed
    assert result["task0"] == 'Medium'  # Example check for the first task
