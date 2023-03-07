#coding:utf-8
#Deux différentes formes de l'utilisation d'un module ... il est important de noter qu'il faut respecter leurs façon d'écriture!!!!!!

"""========================================ECRITURE 1========================================"""
from math import sqrt
from math import sin

liste = [{"Alice": 18}, {"Bob": 46}, {"lisa": 15},
		{"Joel": 21}, {"Thomas": 19}, {"Félix": 75},
		{"Paquerette": 50}, {"Julio": 12}, {"Maria": 14},
		{"Merlin": 17}, {"h4cK3rM4n04": 16}, {"Junior": 10},
		{"Maurice": 34}, {"Miguel": 30}, {"Batricia": 25}, {"Gilbert": 26},
		{"Garmadon": 25}, {"Lucke": 23}, {"Kay": 18}, {"Cole": 20}]

print(sqrt(100))
print(sin(42))


print("=======================================================séparation visuelle=====================================================")

"""========================================ECRITURE 2========================================"""
import math

print(math.sqrt(100))
print(math.sin(42))

print("=======================================================séparation visuelle=====================================================")

"""========================================ECRITURE 1========================================"""
import includes.moodle_import

includes.moodle_import.Louer_Jésus()
print(includes.moodle_import.age_sup22(liste))

print("=======================================================séparation visuelle=====================================================")

"""========================================ECRITURE 2========================================"""
from includes.moodle_import import Louer_Jésus
from includes.moodle_import import age_sup22
Louer_Jésus()
print(age_sup22(liste))

print("=======================================================séparation visuelle=====================================================")

# d'une autre manière je peux réecrire la fonction précédente de cette manière:

import includes.moodle_import as variable_quelconque
variable_quelconque.Louer_Jésus()