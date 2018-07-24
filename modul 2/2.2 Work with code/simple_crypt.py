import simplecrypt

with open("encrypted.bin", "rb") as inp:
    encrypted = inp.read()
dec = ""
with open("passwords.txt", "r") as pas:
    for line in pas:
        try:
            dec = simplecrypt.decrypt(line.strip(), encrypted)
            print(dec)
        except:
            print("Except ")
