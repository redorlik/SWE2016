from rle_encode import rle_encoder,rle_decoder
from py.test import skip

def test_encoder():
    assert rle_encoder('kkkbb') == '3k2b'

def test_encoder2():
    assert rle_encoder('dkkkbb') == '1d3k2b'
    assert rle_encoder('kkkkkkkkkkbb') == '10k2b'

def test_encoder_tal():
    assert rle_encoder('1111kkkbb') == '413k2b'

def test_encoder_space():
    assert rle_encoder('kkk          bb') == '3k10 2b'

def test_encoder_empty():
    assert rle_encoder('') == ''

def test_decoder():
    assert rle_decoder('2k3b') == 'kkbbb'

def test_decoder_space():
    assert rle_decoder('3k10 2b') == 'kkk          bb'
    assert rle_decoder('10k2b') == 'kkkkkkkkkkbb'

def test_decoder_encoder():
    assert rle_decoder(rle_encoder('kkkkkkkkkkbb')) == 'kkkkkkkkkkbb'

def test_decoder_tal():
    skip('Need to think about this')
    assert rle_decoder(rle_encoder('111kkkkkkkkkkbb')) == '111kkkkkkkkkkbb'

