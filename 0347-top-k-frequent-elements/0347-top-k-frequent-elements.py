class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [res[0] for res in 
                (sorted({i: nums.count(i) for i in set(nums)}.items(),
                    key=lambda x: (x[1],x[0]),
                    reverse=True)[:k]
                )]

