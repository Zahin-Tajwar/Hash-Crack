import hashlib
import colorama
from colorama import Fore
colorama.init()

print(Fore.CYAN+'''
 _   _           _           _____                _    
| | | |         | |         /  __ \              | |   
| |_| | __ _ ___| |__ ______| /  \/_ __ __ _  ___| | __
|  _  |/ _` / __| '_ \______| |   | '__/ _` |/ __| |/ /
| | | | (_| \__ \ | | |     | \__/\ | | (_| | (__|   < 
\_| |_/\__,_|___/_| |_|      \____/_|  \__,_|\___|_|\_\

''') 

print(Fore.YELLOW+'''

1. MD5
2. SHA1
3. SHA224
4. SHA256
5. SHA384 
6. SHA512

''')
print(Fore.GREEN+" ")
mode = input("Select Option(1-6)>> ")

# To check if the password 
# found or not. 
pass_found = 0									

print(Fore.RED+" ")
input_hash = input("Enter the hashed password: ") 
print(Fore.RED+" ")
pass_doc = input("\nEnter passwords filename: ") 

try:
	pass_file = open(pass_doc, 'r')			 
except: 
	print(Fore.RED+"Error:") 
	print(pass_doc, "is not found.\nPlease give the path of file correctly.") 
	quit() 

for word in pass_file: 
	# encoding the word into utf-8 format 
	enc_word = word.encode('utf-8') 
			
	# Hasing a word
	if mode == "1":
		hash_word = hashlib.md5(enc_word.strip()) 
	if mode == "2":
		hash_word = hashlib.sha1(enc_word.strip()) 
	if mode == "3":
		hash_word = hashlib.sha224(enc_word.strip()) 
	if mode == "4":
		hash_word = hashlib.sha256(enc_word.strip()) 
	if mode == "5":
		hash_word = hashlib.sha384(enc_word.strip()) 
	if mode == "6":
		hash_word = hashlib.sha512(enc_word.strip()) 
	else:
		hash_word = hashlib.md5(enc_word.strip())

	# digesting that hash into a hexa decimal value	 
	digest = hash_word.hexdigest()		 
	
	print("\n", word, digest)

	if digest == input_hash: 
		# comparing hashes 
		print(Fore.GREEN+"\nPassword found.\nThe password is:", word) 
		pass_found = 1
		break

# if password is not found. 
if pass_found == 0: 
	print(Fore.RED+"\nPassword is not found in the", pass_doc, "file")
	print('\n') 
print("\n***************** Thank you **********************") 
