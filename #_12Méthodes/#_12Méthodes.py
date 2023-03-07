#coding:utf-8

"""
	types de Méthodes:	Méthode simple
						Méthode de classe
						Méhode statique

"""

class Humain:
	"""docstring for Humain"""

	human_numbers = 0
	planette = "Terre"

	def __init__(self, nom, prenom, age, numéro):

		self.nom = nom
		self.prenom = prenom
		self.age = age
		self.numéro = numéro
		Humain.human_numbers += 1

	def num_packet(self):#self = méthode standard
		return self.numéro - self.age

	def change_planet(cls, new_planet): #cls = méthode de classe
		Humain.planette = new_planet

	nom_variable = classmethod(change_planet)

	def human_definition():
		print('L\'humain à été créé par Jésus de Nazareth !!!')

	variable_name = staticmethod(human_definition)
			

if __name__ == "__main__":

	h1 = Humain("Jean", "Bernard", 14, 56)
	h2 = Humain("Ramamiharison", "Manoa Elie", 16, 20)

	print(h1.num_packet())
	print(Humain.human_numbers)

	Humain.nom_variable("Mars")
	print(Humain.planette)

	Humain.variable_name()