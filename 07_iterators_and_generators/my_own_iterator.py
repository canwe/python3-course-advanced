"""
An iterator that can iterate over a string of letters:
All you need to do is implement the __iter__ and __next__ methods in your class.
"""
class MyIterator:

	def __init__(self, letters):
		"""
		Constructor
		"""
		self.letters = letters
		self.position = 0

	def __iter__(self):
		"""
		Returns itself as an iterator
		"""
		return self

	def __next__(self):
		"""
		Returns the next letter in the sequence or raises StopIteration
		"""
		if self.position >= len(self.letters):
			raise StopIteration
		letter = self.letters[self.position]
		self.position += 1
		return letter


if __name__ == '__main__':
	i = MyIterator('abcd')
	for item in i:
		print (item)
# a
# b
# c
# d
