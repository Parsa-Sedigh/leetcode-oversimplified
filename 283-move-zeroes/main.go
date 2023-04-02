package problem283

func moveZeroes(nums []int) {
	//////////////////// approach 1 ////////////////////
	/* (time limit would be exceeded): By creating a new variable called answer */

	//numZeros := 0
	//
	//var answer []int
	//
	//for i := 0; i < len(nums); i++ {
	//	fmt.Println("hello 0", len(nums), i, nums)
	//	if nums[i] == 0 {
	//		numZeros++
	//	}
	//}
	//
	//for i := 0; i < len(nums); i++ {
	//	if nums[i] != 0 {
	//		answer = append(answer, nums[i])
	//	}
	//}
	//
	//for numZeros > 0 {
	//	answer = append(answer, 0)
	//	numZeros--
	//}
	//
	//for i := 0; i < len(nums); i++ {
	//	nums[i] = answer[i]
	//}

	//////////////////// approach 2 ////////////////////
	/* two-pointer  */

	//lastNonZeroIndex := 0

	//for i := 0; i < len(nums); i++ {
	//	if nums[i] != 0 {
	//		nums[lastNonZeroIndex] = nums[i]
	//		lastNonZeroIndex++
	//	}
	//}
	//
	//for i := lastNonZeroIndex; i < len(nums); i++ {
	//	nums[i] = 0
	//}
	////////////////////

	// approach 3: TODO
}
