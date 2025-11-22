class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vistos = {}
        for i, num in enumerate(nums):
            if (complemento := target - num) in vistos:
                return [vistos[complemento], i]
            vistos[num] = i
        return []