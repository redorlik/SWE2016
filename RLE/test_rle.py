from rle import encode

def test_encode():
    assert encode('aa') == '2a'
    assert encode('wwwwwbbb') == '5w3b'

def test_more():
    assert encode('#####') == '5#'
