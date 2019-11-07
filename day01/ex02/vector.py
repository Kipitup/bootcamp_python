class Vector:
	def __init__(self, init_values):
		if isinstance(init_values, list) == True:
			self.values = init_values
			self.lenght = len(init_values)
		elif isinstance(init_values, int) == True:
			self.values = []
			for i in range(0, init_values):
				self.values.append(i * 1.0)
			self.lenght = init_values
		elif isinstance(init_values, tuple) == True:
			self.values = []
			for i in range(init_values[0], init_values[1]):
				self.values.append(i * 1.0)
			self.lenght = init_values

	def __add__(self, other):
		tmp = [x + other for x in self.values]
		return tmp

	def __str__(self):
		txt = str(self.values)
		return txt
