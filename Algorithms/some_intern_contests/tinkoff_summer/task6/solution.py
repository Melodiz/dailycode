import heapq

def find_max_difference(arr):
    if not arr:
        return 0
    left_heap = []
    right_heap = []
    left_sum = 0
    right_sum = 0
    arr_sorted = sorted(arr)
    n = len(arr_sorted)
    left_sum = sum(arr_sorted[:n//2])
    right_sum = sum(arr_sorted[n//2:])
    return abs(right_sum - left_sum)

def smart(arr):
    n = len(arr)
    if n % 2 == 0:
        return find_max_difference(arr)
    
    left_diffs = [0] * n
    right_diffs = [0] * n
    left_heap = []
    right_heap = []
    left_sum = 0
    right_sum = 0
    
    for i in range(0, n-1, 2):
        num = arr[i]
        if not left_heap or num <= -left_heap[0]:
            heapq.heappush(left_heap, -num)
            left_sum += num
        else:
            heapq.heappush(right_heap, num)
            right_sum += num
        
        while len(left_heap) > len(right_heap) + 1:
            val = -heapq.heappop(left_heap)
            left_sum -= val
            heapq.heappush(right_heap, val)
            right_sum += val
        while len(right_heap) > len(left_heap):
            val = heapq.heappop(right_heap)
            right_sum -= val
            heapq.heappush(left_heap, -val)
            left_sum += val
        
        if i+1 < n:
            num = arr[i+1]
            if num <= -left_heap[0]:
                heapq.heappush(left_heap, -num)
                left_sum += num
            else:
                heapq.heappush(right_heap, num)
                right_sum += num
            
            while len(left_heap) > len(right_heap) + 1:
                val = -heapq.heappop(left_heap)
                left_sum -= val
                heapq.heappush(right_heap, val)
                right_sum += val
            while len(right_heap) > len(left_heap):
                val = heapq.heappop(right_heap)
                right_sum -= val
                heapq.heappush(left_heap, -val)
                left_sum += val
        
        left_diffs[i+1] = abs(right_sum - left_sum)
    
    left_heap = []
    right_heap = []
    left_sum = 0
    right_sum = 0
    
    for i in range(n-1, 0, -2):
        num = arr[i]
        if not left_heap or num <= -left_heap[0]:
            heapq.heappush(left_heap, -num)
            left_sum += num
        else:
            heapq.heappush(right_heap, num)
            right_sum += num
        
        while len(left_heap) > len(right_heap) + 1:
            val = -heapq.heappop(left_heap)
            left_sum -= val
            heapq.heappush(right_heap, val)
            right_sum += val
        while len(right_heap) > len(left_heap):
            val = heapq.heappop(right_heap)
            right_sum -= val
            heapq.heappush(left_heap, -val)
            left_sum += val
        
        if i-1 >= 0:
            num = arr[i-1]
            if num <= -left_heap[0]:
                heapq.heappush(left_heap, -num)
                left_sum += num
            else:
                heapq.heappush(right_heap, num)
                right_sum += num
            
            while len(left_heap) > len(right_heap) + 1:
                val = -heapq.heappop(left_heap)
                left_sum -= val
                heapq.heappush(right_heap, val)
                right_sum += val
            while len(right_heap) > len(left_heap):
                val = heapq.heappop(right_heap)
                right_sum -= val
                heapq.heappush(left_heap, -val)
                left_sum += val
        
        right_diffs[i-1] = abs(right_sum - left_sum)
    
    max_diff = 0
    for i in range(0, n, 2):
        current_diff = 0
        if i > 0:
            current_diff += left_diffs[i-1]
        if i < n-1:
            current_diff += right_diffs[i+1]
        max_diff = max(max_diff, current_diff)
    
    return max_diff

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    print(smart(arr))

if __name__ == "__main__":
    main()