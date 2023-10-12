Similar to the problem `Merge k sorted list`.

This problem is about what DSs are we gonna use for each of these methods. So you have to have an understanding of the tradeoffs,
to make sure you implement each of the methods in the most efficient way.

Let's start with the implementation of `follow` and `unfollow` methods.

A user with `followerId` can follow another user with `followeeId`. The easiest DS you wanna consider is a map. We wanna map
a user `followerId` to another user `followeeId`. A user can actually not just follow one person, but they could follow multiple people.
So the simplest idea is to create a hashmap and map the userId to a List of followeeIds. That's just our naive approach.

So everytime a user follows another user, we can add a new value to the end of the list of followeeIds in `O(1)`. But in `unfollow`,
we need to remove from the list and we know removing from a list is not as easy as adding to the end of that list. Because we might
have to search through the entire list to find the followeeId that we're trying to remove and then removing it, is gonna be `O(n)`.

Q: Is there a more efficient way?

A: There is a DS that can add and remove in O(1). Hashmap is one of the those DSs, but in this case, we don't need a map, we just need a
set of values. In this case, we can use a `hashset` and that can insert and remove in `O(1)`. So instead of using a list, we're gonna map
each userId to a hashset of followeeIds(instead of a list).

---

Now about `postTweet` and `getNewsFeed`:

Let's start with postTweet. We need to be able to map a userId to their list of tweets. So again we're gonna have a hashmap mapping each
userId to the list of his tweets and each time we post a tweet for any given user, we just add that tweetId and add it to the end of that
list. This is the most naive approach. This is actually going to work for us. 

So in postTweet, since we're adding to the end of the list each time, we can do that in `O(1)`.

Till now, we've made `follow`, `unfollow` and `postTweet` functions running in `O(1)` . But the `getNewsFeed` is going to be by far the most complex function.

getNewsFeed:

Q: How do we get most recent tweets?

Anytime a user posts a tweet, we're already adding it to the **end** of the list of his tweets. So the most recent tweets are gonna be at the end
of the list for any given user. **But** we don't have just one user. So a user won't only see his tweets so that we can easily show him
his most recent tweets at the end of the list, we **also** need to show him the most recent tweets of his followees. Maybe the user followes
two people, the first person has these tweet ids: [1, 2, 3] and the second person he follows: [4, 5, 6]. We can't just compare these
tweet Ids. So instead of just having a list of tweet ids, how about we also keep track of the **time** that that tweet was posted?
So in that case, we won't just have a list of tweet ids, we'll have a list of **pairs** and each pair is: [count, tweetId]. Why we called it count
instead of time? Because that's what we're gonna keeping track of for time. We don't actually have a time, we have count of how many total tweets
we have at the moment and we actually gonna start our count at 0 and then we're gonna decrement it to -1, -2, -3. It has to do with us using
a heap and in python there's not a max heap, so we're gonna use a min heap but with negative values.

Note: We can't just use the tweet ids to get the 10 most recent tweets. Because according to the problem description, each call to
`postTweet` will generate a unique tweet id, so tweets are not generated in chronological order. So we need another value to order
the tweets based on time.

So 2 DSs we're gonna use:
- hashmap - userId -> hashset of followeeIds
- hashmap - userId -> list of [count, tweetId]

Q: How do we order the tweets in news feed from most recent to least recent?

A: This is exactly like merge k sorted lists. The naive way to do this would run in `O(10*k)` where `k` is number of people that that user
follows. Why? Because if we're trying to get the most recent tweets(order them), OFC we're gonna start at the end of each list(each person
that this user follows has a list of tweetIds). So we're gonna have a pointer for each list at the end of it and we're gonna compare the values
that these pointers point to, which one occurred most recently?
For example, we have multiple lists of counts. So for each followee, we have a list of his counts(first element of each pair of `[count, tweetId]`).
For example, we have: `[-1, -3, -5], [-2, -4], [-6, -7]`. At the beginning, the pointers point to the last element of each list. Now the smallest
value is -7. We're gonna add it to the list named for example `res`. Then we're gonna decrement the pointer of that list to now point to the previous
value(-6). We're gonna keep repeating this. If you're using java, since java has max heap, since the count is gonna be positive, these values in these
lists would also be positive.

So the reason the time is `O(10 * k)` is because we have k lists and to find the minium between k values, it's `O(k)` operation.

This was the naive approach but if you have solved the `merge k sorted lists` before, you know we don't have to do it in naive way,
the slightly more optimal way to do this is to take our frontier for all these lists(frontier el means wherever the pointers are), take those
frontiers and add it to a DS called heap. We want min heap because we want the minimum value. It's gonna be `O(log k)`(pushing to heap) and we're gonna
do this operation at most 10 times. So the time complexity with heap is `O(10 * log k)`. So this is better than `O(10 * k)` which we previously
had. Right?

**Not quite actually** and that's the dumb part about this. Because even if you do use a min heap, it doesn't really change the overall
time complexity. Why?

Because let's say we take each of the k values and we add them to the heap. We can add these values in two different ways:
1. we can push each of them into heap, which will result in `O(k * log k)`(just to push these k values to the min heap)
2. or we can run heapify which would be `O(k)`. This is in addition to our `10 * log k`, it makes the overall time complexity still `O(k)`
which is what we already originally had.

So it actually doesnt' change the overall time complexity, but the benefit is if we were running this algorithm(with min heap) in a generic
case where we didn't have to return 10 tweets, maybe we had to return up to n tweets, our algo(using a heap) would be more efficient.

Note: Do follow, unfollow, postTweet, getNewsFeed in order.

The reason we're using `defaultdict()s` is to save a couple of lines. We could instead initialize tweetMap and followMap to 
a regular hashmap(`{}`), but in that case each time we're adding values to the list of the corresponding key, we have to first
initialize that list before using add() on it. Look at the comments.

**Note:** count(first element of a tweet - note that each tweet is a pair of values) is gonna be unique for every single tweet.
