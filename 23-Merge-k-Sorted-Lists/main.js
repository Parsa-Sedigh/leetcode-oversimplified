function ListNode(val, next) {
    this.val = (val === undefined ? 0 : val)
    this.next = (next === undefined ? null : next)
}

///////// my naive approach /////////
/**
 * @param {ListNode[]} lists
 * @return {ListNode}
 */
var mergeKLists = function (lists) {
    const arr = []

    for (const list of lists) {
        let curr = list

        while (curr) {
            arr.push(curr.val)

            curr = curr.next
        }
    }

    arr.sort((a, b) => a - b)

    let head = new ListNode(-1)
    let curr = head

    for (const el of arr) {
        const newNode = new ListNode(el)
        curr.next = newNode

        curr = newNode
    }


    return head.next
};

//////////

// Time: O(nk log(k))
// n: The total number of elements across all k sorted lists (i.e., total length of all lists combined).
// k: The number of individual sorted lists to be merged.
var mergeKLists = function (lists) {
    if (!lists || !lists.length) {
        return null
    }

    // time: O(n)
    // `n`: the length of the shorter list between the two being merged.
    const mergeLists = (l1, l2) => {
        let dummy = new ListNode()
        let tail = dummy

        while (l1 && l2) {
            if (l1.val < l2.val) {
                tail.next = l1
                l1 = l1.next
            } else {
                tail.next = l2
                l2 = l2.next
            }

            tail = tail.next
        }

        if (l1) {
            tail.next = l1
        }
        if (l2) {
            tail.next = l2
        }

        return dummy.next
    }

    // Time of the while loop: O(log (k))
    while (lists.length > 1) {
        const mergedLists = []

        // time: O(k)
        for (let i = 0; i < lists.length; i = i + 2) {

            // time: O(n)
            mergedLists.push(mergeLists(lists[i], lists[i + 1] ? lists[i + 1] : null))
        }

        lists = mergedLists
    }

    return lists[0]
};