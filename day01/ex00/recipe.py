class Recipe:
	def __init__(self, *,name, cooking_lvl, cooking_time, ingredients, description="no description", recipe_type):
		try:
			if isinstance(name, str) == True:
				self.name = name
			else:
				print("not good");
				exit();
			self.cooking_lvl = int(cooking_lvl)
			self.cooking_time = int(cooking_time)
			if isinstance(ingredients, list) == True:
				self.ingredients = ingredients
			else:
				print("not good");
				exit();
			if description != "no description":
				self.description = description
			if isinstance(recipe_type, str) == True:
				self.recipe_type = recipe_type
			else:
				print("not good");
				exit();
		except ValueError:
			print("InputError: only numbers\n");
			exit();

	def __str__(self):
		"""Return the string to print with the recipe info"""
		txt = "Recipe for " + self.name + "\nlevel: " + str(self.cooking_lvl);
		txt += "\ntime: " + str(self.cooking_time) + "\ningredients: " + str(self.ingredients);
		try:
			txt += "\ndescription: " + self.description;
		except:
			pass;
		txt += "\ntype: " + self.recipe_type;
		return txt;
