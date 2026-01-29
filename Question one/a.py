import numpy as np
import random
import math

# 1(a) SENSOR PLACEMENT LOGIC 
def get_geometric_median(locations, threshold=1e-7):
    """Calculates the optimal hub position to minimize Euclidean distances[cite: 41, 42]."""
    points = np.array(locations)
    # Start at the centroid as the initial guess
    hub = np.mean(points, axis=0)
    
    while True:
        num = 0
        den = 0
        for p in points:
            dist = np.linalg.norm(p - hub)
            if dist == 0: continue
            num += p / dist
            den += 1 / dist
        
        new_hub = num / den
        if np.linalg.norm(new_hub - hub) < threshold:
            break
        hub = new_hub
        
    total_dist = sum(np.linalg.norm(p - hub) for p in points)
    return hub, total_dist


#  MAIN EXECUTION BLOCK 
def main():
    print("Question 1(a): Sensor Placement ")
    # Example 1 from brief [cite: 48]
    ex1_sensors = [[0,1], [1,0], [1,2], [2,1]]
    hub, min_dist = get_geometric_median(ex1_sensors)
    print(f"Optimal Hub: {hub}")
    print(f"Minimum Distance Sum: {min_dist:.5f}\n") # Output should be 4.00000

   

if __name__ == "__main__":
    main()