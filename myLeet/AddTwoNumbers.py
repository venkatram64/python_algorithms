'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored
in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
'''
# Definition for singly-linked list.

class AddTwoNumbers:
    def addTwoNumbers(self, l1, l2):
        l1Num = self.convertToNum(l1)
        l2Num = self.convertToNum(l2)

        sum = l1Num + l2Num

        newNums = []
        while sum > 0:
            remainder = sum % 10
            newNums.append(remainder)
            sum = sum // 10
        return newNums


    def convertToNum(self, nums):
        newNum = 0
        for n in nums:
            newNum = newNum * 10 + n

        return newNum




if __name__ == '__main__':
    addTwoNums = AddTwoNumbers()
    l1 = [2,4,3]
    l2 = [5,6,4]
    #nums = addTwoNums.convertToNum(l1)
    nums = addTwoNums.addTwoNumbers(l1, l2)
    print(nums)

