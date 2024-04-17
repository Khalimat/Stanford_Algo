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


"""
Given a string s, find the length of the longest 
substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        A solution with O(n) time complexity, a bit memory greedy
        Saves last position where a particular symbol appeared
        using a list where symbol position based on its ascii  code

        :param s: input string
        :return: max_len, int
        """
        
        max_len = 0
        start = 0
        last_position = [-1 for i in range(0, 128)]

        for i in range(len(s)):
            a_code = ord(s[i])

            if last_position[a_code] == -1: # check if symbol appeared before
                max_len = max(i - start + 1, max_len)
                last_position[a_code] = i
            else:
                if last_position[a_code] >= start: # if symbol appeared before current substring
                    start = last_position[a_code] + 1
                    last_position[a_code] = i
                else:
                    max_len = max(i - start +1, max_len)
                    last_position[a_code] = i
        return max_len