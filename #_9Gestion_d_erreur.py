#coding:utf-8


"""
	type d'erreurs standars:		ValueError
									TypeError
									AssertionError
									ZeroDivisionError
									OSError
									NameError (Quand on a définit une variable qui n'existe pas!!!)


"""


x = input("Entrez votre âge:	")

try: #Essayer
        x = int(x)
except:#Faire une exception
        print("Votre âge est invalide")
else:#dans le cas contraire
        print("Pour confirmation vous avez bien {} ans?".format(x))
finally:#Faire l'instruction à chaque fois (try--except--else) =========== il s'execute toujours
        print("END OF THE PROGRAM")



print("Nous allons faire une division")

nbre_1 = input("Entrez un nombre:	")
nbre_2 = input("Entrez un second nombre:	")

try:
        nbre_1 = int(nbre_1)
        nbre_2 = int(nbre_2)
        
except ZeroDivisionError:
        print("Un nombre ne peut pas être divisé par 0!!!")

except ValueError:
        print("Le nombre que vous avez entré est invalide!!!")
else:
        print(f"La division de {nbre_1} par {nbre_2} est : {nbre_1 / nbre_2}")

finally:
        print("END OF THE PROGRAM")


#==================================================================LEVER UNE ERREUR=============================================================================

a = 123
b = 0

if not b:
	raise OSError("Ouahh quel talent!!! Votre machine va exploser!!!")