import heapq
from collections import Counter, deque
from typing import List


class Solution:
	def leastInterval(self, tasks: List[str], n: int) -> int:
		# each task 1 unit time
		# minimize idle time

		# We want to count the occurrences of each character in the input. We could just loop through the characters and increment
		# the related key of that character in hashtable, but you can do that easier with Counter hashmap builtin in python.
		count = Counter(tasks)

		# Since in python we don't have a max heap, we use a minheap but with negative values
		maxHeap = [-cnt for cnt in count.values()]

		# heapq.heapify() will take the passed array and order it in such a way that it is a max heap.
		heapq.heapify(maxHeap)

		time = 0

		# we declare a double ended queue and it's gonna contain a pair of values: [-cnt, idleTime].
		# Note: idleTime means at what time is it going to be available for us to add it back to the max heap?
		q = deque()

		# As long as one of these is not empty, that means we have more tasks that we need to process
		while maxHeap or q:
			time += 1

			# It could be the case that there is nothing in the maxHeap, because we've done all the tasks and the time for the
			# nearest task is not arrived yet, so we need to check for maxHeap not being empty.
			if maxHeap:
				# Process the task
				# Note: As we pop from the heap, that means we're processing this task. So to the cnt, we can add one to it, because
				# remember we're using negative values for the counts so we need to increment it by one to show they were processed.
				# If you were using positive values for counts in the max heap, you would subtract one from it.
				cnt = 1 + heapq.heappop(maxHeap)

				# If cnt is non-zero meaning we still have to process it again later:
				if cnt:
					# At `time + n`, we can once again add this task to our max heap
					q.append([cnt, time + n])

			# If the queue is not empty and we have reached the idleTime of first task in the queue(which can be accessed by q[0][1])
			if q and q[0][1] == time:
				heapq.heappush(maxHeap, q.popleft()[0])

		# At this point, everything has been processed from our maxHeap and queue, we can just return the time that it took us to do all that work
		return time

	# Greedy algorithm
	def leastIntervalGreedy(self, tasks: List[str], n: int) -> int:
		counter = Counter(tasks)
		max_count = max(counter.values())
		min_time = (max_count - 1) * (n + 1) + \
				   sum(map(lambda count: count == max_count, counter.values()))

		return max(min_time, len(tasks))