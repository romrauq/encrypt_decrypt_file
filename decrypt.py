import os
from cryptography.fernet import Fernet

os.chdir("target_folder")

files = []

for file in os.listdir():
	if file == "encrypt.py" or file == "thekey.key" or file == "decrypt.py":
		continue
	if os.path.isfile(file):
		files.append(file) 

print(files)

with open("thekey.key", "rb") as key:
	secretKey = key.read()

for file in files:
	with open(file, "rb") as thefile:
		contents = thefile.read()
	contents_decrypted = Fernet(secretKey).decrypt(contents)
	with open(file, "wb") as thefile:
		thefile.write(contents_decrypted)

print("All files within the target folder have been successfully decrypted!")