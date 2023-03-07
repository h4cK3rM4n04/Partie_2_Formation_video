#coding:utf-8

class Humain(object):
	"""docstring for Humain"""

	human_nbr = 0

	def __init__(self, prenom, age):

		self.prenom = prenom
		self.age = age
		Humain.human_nbr += 1

if __name__ == "__main__":

	h1 = Humain("Jojo", 1.5)
	h2 = Humain("h4cK3rM4n04", 16)
	h3 = Humain(h2.prenom[::-1], 61)
	print(Humain.human_nbr)