class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
            num_set = set(nums)
            print(len(nums))

            if len(num_set) != len(nums):
                return True
            else:
                return False