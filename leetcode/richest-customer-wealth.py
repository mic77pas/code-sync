class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        richest = 0
        for account in accounts:
            total = 0
            for money in account:
                total += money
            if total > richest:
                richest = total
        return richest