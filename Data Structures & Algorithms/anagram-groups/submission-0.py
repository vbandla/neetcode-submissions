class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        alpha_dict = defaultdict(list)
        for ana in strs:
            str1 = "".join(sorted(ana))
            alpha_dict[str1].append(ana)
        return list(alpha_dict.values())