# Run length encoder :
#
# Skal konvertere feks. 'kkkbb' til '3k2b'
#
#
def compound(count,old):
    if old.isdigit():
        res = '%d\\%s' %(count,old)
    else:
        res = '%d%s' %(count,old)
    return res

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
            result.append(compound(count,old))
            old = ch
            count = 1
    result.append(compound(count,old))
    return ''.join(result)

def rle_decoder(code):
    i = 0
    j = 0
    result = []
    while j < len(code):
        ch = code[j]
        if '0' <= ch <= '9':
            i = 10*i
            i += int(ch)
        elif ch == '\\':
            j += 1
            ch = code[j]
            result.append(i*ch)
            i = 0
        else:
            result.append(i*ch)
            i = 0
        j += 1
    return ''.join(result)

if __name__ == '__main__':
    import sys
    a = rle_encoder(sys.argv[1])
    import pdb;pdb.set_trace()
    rle_decoder(a)
