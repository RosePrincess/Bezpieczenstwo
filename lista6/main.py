#Karolina Antonik

import cryptographs
import decryptor
import n as decryptor2

def main():
    # cryptographs.change_cryptographs("kryptogramy.txt", "criptographs.txt")
    for number in range(1, 21):
        dec = decryptor.Decryptor()
        dec.get_cryptographs_from_file("criptographs.txt", number)
        dec.decode()

if __name__ == "__main__":
    main()