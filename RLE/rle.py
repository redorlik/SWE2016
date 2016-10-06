# Run length encoder :
#
# Skal konvertere feks. 'kkkbb' til [(3,'k'),(2,'b')]
#
#

def rle_encoder(message):
    if not message:
        return message

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

    result = [count*ch for count,ch in code]
    return ''.join(result)

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
    import sys
    a = rle_encoder(sys.argv[1])
    #print a
    #import pdb;pdb.set_trace()
    print rle_decoder(a)
