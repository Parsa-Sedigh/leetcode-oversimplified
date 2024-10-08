class Node:
	def __init__(self, key, val):
		self.key, self.val = key, val

		# we want a doubly linked list.
		self.prev = self.next = None

class LRUCache:

	# Note: The first node is the least recently used node and last one is most recently used.
	def __init__(self, capacity: int):
		self.cap = capacity
		self.cache = {} # map key to node

		# dummy nodes point (tell us) what are the least recent and most recent values. Dummy node means it's .next will tell us the
		# actual node we want
		# the left is all the way at left and right is all the way at right
		# left = LRU , right = most recently used. But note: left and right are dummy nodes, so their .next field will actually tell
		# us the lru node and most recently used node
		self.left, self.right = Node(0, 0), Node(0, 0)

		# initially we want these nodes to be connected to each other. Because if we're put()ing a new node, we wanna put it in the
		# middle between left and right
		self.left.next, self.right.prev = self.right, self.left

	# remove from doubly linked list
	# Look at 146-1 img.  m nm
	# Note: node is the middle node
	def removeNode(self, node):
		prev, nxt = node.prev, node.next

		# By doing this, the node is no longer in the middle of prev and nxt(it doesn't exist in the linked list anymore)
		prev.next, nxt.prev = nxt, prev

	# insert node at the right of doubly linked right before the right dummy node(so that it becomes the most recently used which is pointed by
	# right dummy node)
	# Look at 146-2 img.
	def insertNodeAtEnd(self, node):
		prev, nxt = self.right.prev, self.right

		# insert node at the middle of prev and nxt
		prev.next = nxt.prev = node

		# update the new node pointers
		node.next, node.prev = nxt, prev

	def get(self, key: int) -> int:
		# everytime we get() a value, we want it to be the most recently used
		if key in self.cache:
			# remove the node related to this key from linked list and re-insert it at the right most position
			# Note: The value of the key in hashmap is a pointer to the respective node and we know that the remove and insert
			# methods want a node in their param. So pass that val which is a pointer to the node.
			self.removeNode(self.cache[key])
			self.insertNodeAtEnd(self.cache[key])

			return self.cache[key].val

		return -1

	def put(self, key: int, value: int) -> None:
		if key in self.cache:
			# we don't need to do: self.insertNodeAtEnd(), because inserting is done at the next lines of this method.
			self.removeNode(self.cache[key])

		# with this, the value of the key in hashmap is a pointer to the new node(but this node is not in the linked list yet)
		self.cache[key] = Node(key, value)

		# we also need to insert the new node in the list
		# Note: setting the prev and next fields of the new node is done at `insertNodeAtEnd()` method
		self.insertNodeAtEnd(self.cache[key])

		if len(self.cache) > self.cap:
			# remove the `lru` from linked list and also remove or evict it from the hashmap(cache)
			lru = self.left.next
			self.removeNode(lru)

			# This is why we stored not only the value but also the key, in the Node class Note: We wanna remove the
			# first node in the linked list. It's key is stored inside itself. Do not make the mistake that the key of
			# the first node that we wanna remove, is the `key` param of this func! The key param of this func is
			# the key we wanna insert, but the key of the first node is stored inside itself(it's `lru.key`)
			del self.cache[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)