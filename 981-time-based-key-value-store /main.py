class TimeMap:

	def __init__(self):
		self.store = {}  # key = string, value = [list of [value, timestamp]] OR key: list of [val, timestamp]

	def set(self, key: str, value: str, timestamp: int) -> None:
		# Instead of this if block, we could use a defaultdict
		if key not in self.store:
			self.store[key] = []

		self.store[key].append([value, timestamp])

	def get(self, key: str, timestamp: int) -> str:
		res = ""
		values = self.store.get(key, [])

		# binary search
		l, r = 0, len(values) - 1

		# While the left pointer hasn't crossed the right pointer
		while l <= r:
			m = (l + r) // 2

			# First we checked this case instead of exact match case. Why? Because this is a valid case(most recent value so far) and
			# therefore we can update the `res`
			if values[m][1] <= timestamp:
				# The result so far
				res = values[m][0]
				l = m + 1

			# Since this case is invalid(we should see an element with less than or equal to the requested timestamp), we don't update the res
			else:
				r = m - 1

		return res

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
