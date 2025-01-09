package _469_next_greater_element_i

// T: O(n * m^2)
// M: O(n)
// n: len of els in nums1, m: len of els in nums2
func nextGreaterElement(nums1 []int, nums2 []int) []int {
	res := make([]int, 0, len(nums1))

	for _, num := range nums1 {
		nextGreaterEl := -1

	loop2:
		for j := 0; j < len(nums2); j++ {
			if nums2[j] == num {

				for k := j; k < len(nums2); k++ {
					if nums2[k] > num {
						nextGreaterEl = nums2[j]

						break loop2
					}
				}

			}
		}

		res = append(res, nextGreaterEl)
	}

	return res
}
