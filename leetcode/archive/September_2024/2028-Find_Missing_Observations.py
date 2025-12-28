class Solution:
    def missingRolls(self, rolls, mean: int, n: int):
        
        # Calculate the total sum needed for the missing rolls
        total_sum_needed = mean * (len(rolls) + n) - sum(rolls)
        
        # If the total sum needed is not possible to achieve with the given number of rolls
        if total_sum_needed < n or total_sum_needed > 6 * n:
            return []
        
        # Initialize the result array with the average value
        result = [total_sum_needed // n] * n
        remainder = total_sum_needed % n
        
        # Distribute the remainder to make the sum correct
        for i in range(remainder):
            result[i] += 1
        
        return result