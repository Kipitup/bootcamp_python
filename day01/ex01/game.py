class GotCharacter:
	def __init__(self, first_name=None, is_alive=True):
		self.first_name = first_name
		self.is_alive = is_alive

class Stark(GotCharacter):
	"""A class representing the Stark family. Or when bad things happen to good people."""

	family_name = "Stark"
	house_words = "Winter is Coming"

	def __init__(self, first_name=None, is_alive=True):
		instance = super(Stark, self)
		instance.__init__(first_name=first_name, is_alive=is_alive)

	def print_house_words():
		print(house_words)

	def die(self):
		self.is_alive = False

instance = Stark('amartino')
print(instance.first_name)
Stark.die(instance)
print(instance.is_alive)
print(instance.__doc__)
