class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """ 
        if not s:
            return 0
    
        sub = []
        max_len = 0

        for char in s:
            if char in sub:
                sub = sub[sub.index(char) + 1:]
            sub.append(char)
            max_len = max(max_len, len(sub))

        return max_len