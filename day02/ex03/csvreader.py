import csv

class CsvReader():
	def __init__(self, sep=',', header=False, skip_top=0, skip_bottom=0):
		self.sep = sep
		self.header = header
		self.skip_top = skip_top
		self.skip_bottom = skip_bottom

class Loadjson(CsvReader):
	def __init__(self, filename, sep=',', header=False, skip_top=0, skip_bottom=0):
		super().__init__(sep=',', header=False, skip_top=0, skip_bottom=0)
		self.filename = filename

	def __enter__(self):
		return self

	def __exit__(self, type, value, traceback):
		pass

	def getdata(self):
		the_file = open(self.filename, newline='')
		spamreader = csv.reader(the_file)
		for row in spamreader:
			print(' '.join(row))

	def getheader(self):
		print('header')
		pass

if __name__ == "__main__":
	with Loadjson('good.csv') as file:
		data = file.getdata()
		header = file.getheader()
