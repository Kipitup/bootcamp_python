class Account(object):
	ID_COUNT = 1
	def __init__(self, name, **kwargs):
		self.id = self.ID_COUNT
		self.name = name
		self.value = 0
		self.__dict__.update(kwargs)
		if hasattr(self, 'value'):
			self.value = 0
		Account.ID_COUNT += 1
	def transfer(self, amount):
		self.value += amount
	def __str__(self):
		txt = 'ID: ' + str(self.id) + '\nName: ' + self.name
		txt += '\nValue of account: ' + str(self.value)
		txt += '\n' + '-' * 30
		return txt

class Bank(object):
	"""The bank"""

	def __init__(self):
		self.account = []
	def add(self, account):
		self.account.append(account)

	def check_account(self, account):
		list = dir(account)
		print(len(list))
		if len(list) % 2 == 0:
			raise ValueError('lenght')
			return False
		elif hasattr(account, 'name') == False:
			raise ValueError('name')
			return False
		else:
			return True

	def transfer(self, origin, dest, amount):
		"""
		@origin: int(id) or str(name) of the first account
		@dest: int(id) or str(name) of the destination account
		@amount: float(amount) amount to transfer
		@return True if success, False if an error occured
		"""
		self.fix_account(origin)
		self.fix_account(dest)
		if origin.value > amount:
			origin.transfer(-amount)
			dest.transfer(amount)

	def fix_account(self, account):
		"""
		fix the corrupted account
		@account: int(id) or str(name) of the account
		@return True if success, False if an error occured
		"""
		try:
			self.check_account(account)
			return True
		except ValueError as e:
			print(e)
			if str(e) == 'name':
				account.__setattr__('name', 'a name')
			elif str(e) is 'lenght':
				account.__setattr__('a_test', 'a test')
			return False

	def __str__(self):
		txt = 'account are: ' + str(self.account)
		for i in range(len(self.account)):
			txt += str(self.account[i])
		return txt

amartino = Account('amartino',  voila='voila')
user2 = Account('user2', voila='voila')
TheBank = Bank()
amartino.transfer(100)
TheBank.add(amartino)
TheBank.transfer(amartino, user2, 20)
print(amartino)
print(user2)
