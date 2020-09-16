def encrypt(key, character):
    return (((ord(character)+key) - 97)%26)

def decrypt(key, character):
    return (((ord(character)-key) - 97)%26)

def decryption(key, ct):
    pt = []
    for x in ct:
        pt.append(chr(decrypt(key,x) +97))

    return "".join(pt)

def main():
    ct = input("Enter cipher text: ")
    for key in range(1, 27):
        print("key = ",key," ", decryption(key, ct))
main()
