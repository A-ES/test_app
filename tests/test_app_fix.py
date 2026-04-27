import pytest
import mock
from src.App import App

@pytest.fixture
def mock_setState(mocker):
    return mocker.patch.object(App, 'setCount')