from collections import Counter
'''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
'''
class FindDuplicate:

    def containsDuplicate(self, nums):
        # Counter works like dictionary, when list is sent to the
        # Counter which intern converts all the numbers int dictionary
        # numbers as key, it's repeation as value
        mapCounter = Counter(nums)
        for key, value in mapCounter.items():
            if key >= 2:
                return True

    #other way doing
    def containsDuplicate2(self, nums):
        myNumSet = set()
        for n in nums:
            myNumSet.add(n)

        for sn in myNumSet:
            count = 0
            for n in nums:
                if sn == n:
                    count += 1
                if count == 2:
                    return True

if __name__ == '__main__':
    dupes = FindDuplicate()
    flag = dupes.containsDuplicate([1,2,1,2,3,4,5,1,1,2,5,6,7,8,9,9])
    print(flag)
