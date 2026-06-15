class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        seen={}
        for str in strs:
            sorted_str="".join(sorted(str))
            if sorted_str in seen:
                seen[sorted_str].append(str)
            else:
                seen[sorted_str]=[str]
        return list(seen.values())
            


