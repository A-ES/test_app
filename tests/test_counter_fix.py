import pytest
from unittest.mock import patch
from src.App import App

@pytest.fixture
def count_context(initial_count):
    return {'__mockState': {'count': initial_count}}

def initial_state()
    return {'count': 0, 'todos': ['Learn React', 'Test Vector++'], 'inputValue': ''}

def test_should_increment_counter_by_one_on_click(count_context):
    from src.App import handleIncrement
    state = {**initial_state(), **count_context}
    handleIncrement(state)
    assert state['__mockState']['count'] == 1
    handleIncrement(state)
    assert state['__mockState']['count'] == 2

def test_should_set_todos_appropriately(count_context):
    setTodosSpy = pytest.spy_on(App.setTodos, name='setTodos')
    state = {**initial_state(), **count_context}
    state['inputValue'] = "Read Docs"
    App.handleAddTodo(state)
    assert setTodosSpy.last_call.args[0] == ['Learn React', 'Test Vector++', 'Read Docs']
    setTodosSpy.assert_called_once()

def test_should_clear_todos(count_context):
    setTodosSpy = pytest.spy_on(App.setTodos, name='setTodos')
    state = {**initial_state(), **count_context}
    App.handleClearTodos(state)
    assert state['__mockState']['todos'] == []
    assert setTodosSpy.mock_calls == [pytest.call([], any_instance_of(dict))]

def test_edge_case_when_input_is_empty(django settings):
    state = initial_state()
    App.handleAddTodo(state)
    assert state['inputValue'] == ''

def test_edge_case_when_input_length_is_exact_five(django settings):
    state = initial_state()
    state['inputValue'] = 'abcde'
    assert not App.handleAddTodo(state)['disabled']
