package main

func maxProfit(prices []int) int {
	maxP := 0
	l, r := 0, 1

	for r < len(prices) {
		if prices[l] < prices[r] {
			maxP = max(maxP, prices[r]-prices[l])
		} else {
			l = r
		}

		r++
	}

	return maxP
}
