class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap=[]
        ans=[]
        hm = Counter(nums)
        #heapq compares tuples from left to right, so it
        #will prioritize the number itself (key), not its frequency (val).
        for num,count in hm.items():
            heapq.heappush(heap,(-count,num))

        for _ in range(k):
            count,num = heapq.heappop(heap)
            ans.append(num)

        return ans