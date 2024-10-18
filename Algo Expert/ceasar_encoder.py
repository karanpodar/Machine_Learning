def caesarCipherEncryptor(string, key):
    # Write your code here.
    
    out = []
    newkey = key % 26
    for i in range(len(string)):
        newVal = ord(string[i]) + newkey
        out.append(chr(newVal) if newVal <= 122 else chr((newVal % 122) + 96))

    return ''.join(out)