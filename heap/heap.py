import heapq

def minheap_sort(nums):
    heap = []
    for n in nums:
        heapq.heappush(heap, n)
    
    res = [heapq.heappop(heap) for i in range(len(heap))]
    return res


def maxheap_sort(nums):
    heap = []
    for n in nums:
        heapq.heappush(heap, -n)
    
    res = [-heapq.heappop(heap) for i in range(len(heap))]
    return res




def main():
    l = [1, -10, 17, 3, 6, 5, -31]
    min_sorted = minheap_sort(l)
    max_sorted = maxheap_sort(l)
    print(f"l = {l}")
    print(f"min_sorted = {min_sorted}")
    print(f"max_sorted = {max_sorted}")
    
    assert(min_sorted == sorted(l))
    assert(max_sorted == sorted(l, reverse=True))
    print("All Tests Passed !")

if __name__ == "__main__":
    main()