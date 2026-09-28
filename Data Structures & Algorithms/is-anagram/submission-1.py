class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = defaultdict(int)
        for char in s:
            dict_s[char] += 1

        dict_t = defaultdict(int)
        for char in t:
            dict_t[char] += 1
        if len(dict_s) != len(dict_t):
            return False
        for key, value in dict_s.items():
            if dict_t[key]!= value:
                return False
        return True