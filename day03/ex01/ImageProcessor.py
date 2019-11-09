import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

class ImageProcessor:
	def load(self, path):
		img = mpimg.imread(path)
		array = np.array(img)
		dim = np.shape(array)
		print('Loading image of dimensions ' + str(dim[0]) + ' x ' + str(dim[1]))
		return array

	def display(self, array):
		imgplot = plt.imshow(array)
		plt.show()

img = ImageProcessor()
array = img.load('./42AI.png')
print(array)
img.display(array)
