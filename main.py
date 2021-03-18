# Password Generator

# Imports
import string as s
import random as r

# Creation of Charset
charset = s.ascii_letters + s.digits + s.punctuation

# User enters the length of password.
# Password 's length must be 8-16 characters,
# in order to be secure and rememberable at the same time.
length = int(input("Give password's length (8-16 chars): "))

# Creation of random password
password = "".join(r.sample(charset, length))

print("Your random password is:", password)
