ciphertext = "^s<qN}{;t~bp?vN}{;"
plaintext = ""

for shiftlen in range(1,129):
    for ch in ciphertext:
        plaintext +=  chr((ord(ch) - shiftlen) % 128)
    print(str(shiftlen) + "" + plaintext)
    plaintext = ""


