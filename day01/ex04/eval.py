class Evaluator:
	def zip_evaluate(coefs, words):
		if len(coefs) != len(words):
			print(-1)
			exit()
		x = zip(coefs, words)
		ret = 0
		for k,v in x:
			ret += k * len(v)
		print(ret)

	def enumerate_evaluate(coefs, words):
		if len(coefs) != len(words):
			print(-1)
			exit()
		x = enumerate(coefs, 0)
		ret = 0
		for k,v in x:
			print(k,v)
			# ret += k * len(v)
		print(ret)


words = ["Le", "Lorem", "Ipsum", "est", "simple"]
coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
Evaluator.enumerate_evaluate(coefs, words)
