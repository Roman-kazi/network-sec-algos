# unicode of a = 97 = 122

def encrypt(key, character):
    return (((ord(character)+key) - 97)%26)

def decrypt(key, character):
    return (((ord(character)-key) - 97)%26)

def encryption(key, pt):
    ct = [] # (p + k )mod 26
    for x in pt:
        ct.append(chr(encrypt(key,x) +97))
    return "".join(ct)

def decryption(key, ct):
    pt = []
    for x in ct:
        pt.append(chr(decrypt(key,x) +97))

    return "".join(pt)

def main():
    # key value must be between 1 to 26
    key = int(input("Key: "))
    if key > 26:
        print("Invalid key")
        return False

    plain_text = input("Plain Text: ").lower()
    print("Cipher text: ", encryption(key, plain_text))
    cipher_text = input("Cipher Text: ").lower()
    print("Plain text: ", decryption(key, cipher_text))
main()
