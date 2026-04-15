import pytest
from src.App import App

@pytest.fixture()
def todos_fixture(mocker):
    mocker.patch('src.App.todos', return_value=['Learn React', 'Test Vector++'])


@pytest.fixture()
def count_fixture(mocker):
    mocker.patch('src.App.count', return_value=0)


@pytest.fixture()
def clearTodos_fixture(mocker):
    return mocker.patch('src.App.handleClearTodos')


@pytest.fixture()
def setTodos_fixture(mocker):
    return mocker.patch('src.App.setTodos')


@pytest.fixture()
def setInputValue_fixture(mocker):
    return mocker.patch('src.App.setInputValue')


@pytest.mark.parametrize('input_value', ['', 'Test', '1234', '123456'])
def test_handleAddTodo(input_value, todos_fixture, count_fixture, setTodos_fixture, setInputValue_fixture):
    app = App()
    app.handleAddTodo()
    assert setTodos_fixture.call_args[0][0] == ['Learn React', 'Test Vector++', input_value]
    assert setInputValue_fixture.call_args[0][0] == ''


def test_handleIncrement(todos_fixture, count_fixture, setTodos_fixture):
    app = App()
    app.handleIncrement()
    assert setCount.call_args[0][0] == count_fixture() + 1


def test_clearTodosSuccess(setTodos_fixture, todos_fixture, count_fixture):
    app = App()
    app.handleClearTodos()
    setTodos_fixture.assert_called_with([])
    assert todos_fixture.return_value == []
    assert count_fixture() == 0


def test_clearTodosFailure(setTodos_fixture, todos_fixture, count_fixture):
    todos_fixture.return_value = None
    app = App()
    app.handleClearTodos()
    setTodos_fixture.assert_called_with([])
    assert todos_fixture.return_value is None


def test_clearTodosEdgeCase(setTodos_fixture, todos_fixture, count_fixture):
    todos_fixture.return_value = []
    app = App()
    app.handleClearTodos()
    setTodos_fixture.assert_called_with([])
    assert todos_fixture.return_value == []
    assert count_fixture() == 0
