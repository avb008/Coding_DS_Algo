class Node:
	# Constructor
	def __init__(self,value):
		self.value = value
		self.next = None

class LinkedList:
	# Constructor
	def __init__(self,value):
		new_node = Node(value)
		self.head = new_node
		self.tail = new_node
		self.length = 1

	# Print the linked list
	def print_list(self):
		temp = self.head
		while temp is not None:
			print(temp.value, end = " ")
			temp = temp.next

	def append(self, value):
		new_node = Node(value)
		temp = self.head
		if temp is None:
			self.head = new_node
			self.tail = new_node

		temp = self.tail
		self.tail = new_node
		temp.next = new_node
		self.length += 1

		return True


	def pop(self):
		if self.length == 0:
			return None

		pre = self.head
		temp = self.head
		while temp.next :
			pre = temp
			temp = temp.next


		self.tail = pre
		self.tail.next = None
		self.length -= 1

		if self.length == 0:
			self.tail = None
			self.head = None

		return temp


	def prepend(self):
		
		new_node = Node(value)
		if self.length == 0:
			self.head = new_node
			self.tail = new_node
		else:
			temp = self.head
			self.head = new_node
			new_node.next = temp
		self.length += 1

		return True


	def pop_first():
		pass

	def get():
		pass

	def set():
		pass

	def insert():
		pass

	def remove():
		pass

	def reverse(self):
		
		temp = self.head
		self.head = self.tail
		self.tail = temp

		previous = None
		after = temp.next

		for _ in range(self.length):
			after = temp.next
			temp.next = previous
			previous = temp
			temp = after

		return True






my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
print('LL before reverse():')
my_linked_list.print_list()

popped_node = my_linked_list.pop()
print(f"Value of popped_node : {popped_node.value}")

my_linked_list.append(4)

print('LL before reverse():')
my_linked_list.print_list()

my_linked_list.reverse()

print('\nLL after reverse():')
my_linked_list.print_list()




	

    