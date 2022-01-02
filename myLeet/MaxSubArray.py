'''
Given an integer array nums, find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.

A subarray is a contiguous part of an array.



Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
'''
class MaxSubArray:
    def maxSubArray(self, nums):
        currentSum = 0
        # assign large negative value
        maxSum = -9999999
        for index, value in enumerate(nums): #enumerate gives the array index and value
            currentSum += value
            if currentSum > maxSum: #current sum is compared with maxSum
                maxSum = currentSum #re setting

            if value > maxSum: #individual number is compared with the maxSum
                maxSum = value #re setting
                currentSum = value #re setting

            if value > currentSum: #individual number should be greater currentSum is checked
                currentSum = value #re setting

        return maxSum


if __name__ == '__main__':
    maxSubArray = MaxSubArray()
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    maxSubArraySum = maxSubArray.maxSubArray(nums)
    print(f'Max sub array is {maxSubArraySum}')