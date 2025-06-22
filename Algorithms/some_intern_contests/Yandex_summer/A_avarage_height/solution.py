
from collections import deque

def main():
    n = int(input())
    queue = deque()
    height_counts = {}
    
    total_sum = 0

    for _ in range(n):
        line = input().strip()
        
        if line.startswith('+'):
            _, k_str = line.split()
            k = int(k_str)
            
            queue.append(k)
            total_sum += k
            height_counts[k] = height_counts.get(k, 0) + 1

        elif line == '-':
            if queue:
                removed_height = queue.popleft()
                
                total_sum -= removed_height
                height_counts[removed_height] -= 1
                if height_counts[removed_height] == 0:
                    del height_counts[removed_height]

        num_people = len(queue)
        
        if num_people == 0:
            print(0)
            continue
            
        if total_sum % num_people == 0:
            average_height = total_sum // num_people
            print(height_counts.get(average_height, 0))
        else:
            print(0)
if __name__ == "__main__":
    main()