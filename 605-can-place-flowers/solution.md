The input arr could also have zeros at the edges. So we could have: [0, 0, 0], we can place 2 flowers or [0, 0, 1], we can place one flower.

We're gonna assume there are zeroes before the edges too, so if we're given [0, 0, 0], we assume: 0,[0,0,0],0. The downside
is overall space complexity gonna become O(n) because we're modifying the input arr and creating a new arr.

But there's another way to solve this problem using exact same idea(assuming there are zeros at the outside of edges), but we can do it
in O(1) memory.