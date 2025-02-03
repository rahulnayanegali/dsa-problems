"""
Given n ropes of different lengths, we need to connect these ropes into one rope. We can connect only 2 ropes at a time.
 The cost required to connect 2 ropes is equal to sum of their lengths. The length of this connected rope is also equal to the sum of their lengths.
  This process is repeated until n ropes are connected into a single rope. Find the min possible cost required to connect all ropes.
"""

"""
Approach:
ropes = [8, 4, 6, 12]
sort = [4, 6, 8, 12]



"""

import heapq


def min_cost_to_conneect_ropes(ropes):
    heap = ropes
    heapq.heapify(heap)

    total_cost = 0

    # while len(ropes) > 1:
    #     cur = heapq.heappop(heap) + heapq.heappop(heap)
    #     heapq.heappush(heap, cur)
    #     total_cost += cur
    return heap


print(min_cost_to_conneect_ropes([8, 4, 6, 12]))
