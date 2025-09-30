class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sum = []
        temp = 0
        for num in nums:
            temp += num
            sum.append(temp)
        return sum