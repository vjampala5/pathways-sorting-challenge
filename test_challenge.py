import challenge

def test_standard():
    assert challenge.sort(100, 100, 100, 10) == "STANDARD"

def test_bulky_only():
    assert challenge.sort(200, 50, 50, 10) == "SPECIAL"

def test_heavy_only():
    assert challenge.sort(100, 100, 100, 25) == "SPECIAL"

def test_bulky_and_heavy():
    assert challenge.sort(200, 200, 200, 25) == "REJECTED"
