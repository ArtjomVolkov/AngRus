from module1 import*
rus=[]
ang=[]
ang=ang_failist("Ang.txt",ang)
rus=rus_failist("Rus.txt",rus)
print(ang)
print(rus)
#russlov=str(input("Добавьте русское слово ->"))
#rus=rida_salvestamine("Rus.txt",russlov)
#angslov=str(input("Add an English word ->"))
#ang=rida_salvestamine("Ang.txt",angslov)
#print(rus)
#print(ang)
print("Добро пожаловать в Русско-Английский словарь \nWelcome to the Russian-English Dictionary")
while True:
	try:
		ch=int(input("Вы хотите с Английского на Русский (1) или с Русского на Английский (2) \nDo you want from English to Russian (1) or from Russian to English (2) -> "))
	except ValueError:
		print("Выберите 1 или 2 \nChoose 1 or 2")
	if ch==1:
		print()
		print("Словарь с Английского на Русский \nDictionary from English to Russian")
		print()
	if ch==2:
		print()
		print("Словарь с Русского на Английский \nDictionary from Russian to English")
		print()
