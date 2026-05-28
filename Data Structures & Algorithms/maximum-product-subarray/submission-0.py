class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        cur_max = nums[0]
        cur_min = nums[0]

        for n in nums[1:]:
            temp_max = cur_max

            cur_max = max(n, n * cur_max, n * cur_min)
            cur_min = min(n, n * temp_max, n * cur_min)

            res = max(res, cur_max)

        return res