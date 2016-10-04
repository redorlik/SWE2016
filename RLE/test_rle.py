from rle import rle_encoder,rle_decoder
from hypothesis import given
from hypothesis.strategies import text

def test_encode():
    assert rle_encoder('aa') == '2a'
    assert rle_encoder('wwwwwbbb') == '5w3b'

def test_more():
    assert rle_encoder('#####') == '5#'

def test_encoder():
    assert rle_encoder('kkkbb') == '3k2b'

def test_encoder2():
    assert rle_encoder('dkkkbb') == '1d3k2b'
    assert rle_encoder('kkkkkkkkkkbb') == '10k2b'

def test_encoder_tal():
    assert rle_encoder('1111kkkbb') == '4\\13k2b'

def test_encoder_space():
    assert rle_encoder('kkk          bb') == '3k10 2b'

def test_encoder_empty():
    assert rle_encoder('') == ''
    assert rle_encoder('0') == '1\\0'

def test_decoder():
    assert rle_decoder('2k3b') == 'kkbbb'

def test_decoder_space():
    assert rle_decoder('3k10 2b') == 'kkk          bb'
    assert rle_decoder('10k2b') == 'kkkkkkkkkkbb'
    assert rle_decoder('10\\3') == '3333333333'
    assert rle_decoder('1\\0') == '0'
    assert rle_decoder('1\\01\\1') == '01'

@given(text())
def test_encode_decode(input):
    assert rle_decoder(rle_encoder(input)) == input
