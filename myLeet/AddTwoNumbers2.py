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
class ListNode(object):
   def __init__(self, val=0, next=None):
       self.val = val
       self.next = next
       
class AddTwoNumbers:

    def addTwoNumbers(self, l1, l2):
        carry = 0
        result = ListNode(0)
        pointer = result

        while (l1 or l2 or carry):
            first_num = l1.val if l1.val else 0
            second_num = l2.val if l2.val else 0

            sum = first_num + second_num + carry

            num = sum % 10
            carry = sum // 10

            pointer.next = ListNode(num)

            pointer = pointer.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return result.next

    def convertListIntoLinkedList(self, nums):
        head = None

        for i, j in enumerate(nums):
            node = ListNode(val=j, next=head)
            head = node
        return head

    def readLinkedList(self, ll):
        current = ll
        while current is not None:
            print(current.val)
            current = current.next




if __name__ == '__main__':
    addTwoNums = AddTwoNumbers()
    l1 = [2,4,3]
    l2 = [5,6,4]
    ll_1 = addTwoNums.convertListIntoLinkedList(l1)
    addTwoNums.readLinkedList(ll_1)
    ll_2 = addTwoNums.convertListIntoLinkedList(l2)
    addTwoNums.readLinkedList(ll_2)
    print("******************")
    nums = addTwoNums.addTwoNumbers(ll_1, ll_2)
    addTwoNums.readLinkedList(nums)

