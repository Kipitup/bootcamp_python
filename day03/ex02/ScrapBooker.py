from ImageProcessor import ImageProcessor
import numpy as np

class ScrapBooker:
	def crop(self, array, dimensions, position=(0, 0)):
		dim = np.shape(array)
		if dimensions[0] > dim[0] or dimensions[1] > dim[1]:
			print('error')
			exit()
		return array[position[0]:position[0] + dimensions[0], position[1]:position[1] + dimensions[1]]

	def thin(self, array, n, axis):
		return np.delete(array, np.s_[::n], axis)

	def juxtapose(self, array, n, axis):
		new_arr = array
		for i in range(1, n):
			new_arr = np.concatenate((new_arr, array), axis)
		return new_arr

	def mosaic(self, array, dimensions):
		new_arr = self.juxtapose(array, dimensions[0], 0)
		new_arr = self.juxtapose(new_arr, dimensions[1], 1)
		return new_arr

img = ImageProcessor()
scrapBook = ScrapBooker()
array = img.load('./42AI.png')
crop = scrapBook.mosaic(array, (2, 3))
img.display(crop)
