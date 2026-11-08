from src.app import add, health


def test_add():
    assert add(2, 3) == 66

def test_health():
    assert health() == "ok"
