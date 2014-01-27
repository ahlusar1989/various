from Crypto import Random
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from base64 import b64encode, b64decode 

# generates one-time key 
def encrypt_AES(message, key=None, key_size=256):
    def pad(s):
        x = AES.block_size - len(s) % AES.block_size
        return s + (chr(x) * x)
 
    padded_message = pad(message)
 
    if key is None:
        key = Random.OSRNG.posix.new().read(key_size // 8)
 
    iv = Random.OSRNG.posix.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
 
    return (iv + cipher.encrypt(padded_message), key)

def decrypt_AES(ciphertext, key):
    unpad = lambda s: s[:-ord(s[-1])]
    iv = ciphertext[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext))[AES.block_size:] 
    return plaintext

# RSA key not included
def encrypt_RSA(key, message):
    rsakey = PKCS1_OAEP.new(RSA.importKey(key))
    encrypted = rsakey.encrypt(message)
    return encrypted.encode('base64')
    
def decrypt_RSA(key, message):
    rsakey = PKCS1_OAEP.new(RSA.importKey(key)) 
    plaintext = rsakey.decrypt(b64decode(message)) 
    return plaintext
    
def generate_RSA(bits=2048):
    '''
    Generate an RSA keypair with an exponent of 65537 in PEM format
    param: bits The key length in bits
    Return private key and public key
    '''
    from Crypto.PublicKey import RSA 
    new_key = RSA.generate(bits, e=65537) 
    public_key = new_key.publickey().exportKey("PEM") 
    private_key = new_key.exportKey("PEM") 
    return private_key, public_key

if __name__ == '__main__':
    message = b'my secret message'
        
    encrypted = encrypt_AES(message)
    decrypted = decrypt_AES(*encrypted)
    assert decrypted == message
    
    private, public = generate_RSA()

    encrypted = encrypt_RSA(public, message)
    decrypted = decrypt_RSA(private, message)
    assert decrypted == message
