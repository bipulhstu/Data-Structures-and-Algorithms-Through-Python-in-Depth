class Stack:

	def __init__(self):
		self.items = []
		
	def isEmpty(self):
		return self.items == []
		
	def push(self, data):
		self.items.append(data)
		
	def pop(self):
		data = self.items[-1]
		del self.items[-1]
		return data
		#or return self.items.pop()
	def peek(self):
		if not self.isEmpty():
		    return self.items[-1]
	def sizeStack(self):
		return len(self.items)

	def get_stack(self):
		return self.items

def reverse_string(stack, input_str):
	#Loop through the string and push contents
	#character by character onto stack
	for i in range(len(input_str)):
		stack.push(input_str[i])
	rev_str = ""
	while not stack.isEmpty():
		rev_str += stack.pop()

	return rev_str

stack = Stack()
input_str = "Hello World"
print(reverse_string(stack, input_str))