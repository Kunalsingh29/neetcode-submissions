class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        q = deque() # to add pair,count and time to the queue. based on time add back to heap
        time = 0
        while maxHeap or q:
            time+=1
            if maxHeap:
                count_remain = 1+ heapq.heappop(maxHeap)
                if count_remain:
                    q.append([count_remain, time+n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])

        return time
