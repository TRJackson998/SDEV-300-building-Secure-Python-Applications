"""
Password Excercise
==================
Password crackers can easily be written using Python code. You can also generate a
hashed password using Python with a variety of hash algorithms. For this exercise, you will create use
Python code to generate ten (10) passwords with different hashing algorithms and then use a popular
online password cracking website to see if the passwords can be cracked.

For your activity, experiment with the Python script using MD-5, SHA-256 and SHA-512 hash algorithms
for at least 20 different passwords. Be sure to experiment with “easy” passwords, salted passwords as
well as randomly generated passwords (e.g. from sites such as Norton password generator
(https://my.norton.com/extspa/passwordmanager?path=pwd-gen).

Author
------
Terrence Jackson

Last Modified
-------------
4.9.24

Class
-----
UMGC SDEV 300
"""

import hashlib
import secrets
import string


def generate_secure_password(length: int, salt: str = "") -> str:
    """
    Uses the secrets library to generate a password
    args: letters, salt
    returns generated password as a string
    """
    alphabet = string.ascii_letters + string.punctuation + string.digits

    # generate password from alphabet
    password = "".join(secrets.choice(alphabet) for _ in range(length))
    password = salt + password
    return password


def main():
    """Driver function"""
    salt_ = "SDEV 300 Building Secure Python Applications"

    # hash 5 easy passwords
    for i in range(5):
        password = f"password{i}"
        print(password)
        password = password.encode()
        print("MD5:    " + hashlib.md5(password).hexdigest())
        print("SHA256: " + hashlib.sha256(password).hexdigest())
        print("SHA512: " + hashlib.sha512(password).hexdigest())
        print()

    # hash 5 easy passwords with salt
    for i in range(5):
        password = salt_ + f"password{i}"
        print(password)
        password = password.encode()
        print("MD5:    " + hashlib.md5(password).hexdigest())
        print("SHA256: " + hashlib.sha256(password).hexdigest())
        print("SHA512: " + hashlib.sha512(password).hexdigest())
        print()

    # hash 5 randomly generated paswords
    for i in range(10, 31, 5):
        password = generate_secure_password(i)
        print(password)
        password = password.encode()
        print("MD5:    " + hashlib.md5(password).hexdigest())
        print("SHA256: " + hashlib.sha256(password).hexdigest())
        print("SHA512: " + hashlib.sha512(password).hexdigest())
        print()

    # hash 5 randomly generated paswords with salt
    for i in range(10, 31, 5):
        password = generate_secure_password(i, salt=salt_)
        print(password)
        password = password.encode()
        print("MD5:    " + hashlib.md5(password).hexdigest())
        print("SHA256: " + hashlib.sha256(password).hexdigest())
        print("SHA512: " + hashlib.sha512(password).hexdigest())
        print()


if __name__ == "__main__":
    main()
