import heapq
from collections import defaultdict
from typing import List


class Twitter:

	def __init__(self):
		# It may be better to call this variable `time`, but it's really counting the number of tweets. So we can maintain
		# which tweet was created earlier than another tweet by comparing their count(each tweet is gonna be a pair of [count, tweetId])
		self.count = 0

		# Or self.tweetMap = {} . If this was the case, we had to initialize the list value before add() to it.
		self.tweetMap = defaultdict(list) # userId -> list of [count, tweetIds]
		self.followMap = defaultdict(set) # userId -> set of followeeId

	def postTweet(self, userId: int, tweetId: int) -> None:
		self.tweetMap[userId].append([self.count, tweetId])

		# we decrement this to use this in our min heap to simulate a max heap using negative values
		self.count -= 1

	def getNewsFeed(self, userId: int) -> List[int]:
		res = [] # ordered starting from the most recent
		minHeap = []

		# The question described we want the 10 most recent tweets from the people that user follows INCLUDING HIMSELF. So a user
		# is technically following himself as well(to see his tweets in the newsFeed).
		# This is kinda dumb!
		self.followMap[userId].add(userId)

		for followeeId in self.followMap[userId]:
			# Note: We're not 100% sure that this followeeId even has any tweets that they created. So before we look into his
			# tweets in the tweetMap, let's see if he at least has one tweet:
			if followeeId in self.tweetMap:
				# We want the most recent tweet of followeeId(his frontier tweet)
				index = len(self.tweetMap[followeeId]) - 1
				count, tweetId = self.tweetMap[followeeId][index]

				# initially just append to the minHeap(which it's still a regular array, not a minHeap, we would heapify later, after we added
				# every value needed)
				# NOTE: The first value of a list that we put in the array which later would become a minHeap, is what's used as the key
				# by python to order the elements of minHeap.
				# Note: We added followeeId as well, because after we popped this tweet(list of 4 values) from the minHeap, we also want the
				# next tweet from this followeeId. So we need to add this followeeId as well.
				# Note: We store `index - 1` as well to have the next position(actually previous) we're gonna look at in our list as long as it's
				# greater than or equal to 0. Basically as long as there are still elements in that list for that followeeId
				minHeap.append([count, tweetId, followeeId, index - 1])

		heapq.heapify(minHeap)

		# We want to pop at most 10 values(tweets)
		while minHeap and len(res) < 10:
			count, tweetId, followeeId, index = heapq.heappop(minHeap)

			# At this point, we have popped the most recent tweet yet
			res.append(tweetId)

			if index >= 0:
				# Now if this followeeId has anymore tweets, we want to get that tweet and that tweet is gonna be at `index` of his corresponding
				# list in tweetMap(remember we wanna potentially get previous tweets of him as well).
				count, tweetId = self.tweetMap[followeeId][index]

				# Remember we always add the `index - 1` in order to get the next(actually previous id) of this followeeId, the time we
				# popped this tweet from the minHeap
				heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])

		return res


	def follow(self, followerId: int, followeeId: int) -> None:
		# If we were using regular hashmap, next line would require two lines. First we would have to create an empty set and then add to it.
		# self.followMap[followerId] = set
		# self.followMap[followerId].add(followeeId)
		self.followMap[followerId].add(followeeId)

	def unfollow(self, followerId: int, followeeId: int) -> None:
		# What if this person(followerId) is actually not even following a different person? So add a condition to make sure
		# that he is following the followeeId, before we call the remove function, because at least in python, it'll throw an exception
		if followeeId in self.followMap[followerId]:
			self.followMap[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)