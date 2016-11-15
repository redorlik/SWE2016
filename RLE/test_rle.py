from rle import rle_encoder,rle_decoder,serialize_int,deserialize_int
from hypothesis import given,settings
from hypothesis.strategies import text,integers

def test_simple_encode():
    assert rle_encoder('aa') == [(2,'a')]
    assert rle_encoder('wwwwwbbb') == [(5,'w'),(3,'b')]

def test_more():
    assert rle_encoder('#####') == [(5,'#')]

def test_encoder():
    assert rle_encoder('kkkbb') == [(3,'k'),(2,'b')]

def test_encoder2():
    assert rle_encoder('dkkkbb') == [(1,'d'),(3,'k'),(2,'b')]
    assert rle_encoder('kkkkkkkkkkbb') == [(10,'k'),(2,'b')]

def test_encoder_tal():
    assert rle_encoder('1111kkkbb') == [(4,'1'),(3,'k'),(2,'b')]

def test_encoder_space():
    assert rle_encoder('kkk          bb') == [(3,'k'),(10,' '),(2,'b')]

def test_encoder_empty():
    assert rle_encoder('0') == [(1,'0')]

def test_decoder():
    assert rle_decoder([(2,'k'),(3,'b')]) == 'kkbbb'

def test_decoder_space():
    assert rle_decoder([(3,'k'),(10,' '),(2,'b')]) == 'kkk          bb'
    assert rle_decoder([(10,'k'),(2,'b')]) == 'kkk1kkkkkkkbb'
    assert rle_decoder([(10,'3')]) == '3333333333'
    assert rle_decoder([(1,'0')]) == '0'
    assert rle_decoder([(1,'0'),(1,'1')]) == '01'

def test_serial_int():
    assert serialize_int(5) == '\x015'

def test_deserial_int():
    assert deserialize_int('\x015') == 5

@given(integers())
def test_serilise_deserial_int(num):
    assert deserialize_int(serialize_int(num)) == num

@given(text(min_size=100))
@settings(max_examples=5000)
def test_encode_decode(input):
    print input
    assert rle_decoder(rle_encoder(input)) == input
