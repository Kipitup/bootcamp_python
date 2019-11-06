 class Book:
	def __init__(self, *,name, last_update, creation_date, recipes_list):
		if isinstance(name, str) == True:
			self.name = name;
		else:
			print("not good");
			exit();
		self.last_update = last_update;
		self.creation_date = creation_date;
		self.recipes_list = recipes_list;

	def get_recipe_by_name(self, name):
		"""Print a recipe with the name `name` and return the instance"""
		pass
	def get_recipes_by_types(self, recipe_type):
		"""Get all recipe names for a given recipe_type """
		pass
	def add_recipe(self, recipe):
		"""Add a recipe to the book and update last_update"""
		pass
