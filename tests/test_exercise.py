from lib.exercise import *
from unittest.mock import Mock

# error() returns the difference between local and server time
def test_error_returns_difference_between_local_and_server_time():
    mock_requester = Mock()
    mock_requester.get.return_value.json.return_value = {"unixtime":1695895742}
    mock_timer = Mock()
    mock_timer.time.return_value = 1695895742.5
    time_error = TimeError(mock_requester, mock_timer)
    assert time_error.error() == -0.5
