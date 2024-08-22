package main

type LRUCache struct {
	cap   int
	cache map[int]*Node
	left  *Node
	right *Node
}

type Node struct {
	key  int
	val  int
	prev *Node
	next *Node
}

func Constructor(capacity int) LRUCache {
	left := &Node{}
	right := &Node{}

	left.next = right
	right.prev = left

	return LRUCache{
		cap:   capacity,
		cache: make(map[int]*Node),
		left:  left,
		right: right,
	}
}

// T: O(1)
// M: O(1)
func (this *LRUCache) removeNode(node *Node) {
	prev, nxt := node.prev, node.next
	prev.next = nxt
	nxt.prev = prev
}

// T: O(1)
// M: O(1)
func (this *LRUCache) insertNodeAtEnd(node *Node) {
	prev, nxt := this.right.prev, this.right
	prev.next, nxt.prev = node, node
	node.prev, node.next = prev, nxt
}

// T: O(1)
// M: O(1)
func (this *LRUCache) Get(key int) int {
	if node, ok := this.cache[key]; ok {
		this.removeNode(node)
		this.insertNodeAtEnd(node)

		return node.val
	}

	return -1
}

// T: O(1)
// M: O(1)
func (this *LRUCache) Put(key int, value int) {
	if node, ok := this.cache[key]; ok {
		this.removeNode(node)
	}

	this.cache[key] = &Node{
		key: key,
		val: value,
	}
	this.insertNodeAtEnd(this.cache[key])

	if len(this.cache) > this.cap {
		lru := this.left.next
		this.removeNode(lru)
		delete(this.cache, lru.key)
	}
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * obj := Constructor(capacity);
 * param_1 := obj.Get(key);
 * obj.Put(key,value);
 */
