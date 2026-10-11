import random

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        self.quicksort(nums, 0, n - 1)
        return nums

    def quicksort(self, nums: List[int], low, high) -> List[int]:
        if (high - low + 1) <=1:
            return
        
        p_idx = random.randint(low, high)
        nums[p_idx], nums[high] = nums[high], nums[p_idx]
        
        pivot = nums[high]
        left = low
        for i in range(low,high):
            if(nums[i]<pivot):
                tmp = nums[left]
                nums[left] = nums[i]
                nums[i] = tmp
                left += 1
        nums[high] = nums[left]
        nums[left] = pivot
        self.quicksort(nums,low, left - 1)
        self.quicksort(nums, left + 1, high)
        return nums
