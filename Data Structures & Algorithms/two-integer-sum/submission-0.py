class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: 
        a = 0
        b = 1

        while nums[a] + nums[b] != target:
            b += 1
            if b == len(nums):
                a += 1
                b = a + 1

        return [a, b]