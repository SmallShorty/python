
def BinToHex(realnum_bin, fracnum_bin):
    realnum_dec = 0; fracnum_dec = 0;
    
    for i in range(len(realnum_bin)):
        realnum_dec += int(realnum_bin[i]) * 2**(len(realnum_bin)-i-1)
    
    for i in range(len(fracnum_bin)):
        fracnum_dec += int(fracnum_bin[i]) * 2**(-(i+1))
    
    realnum_hex = toHex(realnum_dec)

    fracnum_hex = ''

    while True:
        fracnum_dec *= 16
        num = RealFraq(fracnum_dec)
        fracnum_hex+=toHex(int(num[0]))
        if num[1] != '0':
            fracnum_dec = num[1]
            fracnum_dec = float('0.'+str(num[1]))
        else:
            break

    return str(realnum_hex+'.'+fracnum_hex)

def toHex(num_dec):
    num_hex = ''
    hex_l = ['A', 'B', 'C', 'D', 'E', 'F']
    while num_dec > 0:
        ost = num_dec % 16
        if ost < 10:
            num_hex = str(ost) + num_hex
            num_dec //= 16
        else:
            num_hex = hex_l [ost%10] + num_hex
            num_dec //= 16 
    return num_hex

def RealFraq(n):
    r, f = str(n).split('.')
    return r, f


realnum, fracnum = input().split('.')

print(BinToHex(realnum, fracnum))
