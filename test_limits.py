from limits import limit, g


def test_limit():
    assert limit(g, 1) == 2
