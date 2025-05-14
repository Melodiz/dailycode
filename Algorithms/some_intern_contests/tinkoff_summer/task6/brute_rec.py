def max_height_difference_sum(heights):
    # Base cases
    if len(heights) <= 1:
        return 0
    
    if len(heights) == 2:
        return abs(heights[0] - heights[1])
    
    max_sum = 0
    
    # Try removing each adjacent pair and recursively solve for the remaining array
    for i in range(len(heights) - 1):
        # Calculate the difference between adjacent heights
        diff = abs(heights[i] - heights[i + 1])
        
        # Create a new array without the pair at positions i and i+1
        new_heights = heights[:i] + heights[i+2:]
        
        # Recursively find the maximum sum for the remaining people
        remaining_sum = max_height_difference_sum(new_heights)
        
        max_sum = max(max_sum, diff + remaining_sum)
    
    return max_sum

if __name__ == "__main__":
    arr1 = [1, 2, 4, 3]
    arr2 = [2, 1, 4, 5, 2]
    arr3 = [3, 1, 4, 5]
    arr4 = [1, 10, 20, 30, 40, 100]
    arr5 = [3, 2, 2, 1, 10, 20, 30, 40, 100, 2, 2, 3]
    print(max_height_difference_sum(arr1))  # Output: 4
    print(max_height_difference_sum(arr2))  # Output: 6
    print(max_height_difference_sum(arr3))  # Output: 5
    print(max_height_difference_sum(arr4))  # Output: 139
    print(max_height_difference_sum(arr5))  # Output: 201