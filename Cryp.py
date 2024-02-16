import os
import tkinter

import customtkinter
from cryptography.fernet import Fernet
import ctypes
import numpy as np
from tkinter import *

import Encrypt
from Encrypt import Operations

import random

passlen = int(input("Length for generated password? "))

Operations.Generate_Password(passlen)
exit()




path = "C:/Users/User/Desktop/CRYPTOGRAPHY/locale/key.key"
filepath = "C:/Users/User/Desktop/CRYPTOGRAPHY/locale"
Check = os.path.exists(path)
CheckFile = os.path.exists(filepath)

if CheckFile == False:
    os.mkdir("locale")

new = input("Want to generate new key? (y/n)")
clear = input("Do you want to clear store credentials? (y/n)")
if new == 'y' and Check == True:
    Operations.write_new_key()

if clear == 'y' and os.path.exists("C:/Users/User/Desktop/CRYPTOGRAPHY/locale/credentials.txt") == True:
    Operations.write_new_storage()

if Check == False:
    file = open('C:/Users/User/Desktop/CRYPTOGRAPHY/locale/key.key', 'wb')
    key = Fernet.generate_key()
    file.write(key)
    file.close()

EnDe = input("Encryption or decryption? (e/d)")

if EnDe == 'e':
    platform = input("Platform: ")
    User = input("Username: ")
    Pass = input("Password: ")

    Operations(platform, User, Pass).encrypt()

    ctypes.windll.kernel32.SetFileAttributesW("C:/Users/User/Desktop/CRYPTOGRAPHY/locale", 2)

if EnDe == 'd':

    Operations.Decrypt()

    ctypes.windll.kernel32.SetFileAttributesW("C:/Users/User/Desktop/CRYPTOGRAPHY/locale", 2)







