import numpy as np

class NumPyCreator:
	def __init__(self):
		pass

	def from_list(self, lst):
		return np.array(lst)

	def from_tuple(self, tpl):
		return np.array(tpl)

	def from_iterable(self, itr):
		if isinstance(itr, list):
			arr = self.from_list(itr)
		elif isinstance(itr, tuple):
			arr = self.from_tuple(itr)
		elif isinstance(itr, dict):
			arr = np.array(list(itr.items()))
		else:
			arr = np.arange(itr[0], itr[len(itr) - 1])
		return arr

	def from_shape(self, shape, value=0):
		return np.full(shape, value)

	def random(self, shape):
		return np.random.rand(shape[0], shape[1])

	def identity(self, n):
		return np.identity(n)


an_array = [[1,2,3],[6,3,4]]
tpl = ('a', 'b', 'c')
a_dict = {'sal': 'salsalsal', 'quedu': 'quedu'}
shape = (2, 8)
npc = NumPyCreator()
print(npc.from_iterable(range(10, 15)))
print(npc.from_iterable(an_array))
print(npc.from_iterable(tpl))
print(npc.from_iterable(a_dict))
print(npc.from_shape(shape, 5))
print(npc.random(shape))
print(npc.identity(4))
