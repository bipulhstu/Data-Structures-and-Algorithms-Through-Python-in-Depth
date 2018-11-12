class Stack:

	def __init__(self):
		self.items = []
		
	def isEmpty(self):
	#if empty array it returns true. If not empty returns false. Boolean values
		return self.items == []
		
	def push(self, data):
		self.items.append(data)
		#keep appending the given item, which is data in this case, to the stack.
		
	def pop(self):
		#stack has a LIFO structure so last item in, is the first item out
		data = self.items[-1]
		#returns the last item
		del self.items[-1]
		return data
		#or return self.items.pop()
	def peek(self):
		if not self.isEmpty():
		    return self.items[-1]
			#return last item without removing the last item
			# structure remains the same
	def sizeStack(self):
		return len(self.items)

	def get_stack(self):
		return self.items
		
