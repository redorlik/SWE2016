# Run length encoder :
#
# Skal konvertere feks. 'kkkbb' til '3k2b'
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
            result.append('%d%s' %(count,old))
            old = ch
            count = 1
    result.append('%d%s' %(count,old))
    return ''.join(result)

def rle_decoder(code):
    i = 0
    result = []
    for ch in code:
        if '0' <= ch <= '9':
            i = 10*i
            i += int(ch)
        else:
            result.append(i*ch)
            i = 0
    return ''.join(result)

if __name__ == '__main__':
    import sys

    print rle_encoder(sys.argv[1])

