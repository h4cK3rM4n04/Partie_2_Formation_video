#coding:utf-8

def dire_bonjour():
	print("Bonjour")
dire_bonjour()

liste = [{"Alice": 18}, {"Bob": 46}, {"lisa": 15},
		{"Joel": 21}, {"Thomas": 19}, {"Félix": 75},
		{"Paquerette": 50}, {"Julio": 12}, {"Maria": 14},
		{"Merlin": 17}, {"h4cK3rM4n04": 16}, {"Junior": 10},
		{"Maurice": 34}, {"Miguel": 30}, {"Batricia": 25}, {"Gilbert": 26},
		{"Garmadon": 25}, {"Lucke": 23}, {"Kay": 18}, {"Cole": 20}]

def age_sup22(liste_param = liste):
	nom = ""
	for x in liste_param:
		for x, y in x.items():
			if y > 22:
				nom += x + "\t"
	return nom
print(age_sup22())

def age_inf22(liste_param = liste):
	nom = ""
	for x in liste_param:
		for x, y in x.items():
			if y < 22:
				nom += x + "\t"
	return nom
print(age_inf22())

#L'opérateur * désigne que items peut prendre une infinité de valeurs!!!

def show_inventory(*items):
	for x in items:
		print(x)
show_inventory("=======||====================>", "épée", "arballette", "arc", "pistolet", "AK-47")

#===========Fonction spécifique lambda=======================================================================================================================================

x = lambda x, y: x + y
print(x(11, 32))


Chl_é = lambda:print("Jésus est très grand !!!")
Chl_é()