/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {void} Do not return anything, modify head in-place instead.
 */
var reorderList = function(head) {
    // find the middle
    let slow = head;
    let fast = head.next;

    while(fast && fast.next) {
        slow = slow.next;
        fast = fast.next.next;
    }

    // Note: slow is now the middle node

    // second is now the head of the second portion
    let second = slow.next;

    // we don't want to have cycles in the list(cut off the first portion from the second portion)
    slow.next = null;

    // reverse the second portion
    let prev = null

    while (second) {
        const nxt = second.next;
        second.next = prev;
        prev = second;
        second = nxt;
    }

    /* now `prev` has become the head of the second portion which is now reversed. Since we don't want to lose
    the head nodes in general, let's define two new pointers in order traverse the first and second portions(we don't
    want to traverse the lists using head pointers because otherwise we would lose the lists altogether!): */
    let first = head;
    second = prev;

    // merge first and second portions
    while(second) {
        const tmp1 = first.next;
        const tmp2 = second.next;

        first.next = second;
        second.next = tmp1;
        first = tmp1;
        second = tmp2;
    }
};

////////////////////////////////

// using arrays(space complexity O(n))
var reorderList2 = function(head) {
    const nodes = [];

    // Store all nodes from LinkedList into array
    let node = head;
    while (node) {
        nodes.push(node);
        node = node.next;
    }

    // Connecting nodes
    node = nodes[0];
    let counter = 0;
    let length = nodes.length;

    while (counter < length) {
        if (counter === length - 1) {
            node.next = null;
            break;
        }

        if (counter % 2 === 0) {
            node.next = nodes[length - Math.floor(counter / 2) - 1];
        } else {
            node.next = nodes[Math.floor(counter / 2) + 1];
        }

        node = node.next;
        counter++;
    }
};