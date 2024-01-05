class ListNode:
	def __init__(self, key):
		self.key = key
		self.next = None

class MyHashSet:

	def __init__(self):
		# pre-allocate the memory
		# Why of size 10^4? Because that's how many calls are gonna be made to add() . So that's gonna be the maximum number of keys
		# that we probably gonna end up inserting. Why "probably"? Because there could be duplicate keys which are gonna be overwritten.
		# So no new key would be added(no increase in size). Technically we could make it smaller than this if we wanted to, but that would end up
		# giving us more collisions potentially, but since we're not implementing rehashing, it's gonna get bad. So instead, we pre-allocate the
		# maximum size for the underlying arr.
		# Note: Instead of just initializing the elements to be 0, we're gonna create a dummy node for every position because that would make
		# handling the edge cases a tiny bit easier.
		# Note: This is a bug: [ListNode(0)] * 10**4 . It'll copy the exact same pointer in every position, it's not gonna create a NEW ListNode
		# for every position. To fix it, we say: [ListNode(0) for i in range(10**4)] which is gonna create a new ListNode for every position.
		self.set = [ListNode(0) for i in range(10**4)]

	def hash(self, key: int):
		return key % len(self.set)

	def add(self, key: int) -> None:
		index = self.hash(key)

		# get the head of the linked list at the position `index` and create a new pointer named cur and then iterate to the end of that
		# linked list pointed by the dummy node(which we don't care) and insert a new node with `key`
		cur = self.set[index]

		# Why cur.next? Because we wanna skip the dummy node.
		# Note: This while loop will stop when cur is at the last node
		while cur.next:
			# if we detect a duplicate, we don't need to do anything.
			# Note: The reason we say cur.next.key and not cur.key is we wanna skip the dummy node
			if cur.next.key == key:
				return

			cur = cur.next

		cur.next = ListNode(key)

	def remove(self, key: int) -> None:
		index = self.hash(key)
		cur = self.set[index]

		while cur.next:
			if cur.next.key == key:
				cur.next = cur.next.next

				return

			cur = cur.next


	def contains(self, key: int) -> bool:
		index = self.hash(key)
		cur = self.set[index]

		while cur.next:
			if cur.next.key == key:
				return True

			cur = cur.next

		return False

class MyHashSet2:

	def __init__(self):
		self.hashset = []

	def add(self, key: int) -> None:
		if not self.contains(key):
			self.hashset.append(key)

	def remove(self, key: int) -> None:
		if self.contains(key):
			self.hashset.remove(key)

	def contains(self, key: int) -> bool:
		return True if key in self.hashset else False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)