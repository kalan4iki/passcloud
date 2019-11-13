#from Cryptodome.Cipher import Salsa20
from Cryptodome.Cipher import ChaCha20
from base64 import b64encode
import hashlib
isxtext = b'World'
key = b'12345678'
mdkh = hashlib.md5(key)
mdk = mdkh.hexdigest()
cipher = ChaCha20.new(key=mdk.encode())
crytext = cipher.encrypt(isxtext)
print(crytext)
print(cipher.nonce)
#nonce = b64encode(cipher.nonce)
