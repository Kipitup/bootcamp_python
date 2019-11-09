import time
from random import randint

def log(fonction_a_decorer):
	def wrapper_autour_de_la_fonction_originale(self, arg2=None):
		if arg2 is not None:
			fonction_a_decorer(self, arg2)
		else:
			fonction_a_decorer(self)
	return wrapper_autour_de_la_fonction_originale


class CoffeeMachine():
	water_level = 100
	@log
	def start_machine(self):
		if self.water_level > 20:
			return True
		else:
			print("Please add water!")
			return False

	@log
	def boil_water(self):
		return "boiling..."

	@log
	def make_coffee(self):
		if self.start_machine():
			for _ in range(20):
				# time.sleep(0.1)
				self.water_level -= 1
			print(self.boil_water())
			print("Coffee is ready!")

	@log
	def add_water(self, water_level):
		# time.sleep(randint(1, 5))
		self.water_level += water_level
		print("Blub blub blub...")

if __name__ == "__main__":
	machine = CoffeeMachine()
	for i in range(0, 5):
		machine.make_coffee()
	machine.make_coffee()
	machine.add_water(70)


# @decorateur_tout_neuf
# def une_fonction_intouchable():
#     print("Je suis une fonction intouchable, on ne me modifie pas !")
#
# une_fonction_intouchable()

# une_fonction_intouchable_decoree = decorateur_tout_neuf(une_fonction_intouchable)
# une_fonction_intouchable_decoree()
