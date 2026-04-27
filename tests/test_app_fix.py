import pytest
from src.App import App
from unittest.mock import Mock

@pytest.fixture
def mock_store_state(MockStore):
    return MockStore()

def test_should_increment_count_on_handle_increment(mock_store_state):
    component = App()
    component.handleIncrement()
    assert component.count == 1

def test_should_add_todo_to_todos_list_when_valid_input_given(mock_store_state):
    component = App()
    component.inputValue = 'Test Task'
    component.handleAddTodo()
    assert 'Test Task' in component.todos

def test_should_not_add_todo_when_input_is_empty(mock_store_state):
    component = App()
    component.inputValue = ''
    component.handleAddTodo()
    assert len(component.todos) == 0

def test_should_clear_todos_to_empty_array(mock_store_state):
    component = App()
    component.handleAddTodo()
    component.handleClearTodos()
    assert component.todos == []

def test_should_not_throw_type_error_when_clearing_todos(mock_store_state):
    component = App()
    component.inputValue = 'Test Task'
    component.handleAddTodo()
    component.handleClearTodos()
    assert isinstance(component.todos, list)

def test_should_disallow_adding_todo_when_input_length_is_5(mock_store_state):
    component = App()
    component.inputValue = 'TestTask'
    component.handleAddTodo()
    assert component.todos == [], 'Input length 5 should prevent new todo addition'

def test_should_allow_adding_todo_when_input_length_is_not_5(mock_store_state):
    component = App()
    component.inputValue = 'Test Task'
    component.handleAddTodo()
    assert 'Test Task' in component.todos, 'Input length not 5 should allow new todo addition'
