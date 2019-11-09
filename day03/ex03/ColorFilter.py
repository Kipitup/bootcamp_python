from ImageProcessor import ImageProcessor
import numpy as np

class ColorFilter:
	def invert(self, array):
		return  1.0 - array

	def to_blue(self, array):
		new_arr = np.zeros(array.shape)
		new_arr[:,:,2] = array[:,:,2]
		return new_arr

	def to_green(self, array):
		new_arr = array
		new_arr[:,:,0] *= 0
		new_arr[:,:,2] *= 0
		return new_arr

	def to_red(self, array):
		new_arr = array
		new_arr[:,:,1] -= new_arr[:,:,1]
		new_arr[:,:,2] += - new_arr[:,:,2]
		return new_arr

	def celluloid(self, array):
		pass

	def to_grayscale(self, array, filter):
		pass

img = ImageProcessor()
color = ColorFilter()
array = img.load('./42AI.png')
ret_img = color.to_red(array)
img.display(ret_img)
