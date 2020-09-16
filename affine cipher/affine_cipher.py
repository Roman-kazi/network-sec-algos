
# CONSTANTS
a = 7
b = 5

m = 26
alpha_key = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12,
'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}

numeric_key = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k', 11: 'l', 12: 'm',
 13: 'n', 14: 'o', 15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'v', 22: 'w', 23: 'x', 24: 'y', 25: 'z'}

def mmi(n): # modular multiplicative invers
    i = 1
    while(1):
        ans = (n*i) % 26
        if ans == 1:
            return i
        i += 1

def encryption(pt):
    # E(x) = (ax+b)mod m
    ct = []

    for x in pt:
        if x == ' ':
            ct.append(' ')
        else:
            ct_chr = (a * alpha_key[x] + b)%m
            #print("ct_chr ", ct_chr)
            ct.append( numeric_key[ct_chr] )
    return "".join(ct)

def decryption(ct):
    # D(x) = a^-1(x - b)mod m
    pt = []
    a_inverse = mmi(a)
    print("a inverse = ", a_inverse)
    for x in ct:
        if x == ' ':
            pt.append(' ')
        else:
            pt_chr = (a_inverse*(alpha_key[x] - b))% m
            pt.append( numeric_key[pt_chr] )
    return "".join(pt)

def main():
    print("a = ",a)
    print("b = ",b)
    print("m = ",m)
    pt = input("Enter Plain text: ").lower()
    print("Affin cipher: ", encryption(pt))

    ct = input("Enter Cipher text: ").lower()
    print("Decrypted text: ", decryption(ct))

main()
