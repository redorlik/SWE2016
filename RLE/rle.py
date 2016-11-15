# Run length encoder :
#
# Skal konvertere feks. 'kkkbb' til [(3,'k'),(2,'b')]
#
#

def rle_encoder(message):
    
    old = message[0]
    count = 1
    result = []

    for ch in message[1:]:
        if ch == old:
            count += 1
        else:
            result.append((count,old))
            old = ch
            count = 1
    result.append((count,old))
    return result

def rle_decoder(code):
    result = ''
    for count,ch in code:
        result = result + count*ch
    return result

def rle_decoder_join(code):
    #result = [count*ch for count,ch in code]
    #result = ''.join([count*ch for count,ch in code])
    return ''.join([count*ch for count,ch in code])

def deserialize_int(mess):
    cnt = ord(mess[0])
    return int(mess[1:cnt+1])

def serialize_int(tal):
    str = '{}'.format(tal)
    str = '{}{}'.format(chr(len(str)),str)
    return str

def serialize(encoded):
    result = ['{}{}'.format(serialize_int(count),ch) for count,ch in encoded]
    return ''.join(result)


if __name__ == '__main__':
    import sys,time
    #a = sys.argv[1]
    test_data = 50000*[(12000,'f'),(14000,'g')]
    #print test_data
    #import pdb;pdb.set_trace()
    start = time.time()
    res1 = rle_decoder_join(test_data)
    stop = time.time()
    time_for = stop - start
    res2 = rle_decoder(test_data)
    time_join = time.time() - stop
    print u"Tid for 'for'", time_for, "tid for 'join'",time_join,res1==res2
