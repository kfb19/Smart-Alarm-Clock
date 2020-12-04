"""this test tests the function refresh_alarm() in main.py"""

from main import refresh_alarm

def test_refresh_alarm():
    """tests the function refresh_alarm()"""
    assert refresh_alarm() == "Alarm refreshed"
