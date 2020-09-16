
pt_ct = {'A': 'Z', 'B': 'Y', 'C': 'X', 'D': 'W', 'E': 'V', 'F': 'U', 'G': 'T', 'H': 'S', 'I': 'R', 'J': 'Q', 'K': 'P', 'L': 'O', 'M': 'N', 'N': 'M', 'O': 'L', 'P': 'K', 'Q': 'J', 'R': 'I', 'S': 'H', 'T': 'G', 'U': 'F', 'V': 'E', 'W': 'D', 'X': 'C', 'Y': 'B', 'Z': 'A'}

pt_input = input("plain text ").upper()
#ct = []

def encrypt(pt):
    ct = []
    for i in range(len(pt)):
        if pt[i] not in pt_ct:
            ct.append(pt[i])
        else:
            ct.append(pt_ct[pt[i]])
    return "".join(ct)

def decrypt(ct):
    pt = []
    for i in range(len(ct)):
        if ct[i] in pt_ct:
            pt.append(pt_ct[ct[i]])
        else:
            pt.append(ct[i])
    return "".join(pt)
print(encrypt(pt_input))
ct_input = input("cipher text ").upper()
print(decrypt(ct_input))
