import pytest
from src.App import App
from unittest.mock import patch

@pytest.fixture
def initial_state(
        state_factory,
        input_value_factory
):
    input_value = input_value_factory()
    count = 0
    todos = ['Learn React', 'Test Vector++']
    return {'count': count, 'todos': todos, 'inputValue': input_value}

@pytest.fixture
def input_value_factory():
    def factory(value=''): return value
    return factory

@pytest.mark.parametrize('todos_before_clear', [[], ['Learn React'], ['Learn React', 'Test Vector++']])
def test_handle_clear_todos_success(initial_state, todos_before_clear):
    with patch.object(App, 'setTodos') as mock_setTodos:
        mock_setTodos.return_value = None
        app = App()
        app.todos = todos_before_clear
        app.inputValue = ''
        app.handleClearTodos()
        assert mock_setTodos.call_count == 1
        mock_setTodos.assert_called_with([])

@pytest.mark.parametrize('todos_before_clear', [None, [], ['Learn React', 'Test Vector++']])
def test_handle_clear_todos_failure(initial_state, todos_before_clear):
    with patch.object(App, 'setTodos') as mock_setTodos:
        mock_setTodos.return_value = None
        app = App()
        app.todos = todos_before_clear
        app.inputValue = ''
        app.handleClearTodos()
        assert mock_setTodos.call_count == 1
        mock_setTodos.assert_called_with([])

@pytest.mark.parametrize('todos_before_clear', [None])
def test_handle_clear_todos_handles_null(initial_state, todos_before_clear):
    with patch.object(App, 'setTodos') as mock_setTodos:
        mock_setTodos.return_value = None
        app = App()
        app.todos = todos_before_clear
        app.inputValue = ''
        app.handleClearTodos()
        assert mock_setTodos.call_count == 1
        mock_setTodos.assert_called_with([])

@pytest.mark.parametrize('input_value', ['x', 'xyz', 'abcde'])
def test_handle_add_todo_disabled_flag(input_value_factory):
    app = App()
    app.inputValue = input_value_factory('x')
    app.handleAddTodo()
    assert not app.todoFormButton.disabled
    app.inputValue = input_value_factory('xyz')
    app.handleAddTodo()
    assert not app.todoFormButton.disabled
    app.inputValue = input_value_factory('abcde')
    app.handleAddTodo()
    assert app.todoFormButton.disabled

@pytest.mark.parametrize('input_value', ['xxxxx', 'abcdefg'])
def test_handle_add_todo_enables_flag(input_value_factory):
    app = App()
    app.inputValue = input_value_factory('xxxxx')
    app.handleAddTodo()
    assert app.todoFormButton.disabled
    app.inputValue = input_value_factory('abcdefg')
    app.handleAddTodo()
    assert app.todoFormButton.disabled
