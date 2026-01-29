def max_points(tile_multipliers):
    # Add 1 to both ends to handle out-of-bounds cases (Rules in )
    nums = [1] + tile_multipliers + [1]
    n = len(nums)
    
    # Initialize DP table 
    dp = [[0] * n for _ in range(n)]
    
    # Order of computation: length of the sub-array 
    for length in range(1, n - 1):  # length of the range of tiles being shattered
        for i in range(1, n - length):
            j = i + length - 1
            # Try every tile 'k' as the LAST one to be shattered in range [i, j]
            for k in range(i, j + 1):
                # Points from tile k = (multiplier to the left of range) * k * (multiplier to the right)
                points = nums[i-1] * nums[k] * nums[j+1]
                
                # Total = points from k + max points from sub-ranges left and right of k
                total = points + dp[i][k-1] + dp[k+1][j]
                
                dp[i][j] = max(dp[i][j], total)
                
    return dp[1][n-2]

def main():
    # Example 1 [cite: 98]
    tiles1 = [3, 1, 5, 8]
    print(f"Example 1 Output: {max_points(tiles1)}") 
    
    # Example 2 [cite: 109]
    tiles2 = [1, 5]
    print(f"Example 2 Output: {max_points(tiles2)}") 

if __name__ == "__main__":
    main()