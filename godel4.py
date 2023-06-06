"""
CAUSION: To use on SMALL files ONLY !!!
          DO NOT USE ON LARGE FILES !!!
"""

import argparse
import os

bbin = lambda b, n = 8: bin(b)[2:].zfill(n)[-n:]

class Godel4:
    """
    Cryptography algorithm based on Gödel numbering
    that splits each byte's encoding into chunks of 4 bits
    """
    @staticmethod
    def encrypt_byte(byte : int) -> int:
        """
        Encrypt a specific byte
        """
        byte = bbin(byte)
        primes = [2, 3, 5, 7, 11, 13, 17, 19]
        result = 1
        
        for i, p in enumerate(primes):
            result *= p ** int(byte[i])
        
        return result


    @staticmethod
    def decrypt_byte(bytes6 : int) -> int:
        """
        Decrypt a specific byte
        """
        primes = [2, 3, 5, 7, 11, 13, 17, 19]
        bin_rep = ['1' if bytes6 % p == 0 else '0' for p in primes]
        return int(''.join(bin_rep), 2)


    @staticmethod
    def encrypt_bytes(bytes_ : bytes) -> bytes:
        """
        Encrypt given bytes
        """
        result = []

        for i, b in enumerate(bytes_):
            enc = bbin(Godel4.encrypt_byte(b), 24)
            enc = [enc[i : i + 4] for i in range(0, len(enc), 4)]
            enc = list(map(lambda x: int(x, 2), enc))[::1 if i % 2 == 0 else -1]
            result += enc
        
        return bytes(result)


    @staticmethod
    def decrypt_bytes(bytes_ : bytes) -> bytes:
        """
        Decrypt given bytes
        """
        if (len(bytes_) % 6 != 0):
            raise Exception("Wrong format")
        
        chunks = [bytes_[i : i + 6] for i in range(0, len(bytes_), 6)]
        result = []

        for i, c in enumerate(chunks):
            dec = [b for b in c]
            dec = ''.join(list(map(lambda x: bbin(x, 4), dec))[::1 if i % 2 == 0 else -1])
            result.append(Godel4.decrypt_byte(int(dec, 2)))

        return bytes(result)
            

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Godel - 4 bit')
    parser.add_argument('-e', '--encrypt', action = 'store_true', help = 'Encrypt')
    parser.add_argument('-d', '--decrypt', action = 'store_true', help = 'Decrypt')
    parser.add_argument('filepath', type = str, help = 'The file to operate on')
    args = parser.parse_args()

    filepath = args.filepath
    if not os.path.isfile(filepath):
        print('[!] The file does not exist')
        exit(-1)
    
    with open(filepath, 'rb') as file:
        data = file.read()
    
    if args.encrypt and not args.decrypt:
        data = Godel4.encrypt_bytes(data)
    elif not args.encrypt and args.decrypt:
        data = Godel4.decrypt_bytes(data)
    else:
        print('[!] Operation has not been specified')
        exit(-2)
    
    with open(filepath, 'wb') as file:
        file.write(data)