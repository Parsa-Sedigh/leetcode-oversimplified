import collections
from typing import List

# T: O()
# M: O()
class Solution:
	def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
		# prerequisites map. Maps each course to prereq list
		# This is important: We need to create an entry for every index in numCourses so that if that entry is not among the
		# actual src and dst of prerequisites, we still would have it as a key in preMap so that we won't get an error that we're
		# accessing a key that doesn't exist in the hashmap.
		preMap = { i: [] for i in range(numCourses)}

		# create the adjacency list
		for crs, pre in prerequisites:
			preMap[crs].append(pre)

		# stores all the courses along the current DFS path
		visitSet = set()

		def dfs(crs):
			# we're visiting a course(node) twice, so we detected a loop
			# Base case 1
			if crs in visitSet:
				return False

			# Base case 2
			if preMap[crs] == []:
				return True

			visitSet.add(crs)

			# pre is a neighbor of current node(crs)
			for pre in preMap[crs]:
				if not dfs(pre):
					return False

			# When we get to here, it means there are no neighbors for the current node, so we can return True to parent, since there are
			# no prerequisites for this node so we can read it, hence we return True, but before doing that, we remove this node from set and
			# also set it's list of neighbors to [].
			# Note: we have to remove the current node from visitSet. Because yes in this path we're going backwards, but there could be another
			# course that has a path to the current crs and it's a valid path, so we need to remove this crs from visitSet so that that
			# course can still reach this one.
			visitSet.remove(crs)

			# since we know this course can be visited(because we got till here), if we ever have to run DFS on it again,
			# we would hit the base case #2 and return True immediately and we won't have to repeat running DFS on it's neighbors.
			# In other words, we don't want to compute if this node doesn't lead to cycle or not. We've already found out that it doesn't lead
			# to a dead end and we can read all of the courses(nodes).
			# Note: If you don't do this, we would get: Time Limit Exceeded error.
			preMap[crs] = []

			return True

		# Note: We have to go through all of the nodes. If you didn't use this for loop and only wrote: return dfs(0) , there are some
		# inputs that in them, some nodes are isolated, so we can't reach them from the rest and those isolated nodes have cycles.
		# So if we only did: return dfs(0) here, we won't reach those nodes and we would possibly return True instead of False(since we have
		# cycles).
		# Note: Why we're looping like this(for all courses)?
		# A: What if our graph is like this:
		# 1 -> 2
		# 3 -> 4
		# These are not connected. So we have to manually loop through every course and check if all can be completed.
		for crs in range(numCourses):
			# if any of the func calls returns false, we return false immediately. Because just having one false means we can return false
			# as the overall result.
			if not dfs(crs):
				return False

		return True

# Cracking FAANG
# T: O(V + E)
# M: O(V)
class Solution2:
	def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
		# if there is no prerequisites, we definitely can take all courses.
		if not prerequisites:
			return True

		# build the graph. The keys(nodes) are courses and the neighbors are prerequisites that we have to take before taking
		# this node.
		self.graph = collections.defaultdict(list)

		for course, prereq in prerequisites:
			self.graph[course].append(prereq)

		white = set(self.graph.keys())
		grey = set()
		black = set()

		# process the nodes in white set
		while white:
			# order of popping doesn't matter because we wanna visit all of the nodes(courses)
			course = white.pop()

			if not self.dfs(course, grey, black):
				return False

		# we visited all of the nodes in dep graph(white set), it means we took every single course, so return True
		return True

	# dfs returns True if we can visit all of the children of node successfully and False if there's a cycle
	def dfs(self, course, grey, black):
		grey.add(course)

		for prereq in self.graph[course]:
			if prereq in black:
				continue

			# grey set represents nodes that we're currently VISITING. Now we end up at it again, so we have a cycle. Cycle maens
			# we can't solve this problem.
			if prereq in grey:
				return False

			# visit all of it's children(neighbors)
			if not self.dfs(prereq, grey, black):
				return False

		grey.remove(course)
		black.add(course)

		# we have processed the course and it's prerequisites
		return True