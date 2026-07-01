class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen={}
        for num in nums:
            seen[num]=seen.get(num,0)+1
        #create bucket
        bucket=[[] for _ in range(len(nums)+1)]
        #fill the buckets
        for num,frq in seen.items():
            bucket[frq].append(num)
        #collect the top k
        result=[]
        for i in range(len(bucket)-1,0,-1):
            for num in bucket[i]:
                result.append(num)
                if len(result)==k:
                    return result






            
           