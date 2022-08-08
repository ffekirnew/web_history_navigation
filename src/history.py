# We are assuming you are reading this file after knowing the data structure
# we chose and why we chose it.

class Entry:
	"""
	This is a class to hold information about single entries (requests) in the history
	This mimics a node in a DLL (doubly-linked list), having previous and next attributes 
	to aid in the forwards and backwards navigation.
	"""
	def __init__(self, URL):
		self.__data = URL
		self.__previous = None
		self.__next = None

	def __repr__(self):
		return "{}".format(self.__data)

	def get_data(self):
		return self.__data

	def get_next(self):
		return self.__next

	def get_previous(self):
		return self.__previous

	def set_next(self, url):
		self.__next = url

	def set_previous(self, url):
		self.__previous = url

class History:
	"""
	class creates data structure to hold requests, allowing for addition 
	and traversing forwards and backwards.
	"""
	def __init__(self):
		self.__current = Entry(None)
		self.__recent = Entry(None)
		self.__is_empty = True

	def __str__(self) -> str:
		if self.__is_empty:
			return "No browsing history is recorded so far."
		else:
			return "You are now at: {}".format(self.__current)

	def add(self, url:str) -> None:
		'''
		this method adds a new request to the data structure
		time-complexity = O(1)
		'''
		entry = Entry(url)
		self.__recent.set_next(entry)
		if self.__is_empty: 
			entry.set_previous(None)
		else: 
			entry.set_previous(self.__recent)

		self.__recent = entry
		self.__current = self.__recent

		self.__is_empty = False

	def forward(self) -> str:
		'''
		this method traverses one step forwards through the data structure
		time-complexity = O(1)
		'''
		if self.__is_empty:
			return self
		elif self.__current.get_next() == None:
			return "that was the most recent page you visited "
		else:
			previous = self.__current
			next = self.__current.get_next().get_next()
			self.__current = self.__current.get_next()
			self.__current.set_next(next)
			self.__current.set_previous(previous)
			return "you have navigated forwards >>>"

	def backward(self) -> str:
		'''
		this method traverses one step backwards through the data structure
		time-complexity = O(1)
		'''
		if self.__is_empty:
			return self
		elif self.__current.get_previous() == None:
			return "that was the oldest page you visited"
		else:
			next = self.__current
			self.__current = self.__current.get_previous()
			self.__current.set_next(next)
			return "<<< you have navigated backwards"