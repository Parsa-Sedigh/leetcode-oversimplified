/////////// sorting approach ///////////

/**
 * @param {number} k
 * @param {number[]} nums
 */
var KthLargest = function(k, nums) {
    this.nums = nums.sort((a, b) => b - a)
    this.k = k
};

/**
 * @param {number} val
 * @return {number}
 */
KthLargest.prototype.add = function(val) {
    this.nums.push(val)
    this.nums.sort((a, b) => b-a)

    return this.nums[this.k - 1]
};

/////////////////// min heap approach ///////////////////

const swap = (a, b) => {
    const tmp = a
    a = b
    b = tmp
}

/**
 * @param {number} k
 * @param {number[]} nums
 */
var KthLargest2 = function(k, nums) {
    // nums.push(nums[0])
    // this.heap = nums

    // cur = (this.heap - 1) / 2

    // while (cur > 0) {
    //     let i = cur

    //     while (2 * i < this.heap.length) {
    //         if (2 * i + 1 < this.heap.length &&
    //             this.heap[2 * i + 1] < this.heap[2 * i] &&
    //             this.heap[i] > this.heap[2 * i + 1]) {
    //                 swap(this.heap[i], this.heap[2 * i + 1])
    //         } else if (this.) {}
    //         else break
    //     }
    // }
};

/**
 * @param {number} val
 * @return {number}
 */
KthLargest2.prototype.add = function(val) {
    return this.nums[this.k - 1]
};



/**
 * Your KthLargest object will be instantiated and called as such:
 * var obj = new KthLargest(k, nums)
 * var param_1 = obj.add(val)
 */