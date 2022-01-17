def rus_failist(f:str,u:list):
	"""
	"""
	fail=open(f,'r',encoding="utf-8-sig")
	for rida in fail:
		u.append(rida.strip())
	fail.close()
	return u

def ang_failist(a:str,p:list):
	"""
	"""
	fail=open(a,"r")#чтение файла
	for rida in fail:
		p.append(rida.strip())
	fail.close()
	return p

def rida_salvestamine(f:str,rida:str):
	fail=open(f,"a")#режим до записи
	fail.write(rida+"\n")
	fail.close()