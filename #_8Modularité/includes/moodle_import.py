#coding:utf-8
#================================================================CE FICHIER VA AVEC #_8MODULARITE====================================================================

liste = [{"Alice": 18}, {"Bob": 46}, {"lisa": 15},
		{"Joel": 21}, {"Thomas": 19}, {"Félix": 75},
		{"Paquerette": 50}, {"Julio": 12}, {"Maria": 14},
		{"Merlin": 17}, {"h4cK3rM4n04": 16}, {"Junior": 10},
		{"Maurice": 34}, {"Miguel": 30}, {"Batricia": 25}, {"Gilbert": 26},
		{"Garmadon": 25}, {"Lucke": 23}, {"Kay": 18}, {"Cole": 20}]

def Louer_Jésus():
	print("Jésus est très grand!!!")

def age_sup22(liste_param):
	nom = ""
	for x in liste_param:
		for x, y in x.items():
			if y > 22:
				nom += x + "\t"
	return nom

#Faire un test si python teste sur ce fichier (test isolé) sans le fichier :	#_8Modularité

if __name__ == "__main__":
	Louer_Jésus()
	print(age_sup22(liste))