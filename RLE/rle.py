
def encode(mess):
    """ Run length encoding - konverter strenge fra 'wwwwwwbbbb' til '6w4b'"""
    
    res = []
    old = mess[0]
    i = 0
    for c in mess:
        if c == old:
            i += 1
        else:
            res.append('%d%c' % (i,old))
            old = c
            i = 1
    res.append('%d%c' % (i,c))
    return ''.join(res) 
