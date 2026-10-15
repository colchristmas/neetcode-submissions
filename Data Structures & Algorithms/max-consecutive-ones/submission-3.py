class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxSum, counter = 0, 0
        for num in nums:
            if num == 1:
                counter += 1
                maxSum = max(maxSum, counter)
            else:
                counter = 0
        return maxSum