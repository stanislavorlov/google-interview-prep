# we can map a character only to itsef or to one other
# no two character should map to the same char
# replacing each character in string s with the character it is mapped to results  in string t

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t_mapping = {}
        t_to_s_mapping = {}

        for sC, tC in zip(s,t):
            temp1 = ''
            temp2 = ''
            if sC in s_to_t_mapping:
                temp1 = s_to_t_mapping[sC]
            
            if tC in t_to_s_mapping:
                temp2 = t_to_s_mapping[tC]

            if ((len(temp1) or len(temp2)) and temp1 != tC and temp2 != sC):
                return False

            s_to_t_mapping[sC] = tC
            t_to_s_mapping[tC] = sC

        return True

sol = Solution()
print(sol.isIsomorphic("egg", "add"))       # true
print(sol.isIsomorphic("foo", "bar"))       # false
print(sol.isIsomorphic("paper", "title"))   # true