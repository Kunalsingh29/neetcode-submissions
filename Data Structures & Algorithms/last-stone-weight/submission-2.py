class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """ create a max heap with top element representing max element and second as second max. 
        operate on these 2 values and add the remaining value back into the heap data structure"""
        # create max hep of nums
        if not stones:
            return 0
        self.pq = [-stone for stone in stones]

        heapq.heapify(self.pq)
        while len(self.pq) > 1:
            stone_1 = -heapq.heappop(self.pq)
            stone_2 = -heapq.heappop(self.pq)

            result_weight = stone_1 - stone_2
            if stone_1 != stone_2:
                heapq.heappush(self.pq, -(stone_1 - stone_2))
        
        return -self.pq[0] if self.pq else 0




        

 

       