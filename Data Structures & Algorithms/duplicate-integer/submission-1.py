class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
       set_uni = set()
       for num in nums:
        if num in set_uni:
            return True
        set_uni.add(num)    
       return False      