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
		
s = Stack()
s.push(10)
s.push(22)
s.push(33)
#pushing values into the stack, and 33 is the last item in the stack, so if pop is called 33 is the first out
print(s.sizeStack())
print("Popped: ", s.pop())
print("Popped: ", s.pop())
#33 and 22 popped out first
print(s.sizeStack())
print("Peek:", s.peek())
#peek will return 10, but size will remain the same so length of 1 is shown below
print(s.sizeStack())