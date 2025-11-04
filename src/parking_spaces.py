import heapq

def min_parking_spots(intervals):
    if not intervals:
        return 0

    intervals.sort()
    heap = []  # to track end times
    spots = 0

    for s, e in intervals:
        # remove cars that already left
        while heap and heap[0] <= s:
            heapq.heappop(heap)
        # add new car
        heapq.heappush(heap, e)
        # update max spots used
        spots = max(spots, len(heap))

    return spots
