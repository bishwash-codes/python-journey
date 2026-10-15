from calc import add, sub, mul


def test_add():
    assert add(5, 10) == 15
    assert add(0, 0) == 0


def test_sub():
    assert sub(-7, 3) == -10


def test_mul():
    assert mul(0, 0) == f"the product is {0}"
