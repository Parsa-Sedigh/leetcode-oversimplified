First of all we need to shift the right pointer n steps ahead of left pointer and after that we move them forward each by
1 step. With this, the destination between these pointers will always remain n.

After the r pointer reaches nil, the l pointer exactly points to the node that we wanna delete and the reasons is the offset between
these pointers is n, making sure that we have the node we wanna delete after r goes out of linked list.
	
But the problem is we need to access to the previous node of where the l pointer will point **eventually**(the previous node of eventual position
of l pointer), in order to delete the node we want. 

This problem can be solved with dummy node technique. So we're gonna have another node that we insert at the beginning of the linked list
that we don't really use. So now our left pointer gonna be initialized at the dummy node instead of head. But the right pointer
initialization place should be the same. So now when the right pointer reaches end of list(out of list), the left pointer will be where
we can delete the next node which is the node we wanna delete.

**Important:** We need to return dummyNode.Next instead of head. Otherwise, in cases that we should remove the head itself, it doesn't
make sense to return the head again right? An example of such case is [1] and n = 1 which means the head itself should be removed.
In this case, the dummyNode will point to nil which means the linked list would become empty.