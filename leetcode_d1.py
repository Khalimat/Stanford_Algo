###########
# Problem 1, two sum

"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
Only one valid answer exists.
"""




class Solution(object):
    def twoSum(self, nums, target):
        """
        A solution with O(n*2) time complexity
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


class Solution(object):
    def twoSum(self, nums, target):
        """
        A solution with O(n) time complexity

        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        hashtable = {}
        for i in range(len(nums)):
            lookup_num = target - nums[i]
            if lookup_num in hashtable:
                return [i, hashtable[lookup_num]]
            hashtable[nums[i]] = i


###########
# Problem 2, Add twp numbers

"""
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):

    def sum_a_b(self, a, b, carry):
        if a + b + carry > 9:
            return int(str(a + b + carry)[1]), int(str(a + b + carry)[0])
        else:
            return a + b + carry, 0

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        head_val, carry = self.sum_a_b(l1.val, l2.val, carry)
        head = ListNode(head_val)
        previous = head

        while l1.next != None and l2.next != None:
            l1 = l1.next
            l2 = l2.next
            current_val, carry = self.sum_a_b(l1.val, l2.val, carry)
            current = ListNode(current_val)
            previous.next = current
            previous = current

        while l2.next != None:
            l2 = l2.next
            current_val, carry = self.sum_a_b(0, l2.val, carry)
            current = ListNode(current_val)
            previous.next = current
            previous = current

        while l1.next != None:
            l1 = l1.next
            current_val, carry = self.sum_a_b(0, l1.val, carry)
            current = ListNode(current_val)
            previous.next = current
            previous = current

        if carry != 0:
            current = ListNode(carry)
            previous.next = current
            previous = current

        return head
