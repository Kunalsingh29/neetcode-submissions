class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
       # start heapify on array and stop at k. when you add elements to heapiy, stop at k
       pq = []
       if not nums:
        return nums
       #pq = heapq.heapify(nums)
       for num in nums: #O(n)

        heapq.heappush(pq, num)
        if len(pq)>k:
            heapq.heappop(pq)
        
       return pq[0]
    

