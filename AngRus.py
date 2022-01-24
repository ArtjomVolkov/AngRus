from module1 import*
rus=[]
ang=[]
#ang=lug("Ang.txt",ang)
#rus=lug("Rus.txt",rus)
#print(ang)
#print(rus)
print("Добро пожаловать в Русско-Эстониский словарь \nTere tulemast vene-eesti sõnastikku!")
while True:
	while 1:
		try:
			menu=input("\nRääkida - R \nKõik sõnad - S \nTõlgida - T \nUus sõna - U \nViga - V \nKontroll - K \nLõpp - L \n")
		except ValueError:
			print()
			print("Valige R,S,T,U,V,K,L")
			print()
		if menu.upper()=="U":
			rus=newWord("Rus.txt",input("Новое слово -> "))
			ang=newWord("Ang.txt",input("Uus sõna -> "))
		elif menu.upper()=="S":
			print(rus)
			print(ang)
		elif menu.upper()=="T":
			tolkimine(rus,ang)
		elif menu.upper()=="U":
			print()
		elif menu.upper()=="V":
			viga(rus,"Rus.txt",ang,"Ang.txt")
			#keel=input("Mis keel?")
			#if keel=="rus":
			#	rus=correction(input("Слово -> "),rus)
			#	failisse(rus,"Rus.txt")
			#else:
			#	ang=correction(input("Sõna -> "),ang)
			#	failisse(ang,"Ang.txt")
		elif menu.upper()=="K":
			test(rus,ang)
		elif menu.upper()=="L":
			print("Удачи! \nHead aega!")
			exit(0)
		elif menu.upper()=="R":
			keel=input("Mis keeles ütelda? ->")#ru et en fi
			sona=input("Sõna -> ")
			heli(sona,keel)
		else:
			break
