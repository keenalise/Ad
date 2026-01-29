import numpy as np
import random
import math



# 1(b) SIMULATED ANNEALING LOGIC 
def calculate_tour_distance(tour, cities):
    """Objective Function: Total Euclidean distance of the tour[cite: 76]."""
    d = 0
    for i in range(len(tour)):
        c1, c2 = cities[tour[i]], cities[tour[(i + 1) % len(tour)]]
        d += math.sqrt((c1[0]-c2[0])**2 + (c1[1]-c2[1])**2)
    return d

def simulated_annealing(cities, schedule='exponential'):
    """Finds a near-optimal TSP solution using specified cooling[cite: 74, 79]."""
    n = len(cities)
    current_tour = list(range(n))
    random.shuffle(current_tour)
    current_dist = calculate_tour_distance(current_tour, cities)
    
    temp = 1000.0
    alpha = 0.995 # For exponential
    beta = 0.5    # For linear
    
    while temp > 0.01:
        # Neighborhood: 2-opt (Reverse a segment) [cite: 78]
        new_tour = current_tour[:]
        i, j = sorted(random.sample(range(n), 2))
        new_tour[i:j] = reversed(new_tour[i:j])
        
        new_dist = calculate_tour_distance(new_tour, cities)
        
        # Acceptance Criteria
        if new_dist < current_dist or random.random() < math.exp((current_dist - new_dist) / temp):
            current_tour, current_dist = new_tour, new_dist
            
        # Cooling Schedule Selection 
        if schedule == 'exponential':
            temp *= alpha
        else:
            temp -= beta
            
    return current_dist
#  MAIN EXECUTION BLOCK 
def main():
    

    print(" Question 1(b): TSP Simulated Annealing ")
    # Generate random TSP instance (N=20 to 50) [cite: 72]
    num_cities = 30
    cities = [[random.randint(0, 1000), random.randint(0, 1000)] for _ in range(num_cities)]
    
    # Compare Schedules 
    for mode in ['exponential', 'linear']:
        best_d = simulated_annealing(cities, schedule=mode)
        print(f"Results using {mode} cooling: {best_d:.2f}")

if __name__ == "__main__":
    main()