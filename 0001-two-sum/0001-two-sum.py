class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash = {}
        for i, value in enumerate(nums):
            if target - value in hash:
                return [hash[target-value], i]
            hash[value] = i