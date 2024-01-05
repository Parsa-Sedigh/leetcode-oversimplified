Hashsets cannot contain duplicate values.

The hard parts about implementing hashsets and hashmaps is:
1. rehashing. Because just like dynamic arrays, hashsets and hashmaps can grow in size and we don't want to start out the hashset or
hashmap with like 1,000,000 in size. But the given size in description is 10,000. So we could initialize an array with 10,000 elements,
so that we don't need to use rehash(that's why this problem is easy), but this approach is naive.
2. how do we handle collisions? The most simple way is using the chaining technique aka using a linked list.

The value of elements in the underlying arr, is gonna be a linked list node. Because that's how we're gonna handle collisions.

In case of hashset, we only care about the keys, we don't have a key->value mapping.

We want to map the given key to some index in our underlying arr and the easiest way to do that is using the mod operator(%). We mod that
key to the size of the underlying arr and when you do this, we will never get a value that's larger than the size of the arr, it will be
in bounds.

If we've added a linked list node in the same index, we don't insert another one. Because hashsets can't contain duplicates.

Why we implement rehashing? We can just append a new node to the linked list in case of collisions?

Because this gets more and more time-consuming as we add more keys that get collided, so we have to increase the size of the arr to get less
collisions to handle and workaround(but in this solution, we're not gonna implement that).

Dummy node: We won't use it, it won't be part of the returned result. It just helps us handle the edge cases easier.

Time:

In average case, usually **if** the length of the underlying arr is a prime number which helps to minimize collisions and **if** we implement rehashing
where we dynamically increase the size of the arr as it gets filled up to a certain point, we can get close to `O(1) in the average case`(not in
the worst case)

Memory:

O(n) where n is the number of keys(linked list nodes) that we have in our hashset. Technically it's more than that because we're pre-allocating
an underlying arr with the maximum size given in the description(in this case 10,000). So we could argue whether this is O(1) or O(n) or maybe
even bigger than that.