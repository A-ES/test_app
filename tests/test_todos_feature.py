import pytest
from unittest.mock import patch

from src.app import App
from src.reducers.todosReducer import todosReducer

@pytest.fixture
@patch('src.reducers.todosReducer.todos')
def mock_todos(mock_todos):
    mock_todos.value = []
    return mock_todos

def test_handles_clear_todos_successfully(mock_todos):
    '''Test clearing todos successfully does not cause an error''' 
    mock_todos.value = ['Learn React', 'Test Vector++']
    set_state_side_effect = mock_todos.post_value = []
    App().render()
    with patch.object(App, 'setTodos') as mock_setTodos:
        mock_setTodos.side_effect = set_state_side_effect
        App().handleClearTodos()
    mock_setTodos.assert_called_once_with([])
    assert not mock_todos.post_value

def test_clearing_todos_with_empty_state(mock_todos):
    '''Test clearing todos when already empty''' 
    mock_todos.value = []
    set_state_side_effect = mock_todos.post_value = []
    App().render()
    with patch.object(App, 'setTodos') as mock_setTodos:
        mock_setTodos.side_effect = set_state_side_effect
        App().handleClearTodos()
    mock_setTodos.assert_called_once_with([])
    assert mock_todos.post_value == []

def test_add_new_todo(mock_todos):
    '''Test adding a new todo updates the list correctly''' 
    mock_todos.value = []
    App().render()
    with patch.object(App, 'setTodos') as mock_setTodos,
         patch.object(App, 'setInputValue') as mock_setInputValue:
        mock_setTodos.value = ['Learn React', 'Test Vector++']
        mock_setInputValue.value = ''
        mock_setTodos.method.return_value = ['Learn React', 'Test Vector++', 'New Todo']
        App().handleAddTodo()
        mock_setTodos.assert_called_with(['Learn React', 'Test Vector++', 'New Todo'])
        mock_setInputValue.assert_called_with('')

def test_clear_todos_throws_error_on_non_array_input(mock_todos):
    '''Edge Case: Test clearing todos with non-array input, should not throw error''' 
    mock_todos.value = ''
    set_state_side_effect = mock_todos.post_value = []
    App().render()
    with patch.object(App, 'setTodos') as mock_setTodos:
        mock_setTodos.side_effect = set_state_side_effect
        App().handleClearTodos()
    mock_setTodos.assert_called_once_with([])
