class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums_dict = defaultdict(int)
        for i in range(len(nums)):
            nums_dict[nums[i]] += 1
        k = 0
        for key in [0, 1, 2]:
            value = nums_dict[key]
            while(value > 0):
                nums[k] = key
                value -= 1
                k += 1
