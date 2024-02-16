import hashlib
from cryptography.fernet import Fernet

def load_count():
    with open("count.txt", "r") as file:
        return file.read()

def check_count_is_0():
    print(type(load_count()))

    if int(load_count()) == 0:
        return True
    return False

print(load_count())
print(check_count_is_0())

string = "123"
string1 = "1234"

print(type(hashlib.sha256(string.encode('utf-8')).hexdigest()))
print(hashlib.sha256(string.encode('utf-8')).hexdigest())

key = Fernet.generate_key()
fernet = Fernet(key)

print(fernet.encrypt(string.encode('utf-8')))
print(fernet.encrypt(string1.encode('utf-8')))

