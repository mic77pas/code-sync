class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for i in range(len(numbers)):
            x = target - numbers[i]
            if x in hashmap:
                return [hashmap[x] + 1, i + 1]
            hashmap[numbers[i]] = i
        return []