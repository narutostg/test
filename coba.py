from cryptography.hazmat.primitives.ciphers import Cipher, algorithms
from cryptography.hazmat.primitives import hashes

key = b"0123456789abcdef"
cipher = Cipher(algorithms.AES(key), mode=None)

digest = hashes.SHA256()
