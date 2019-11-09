def ft_filter(function_to_apply, list_of_inputs):
	tab = []
	for item in list_of_inputs:
		if function_to_apply(item) == True:
			tab.append(item)
	return tab


ages = [5, 12, 17, 18, 24, 32]

adults = ft_filter(lambda x: False if x < 18 else True, ages)
print(list(adults))
