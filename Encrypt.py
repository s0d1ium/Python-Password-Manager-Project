import os
from cryptography.fernet import Fernet
import ctypes
import numpy as np
import random
import json
import PySimpleGUI as sg
import hashlib

def hash(password):

    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def save_settings(settings):
    with open('config.json', 'w') as file:
        json.dump(settings, file)

def load_settings():
    with open('config.json', 'r') as file:
        return json.load(file)

def save_count(count):
    with open("count.txt", "w") as file:
        file.write(count)

def load_count():
    with open("count.txt", "r") as file:
        return file.read()


def save_hash(file, hash):
    with open(file, "wb") as file:
        file.write(hash.encode('utf-8'))

def load_hash():
    with open("hash.txt", "rb") as file:
        return file.read()

keyfile = 'C:/Users/User/Desktop/CRYPTOGRAPHY/locale/key.key'
key = open(keyfile, 'rb').read()
checkfernet = Fernet(key)


def fernetEncrypt(password):

    passin = password.encode('utf-8')
    passwordFernet = checkfernet.encrypt(passin)

    return passwordFernet


class Operations:

    def __init__(self, platform, username, password):

        self.platform = platform
        self.username = username
        self.password = password


    def encrypt(self):

        key = open('C:/Users/User/Desktop/CRYPTOGRAPHY/locale/key.key', 'rb').read()
        fernet = Fernet(key)

        Eplat = fernet.encrypt(self.platform.encode())
        Euser = fernet.encrypt(self.username.encode())
        Epass = fernet.encrypt(self.password.encode())

        Encrypt = [[]] * 3

        Encrypt[0] = Eplat
        Encrypt[1] = Euser
        Encrypt[2] = Epass

        with open('credentials.txt', 'ab') as store:
            if os.stat('credentials.txt').st_size > 0:
                store.seek(0, 2)
                store.write(b'\n')
            for x in range(3):
                store.write(Encrypt[x])
                if x == 0 or x == 1:
                    store.write(b',')

    def Decrypt():
        fernet = Fernet(open('C:/Users/User/Desktop/CRYPTOGRAPHY/locale/key.key', 'rb').read())

        with open('credentials.txt', 'rb') as store:

            Lines = store.readlines()

            counter = 0

            for line in store:
                counter += 1
            encry = []
            buffer = []
            decry = []

            for line in Lines:
                string = bytes.decode(line)
                buffer = string.split(',')
                for x in range(len(buffer)):
                    buffer[x] = buffer[x].strip()
                encry.append(buffer)
            store.close()

            print(encry)

        for y in range(len(encry)):
            for x in range(len(encry[0])):
                encry[y][x] = encry[y][x].encode('utf-8')
                decry.append(fernet.decrypt(encry[y][x]))

        decry = np.array(decry).reshape(-1, 3)

        for y in range(len(decry)):
            for x in range(len(decry[0])):
                decry[y][x] = decry[y][x].decode('utf-8')
        return decry


    def Generate_Password(length):
        characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnoqrstuvwxyz1234567890@!£$%^&|()~#'"
        list_characters = list(characters)
        passgen = ''.join([random.choice(list_characters) for x in range(length)])

        print(passgen)

        return passgen

    def write_new_key():
        os.remove('key.key')
        file = open(keyfile, 'wb')
        key = Fernet.generate_key()
        file.write(key)
        file.close()

    def write_new_storage():
        os.remove('C:/Users/User/Desktop/CRYPTOGRAPHY/locale/credentials.txt')
        file = open('C:/Users/User/Desktop/CRYPTOGRAPHY/locale/credentials.txt', 'wb')
        file.close()

    def set_new_pass(password):

        print(password)

        hash = fernetEncrypt(password)

        print(hash)

        save_settings(hash.decode('utf-8'))

        print(hash.decode('utf-8'))

        sg.popup("New Password Set")

        print("NEW PASSWORD SET: " + hash.decode('utf-8'))


    def check_pass(password):

        print("CHECK PASS DEBUG FUNCTION")

        passin = password.encode('utf-8')

        passwordFernet = fernetEncrypt(password)


        print("Entered Password Type: ", end="")
        print(type(password))

        print("Entered Password: ", end="")
        print(password)

        print("\n")

        print("Entered Password Encrypted Type: ", end="")
        print(type(passwordFernet))

        print("Encrypted Password: ", end="")
        print(passwordFernet)

        print("\n")

        print("CHECKSETTINGS")

        print(type(checksettings))
        print(checksettings)

        print("JSON IMPORT")

        print(type(load_settings()))
        print(load_settings())

        if passwordFernet.decode('utf-8') == load_settings():
            return True
        return False

    def check_pass_debug(password):

        print("CHECK PASS DEBUG FUNCTION")

        print(password)

        passwordFernet = fernetEncrypt(password)

        print(passwordFernet)
        save_settings(passwordFernet.decode('utf-8'))

        print(passwordFernet.decode('utf-8'))

        #print("SAVE NEW PASSWORD DEBUG")

        '''hash = fernetEncrypt(password)
        save_settings(hash.decode('utf-8'))'''

        #print("PASSWORD TEST")

        #print("PASSWORD ENCRYPTED: " + passwordFernet.decode('utf-8'))

        json_import = load_settings()

        #print("LOAD FROM SETTINGS")

        #print(type(json_import))
        print("IMPORTED FROM SETTINGS: " + json_import)

        if passwordFernet.decode('utf-8') == json_import:
            return True
        return False

    def set_new_pass_hash(password):

        '''print(type(hash(password)))'''

        save_hash("hash.txt", hash(password))
        save_count("1")
        '''print("hash set debug")
        print(hash(password))'''

    def check_pass_hash(password):

        hash = load_hash()
        '''print("loaded from settings: ", end="")
        print(hash)

        print("hash of entered password: ", end="")
        print(hashlib.sha256(password.encode('utf-8')).hexdigest())'''

        if hashlib.sha256(password.encode('utf-8')).hexdigest().encode('utf-8') == hash:
            return True
        return False

    def check_count_is_0():
        count = load_count()

        if int(count) == 0:
            return True
        return False





