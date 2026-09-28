class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        two_list = []
        for i,num in enumerate(nums):
            print(f"num: {num}, i: {i}")
            if (target-num) in hash_map:
                two_list.append(hash_map[target-num])
                two_list.append(i)
            else:
                hash_map[num] = i
        return two_list        