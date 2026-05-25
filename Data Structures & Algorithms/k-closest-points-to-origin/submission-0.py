class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(point):
            x = point[0]
            y = point[1]
            return x**2 + y**2
        self.heap = []
        for point in points:
            distance = dist(point)

            heapq.heappush(self.heap, (-distance, point))
            if len(self.heap)>k:
                heapq.heappop(self.heap)
            
        result = []
        for (distance, point) in self.heap:
            result.append(point)

        return result