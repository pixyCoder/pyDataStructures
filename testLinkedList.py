class Node:
	def __init__(self, data=None, next=None):
		self.data = data
		self.next = next

class LinkedList:
	def __init__(self):
		self.data = None
		self.head = None

	def insert_at_beginning(self, data):
		node = Node(data, self.head)
		self.head = node

	def insert_at_end(self, data):
		if self.head is None:
			self.head = Node(data, None)
			return

		itr = self.head
		while itr.next is not None:
			itr = itr.next	

		itr.next = Node(data, None)

	def print(self):
		if self.head is None:
			print('Linked list is empty')
			return

		itr = self.head
		lldatastr = ''

		while itr is not None:
			lldatastr = lldatastr + str(itr.data) + '-->'
			itr = itr.next
		
		print('LL data string : ', lldatastr)

if __name__ == '__main__':
	ll = LinkedList()
	print()
	ll.print()
	print('Inserting elements at beginning...')
	ll.insert_at_beginning(16)
	ll.print()
	ll.insert_at_beginning(25)
	ll.print()
	ll.insert_at_beginning(36)
	ll.print()
	print('Inserting elements at end...')
	ll.insert_at_end(2)
	ll.print()
	ll.insert_at_end(3)
	ll.print()
	ll.insert_at_end(4)
	ll.print()
	print()
