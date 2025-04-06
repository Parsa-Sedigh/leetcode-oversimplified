from typing import List

# My solution
class Solution:
	def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
		self.adjList = {i: [] for i in range(numCourses)}

		if not prerequisites:
			return self.adjList

		for crs , pre in prerequisites:
			self.adjList[crs].append(pre)

		white = set(self.adjList.keys())
		grey = set()

		# sets are not sorted. Use a list instead.
		black = []

		while white:
			course = white.pop()

			if not self.dfs(course, grey, black):
				return []

		return black

	def dfs(self, node, grey, black):
		grey.add(node)

		for pre in self.adjList[node]:
			if pre in black:
				continue

			if pre in grey:
				return []

			if not self.dfs(pre, grey, black):
				return []

		grey.remove(node)

		if node not in black:
			black.append(node)

		return black