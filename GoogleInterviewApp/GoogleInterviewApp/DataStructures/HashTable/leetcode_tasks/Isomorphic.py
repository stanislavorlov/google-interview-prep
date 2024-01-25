# we can map a character only to itsef or to one other
# no two character should map to the same char
# replacing each character in string s with the character it is mapped to results  in string t

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t_mapping = {}
        t_to_s_mapping = {}

        for sC, tC in zip(s,t):
            if sC not in s_to_t_mapping and tC not in t_to_s_mapping:
                s_to_t_mapping[sC] = tC
                t_to_s_mapping[tC] = sC
            elif s_to_t_mapping.get(sC) != tC and t_to_s_mapping.get(tC) != sC:
                return False

        return True

sol = Solution()
print(sol.isIsomorphic("egg", "add"))       # true
print(sol.isIsomorphic("foo", "bar"))       # false
print(sol.isIsomorphic("paper", "title"))   # true