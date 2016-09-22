from rle import rle_encoder,rle_decoder
from hypothesis import given
from hypothesis.strategies import text

def test_encode():
    assert rle_encoder('aa') == '2a'
    assert rle_encoder('wwwwwbbb') == '5w3b'

def test_more():
    assert rle_encoder('#####') == '5#'
    
@given(text())
def test_encode_decode(input):
    assert rle_decoder(rle_encoder(input)) == input
