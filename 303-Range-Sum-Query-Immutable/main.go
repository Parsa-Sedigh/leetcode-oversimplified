package main

type NumArray struct {
	prefix []int
}

func Constructor(nums []int) NumArray {
	prefix := make([]int, 0, len(nums))
	total := 0

	for _, n := range nums {
		total += n
		prefix = append(prefix, total)
	}

	return NumArray{
		prefix: prefix,
	}
}

func (n *NumArray) SumRange(left int, right int) int {
	preRight := n.prefix[right]
	var preLeft int

	if left > 0 {
		preLeft = n.prefix[left-1]
	}

	return preRight - preLeft
}

/**
 * Your NumArray object will be instantiated and called as such:
 * obj := Constructor(nums);
 * param_1 := obj.SumRange(left,right);
 */
