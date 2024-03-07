"""Password"""
import hashlib

def password():
    """password"""
    passkey = str(input())
    encodepass = passkey.encode("utf-8")
    sha512 = hashlib.sha512()
    sha512.update(encodepass)
    print(sha512.hexdigest().upper())

password()
