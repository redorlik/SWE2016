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

if __name__ == '__main__':
    import sys
    a = rle_encoder(sys.argv[1])
    #print a
    #import pdb;pdb.set_trace()
    print rle_decoder(a)
