from Crypto import Random
from Crypto.Cipher import AES
 
def encrypt(message, key=None, key_size=256):
    def pad(s):
        x = AES.block_size - len(s) % AES.block_size
        return s + (chr(x) * x)
 
    padded_message = pad(message)
 
    if key is None:
        key = Random.OSRNG.posix.new().read(key_size // 8)
 
    iv = Random.OSRNG.posix.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
 
    return (iv + cipher.encrypt(padded_message), key)
 
def decrypt(ciphertext, key):
    unpad = lambda s: s[:-ord(s[-1])]
    iv = ciphertext[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext))[AES.block_size:]
 
    return plaintext
 
if __name__ == '__main__':
    message = b'my secret message'
 
    encrypted = encrypt(message)
    decrypted = decrypt(*encrypted)
 
    assert decrypted == message
