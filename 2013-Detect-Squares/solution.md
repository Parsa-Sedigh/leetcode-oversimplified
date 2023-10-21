There is a trick for detecting the squares or generic rectangles within a grid.

We could have duplicate points in the exact same spot of grid and we do want to store those.

Since the count of how many each point that we have matters(we could have duplicate points), we're gonna be using a hashmap to count
number of occurrences for each point.

## The trick:

The most brute force way is gonna be n^3(n cubed). Why? Let's say we're given a query point, then we wanna run through all possible 
combinations of the remaining three points. So we wanna do a loop for the top left point and another loop for all the combinations of second
node(nested loop) with the nodes of first loop(bottom left) and another nested loop for every bottom right node and then we check does this
current combination of four points, form a square or not?

This is not efficient.

We're gonna see a trick that applies rectangles(more generic than squares, but a square is what we want in this problem).
So instead of detecting squares, we wanna detect rectangles.

We're given a point, we wanna find a diagonal point from it. So instead of doing three(n-length) nested loops to find every single valid
matching 3 points, we just gonna run a single loop and supposing that every single point in the loop was the diagonal point from the query point
that we're given. Now we wanna verify if it could form a square. How do we know if this diagonal point with that query point could form a square?
The answer is: the height difference of them or the y difference of them, has to be the exact same as the width distance or the x distance between them.
Once we have verified that, then we can instantly check in O(1) if it's possible that these two form an actual square, given the current points
that we have. How can we check it with O(1)? Well we do have a hashmap. Let's say the coordinates of the query point are: (px, py) and the
coordinates of the bottom left point is (x, y). Now we wanna find a valid top left point. How can we check that?
By taking the x coordinate of bottom left point and y coordinate of top right point and checking if that exists in our hashmap. In other words,
we check if (x, py) exist in the hashmap.

For checking if a valid bottom right point exist in the hashmap, we check if (px, y) exist in the hashmap?

This is gonna be a O(1) operation. With these we can instantly check if we can form a square or not.

But remember we could have 3 copies of the top left point and two copies of bottom right point and ...

Note: The O(n) loop is only iterating through the diagonal list of points.

Time: O(n)