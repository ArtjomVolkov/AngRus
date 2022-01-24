
def lug(f:str,l:list):
    fail=open(f,"r",encoding="utf-8-sig")
    mas=[] 
    for rida in fail:
        l.append(rida.strip())
    fail.close()
    return l

def failisse_salvestamine(f:str,l:list):
	"""Loetelu salvaestame failisse
	"""
	fail=open(f,"w")#чтение файла
	for el in l:
		fail.write(el+"\n")
	fail.close()

def rida_salvestamine(f:str,rida:str):
	"""
	"""
	fail=open(f,"a")#режим до записи
	fail.write(rida+"\n")
	fail.close()

def newWord(f:str, rida:str)->list:
    l=[]
    with open(f,"a",encoding="utf-8-sig") as fail:
        fail.write(rida+"\n")
    l=lug(f,l)
    return l

def uus_sona(f:str,rida:str)->list:
	"""Lisame uus sõna failisse ja listisse
	:param str file: Faili nimetus
	:param str x: lisatav sõna
	"""
	l=[]
	with open(f,"a",encoding="utf-8-sig") as fail:
		fail.write(rida+"\n")
	l=failist_lugemine(f,1)
	return l

def tolkimine(l1:list,l2:list):
	"""Tõlkimine sõna
	:param list l1:
	:param list l2:
	"""
	sona=input("Mida tõlkida? ")
	if sona in l1:
		tolk=l2[l1.index(sona)]
		print(sona+"="+tolk)
	elif sona in l2:
		tolk=l1[l2.index(sona)]
		print(sona+"="+tolk)
	else:
		print("Sõna puudub sõnastikus!")

def correction(sona:str,l:list):
	for i in range(len(l)):
		if l[i]==sona:
			uus_sona=sona.replace(sona,input("Uus sõna -> "))
			l.insert(i,uus_sona)
			l.remove(sona)
	return l

def viga(l1:list,f1:str,l2:list,f2:str):
	"""
	"""
	sona=input("Sõna veaga? -> ")
	if sona not in l1 and sona not in l2:
		print("Sõna puudub!")
	else:
		if sona in l1:
			tolk=l2[l1.index(sona)]
			l1.remove(sona)
			l2.remove(tolk)
		elif sona in l2:
			tolk=l1[l2.index(sona)]
			l2.remove(sona)
			l1.remove(tolk)
		uus_sona(l1,input("Введите новое слово -> "))
		uus_sona(l2,input("Sisesta uus sõna -> "))
		failfailisse_salvestamine(f1,l1)
		failisse_salvestamine(f2,l2)

def failisse(mas:list,file:str):
	f=open(file,"w",encoding="utf-8-sig")
	for sona in mas:
		f.write(sona+"\n")
		f.close()

import os
from gtts import gTTS
def heli(text:str,keel:str):
	obj=gTTS(text=text,lang=keel,slow=False).save("heli.mp3")
	os.system("heli.mp3")
	playsound("heli.mp3")

import random
def test(l1:list,l2:list):
	"""
	"""
	print(1)
	res=0
	l3=[]
	l3.extend(l1)
	l3.extend(l2)
	random.shuffle(l3)
	print("Random list ",l3)
	for i in range(len(l1)):
		print("l1 ",l1)
		print("l2 ",l2)
		h=input(f"Переведи данное слово - '{l3[i]}': ")
		if h in l1 or h in l2:
			if l3[i] in l1:
				if l1.index(l3[i])==l2.index(h):
					res+=1
					print('правильно!')
					print()
				elif l3[i] in l2:
					if l2.index(l3[i])==l1.index(h):
						res+=1
						print('правильно!')
						print()
		else:
			print("Неправильно!")
			print()
	r=(res/len(l1))*100
	print(f"Ваш результат: {resultPer}%")