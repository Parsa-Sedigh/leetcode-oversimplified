A car can never pass another car, that's because we have one lane in the road.

Once the faster car catches the slower one, it's speed is going to be reduced to the speed of the slower one because it can't
pass the slower car(which is a head of that faster car at the beginning).

Note: If the cars are right next to each other, they're basically assumed to have the same exact position. Even though technically one is
behind the other one, but they're still considered to have the same position.

So cars will intersect(collide) and become a single car fleet before they reach the destination.

So we can calculate the intersection point of cars, but there's a slightly easier way. We can just calculate what time the cars are gonna reach
the destination. If a car at the behind of current car, reaches the destination **before** or at the same time of the current car, that means they
became a car fleet somewhere in the road.

To find the time that a car reaches the destination: `(destination - initial position) / speed`.

When a car gets into a car fleet, we remove the one that was behind. So we always keep the one that comes ahead. Because if two cars collided,
they're gonna end up being reduced down to the speed of the one that's ahead. Why?

Because if we remove the one that was ahead(after it collided with another car) and now we wanna compare the one that was behind with another car,
it's gonna be harder to calculate because the one that was behind is gonna have 2 different speeds. It's initial speed and then at some point,
it's gonna change to the speed of the one that was ahead and slower. So it's easier to keep the one that's ahead, because it's speed won't change if
another car catches it.

It's better to start at right(closer to destination) and iterate at reverse order of road because we if we don't do this, a car could collied with
some other car and slow down(it's speed will be decreased when it's collided). Why? Because cars won't pass each other in this question.

**time complexity:** O(n) for going through the cars but we also have to sort the input(speed and position arrays) which is gonna be o(logn), so overall
will be `O(nlogn)`

**space complexity:** O(n)