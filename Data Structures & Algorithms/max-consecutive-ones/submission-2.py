class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxSum, i, counter = 0, 0, 0
        while (i < len(nums)):
            if (nums[i] == 1):
                counter += 1
                if maxSum < counter:
                    maxSum = counter
            if (nums[i] == 0):
                counter = 0
            i +=1
        return maxSum
        