package main

import "fmt"

/* We have 2 portions. One portion will be shifted to the end of the array and the other portion is the last k elements.
The last portion will be shifted all the way to the beginning of the array.

Let's rotate the array.

Now if we look at the array, we can rotate the first k elements and then also rotate the remaining.

Note: We can reverse the array using two pointers. Using a normal for loop with iteration over all elements of array you wanna rotate, won't do anythinf!*/

func rotate(nums []int, k int) {
	k = k % len(nums)
	l, r := 0, len(nums)-1

	// reverse the array
	for l < r {
		tmp := nums[r]
		nums[r] = nums[l]
		nums[l] = tmp
		l++
		r--
	}

	l = 0
	r = k - 1

	for l < r {
		tmp := nums[r]
		nums[r] = nums[l]
		nums[l] = tmp
		l++
		r--
	}

	l = len(nums) - k
	r = len(nums) - 1

	fmt.Println("nums", nums)
	for l < r {
		tmp := nums[r]
		nums[r] = nums[l]
		nums[l] = tmp
		l++
		r--
	}

	fmt.Println("nums 2", nums)
}

func main() {
	rotate([]int{1, 2, 3, 4, 5, 6, 7}, 3)
}
