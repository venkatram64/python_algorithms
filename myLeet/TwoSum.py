'''

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.



Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

'''
class TwoSum:
    def processTwoSum(self, nums, target):
        hashTable = dict()
        indexPair = []

        for i in range(len(nums)):
            hashTable[nums[i]] = i  #adding elements into dictionary, num is key, i is the value

        foundPair = False
        i = 0
        while i < len(nums) and not foundPair:
            secondNum = target - nums[i]
            if secondNum in hashTable:
                if i != hashTable[secondNum]:
                    indexPair.append(i)
                    indexPair.append(hashTable[secondNum])
                    foundPair = True
            i += 1

        return indexPair

if __name__ == '__main__':
    twoSum = TwoSum()
    indices = twoSum.processTwoSum([2,7,11,15],22)
    print("Two sum indices are ", indices)
