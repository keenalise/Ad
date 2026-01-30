# Advanced Algorithms Project

A comprehensive collection of algorithm implementations solving real-world optimization and computational problems using Python.

## 📁 Project Structure

```
Advance Algorithm/
│
├── Question One/
│   ├── a.py                    # Sensor Placement using Geometric Median
│   └── b.py                    # TSP Simulated Annealing
│
├── Question Two/
│   └── trategictileshatter.py  # Strategic Tile Shatter (Dynamic Programming)
│
├── Question Three/
│   └── ServiceCenter.py        # Minimum Service Centers (Tree Algorithm)
│
├── Question Four/
│   └── SmartGrid.py            # Energy Distribution Optimization
│
└── Question Five/
    └── GUI.py                  # Emergency Network Simulator (Tkinter GUI)
```

## 🚀 Features

### Question 1: Optimization Algorithms

#### a.py - Sensor Placement Optimization
- **Algorithm**: Geometric Median Calculation
- **Purpose**: Find optimal hub position to minimize total distance to all sensors
- **Method**: Iterative Weiszfeld's algorithm
- **Complexity**: O(n × iterations)
- **Use Case**: IoT sensor network optimization

**Key Functions:**
- `get_geometric_median(locations, threshold)` - Calculates optimal hub location

**Example Usage:**
```bash
python a.py
```

**Sample Output:**
```
Question 1(a): Sensor Placement
Optimal Hub: [1. 1.]
Minimum Distance Sum: 4.00000
```

#### b.py - Traveling Salesman Problem (TSP)
- **Algorithm**: Simulated Annealing
- **Purpose**: Find near-optimal tour visiting all cities
- **Cooling Schedules**: 
  - Exponential: T = T × α (α = 0.995)
  - Linear: T = T - β (β = 0.5)
- **Neighborhood**: 2-opt edge reversal
- **Complexity**: O(n² × iterations)

**Key Functions:**
- `calculate_tour_distance(tour, cities)` - Computes total tour distance
- `simulated_annealing(cities, schedule)` - Finds optimal tour

**Example Usage:**
```bash
python b.py
```

**Sample Output:**
```
Question 1(b): TSP Simulated Annealing
Results using exponential cooling: 7842.34
Results using linear cooling: 8156.72
```

---

### Question 2: Strategic Tile Shatter

#### trategictileshatter.py - Maximum Points Game
- **Algorithm**: Dynamic Programming (Interval DP)
- **Purpose**: Maximize points by strategically shattering tiles
- **Complexity**: O(n³)
- **Problem Type**: Burst Balloons variant

**Rules:**
- Each tile has a multiplier
- Points = left_multiplier × tile_multiplier × right_multiplier
- Choose optimal shattering order

**Key Functions:**
- `max_points(tile_multipliers)` - Computes maximum achievable points

**Example Usage:**
```bash
python trategictileshatter.py
```

**Sample Output:**
```
Example 1 Output: 167
Example 2 Output: 10
```

---

### Question 3: Service Center Placement

#### ServiceCenter.py - Minimum Service Centers in Tree
- **Algorithm**: Tree Dynamic Programming with DFS
- **Purpose**: Minimize service centers needed to cover all nodes
- **Complexity**: O(n)
- **Problem Type**: Dominating Set on Trees

**States:**
- 0: Node is NOT covered
- 1: Node HAS a service center
- 2: Node IS covered by another node

**Key Classes & Functions:**
- `TreeNode` - Binary tree node structure
- `min_service_centers(root)` - Finds minimum centers needed
- `build_tree()` - Constructs sample tree

**Example Usage:**
```bash
python ServiceCenter.py
```

**Sample Output:**
```
Minimum Service Centers Required: 2
```

---

### Question 4: Smart Grid Energy Optimization

#### SmartGrid.py - Energy Distribution System
- **Algorithm**: Greedy Allocation with Time-based Constraints
- **Purpose**: Optimize energy distribution across districts
- **Features**:
  - Multi-source allocation (Solar, Hydro, Diesel)
  - Time-based availability windows
  - Cost optimization
  - Renewable energy tracking

**Key Functions:**
- `optimize_energy_distribution(demand_data, source_data)` - Allocates energy optimally

**Data Models:**
- **Demand Table**: Hourly energy demand per district
- **Source Table**: Energy sources with capacity, availability, and cost

**Example Usage:**
```bash
python SmartGrid.py
```

**Sample Output:**
```
Hour  | Dist       | Solar  | Hydro  | Diesel | Total  | Demand | % Met
---------------------------------------------------------------------------
6     | District A | 20     | 0      | 0      | 20     | 20     | 100.0%
6     | District B | 15     | 0      | 0      | 15     | 15     | 100.0%
...

Total Cost: Rs. 215.5
Renewable Energy Usage: 72.34%
```

---

### Question 5: Emergency Network Simulator

#### GUI.py - Interactive Network Visualization
- **Framework**: Tkinter + NetworkX + Matplotlib
- **Purpose**: Simulate and visualize emergency response networks
- **Algorithms**:
  - Minimum Spanning Tree (Kruskal's Algorithm)
  - K-Disjoint Paths (Redundant routing)
  - Node Failure Simulation

**Features:**
1. **Generate MST** - Visualizes optimal network backbone
2. **Find K-Disjoint Paths** - Identifies redundant routes
3. **Simulate Node Failure** - Tests network resilience
4. **Reset Network** - Restores original topology

**Key Components:**
- `EmergencySimulator` class - Main application
- `add_sample_data()` - Initializes Nepal city network
- `visualize_mst()` - Highlights minimum spanning tree
- `find_k_paths()` - Finds edge-disjoint paths
- `fail_node()` - Simulates node failure
- `draw_graph()` - Renders network visualization

**Example Usage:**
```bash
python GUI.py
```

**GUI Controls:**
- Click "Generate MST" to see optimal connections (red edges)
- Click "Find K-Disjoint Paths" to find redundant routes
- Click "Simulate Node Failure" to remove Pokhara node
- Click "Reset Network" to restore original network

**Network Data:**
- Preloaded cities: Kathmandu, Lalitpur, Bhaktapur, Pokhara, Chitwan, Banepa
- Weighted edges representing distances

---

## 🛠️ Installation & Setup

### Prerequisites
```bash
python 3.8+
```

### Required Libraries
```bash
pip install numpy
pip install networkx
pip install matplotlib
pip install tkinter  # Usually comes with Python
```

### Alternative: Install all at once
```bash
pip install numpy networkx matplotlib
```

---

## 📊 Algorithm Complexity Summary

| Problem | Algorithm | Time Complexity | Space Complexity |
|---------|-----------|-----------------|------------------|
| Sensor Placement | Geometric Median | O(n × k) | O(n) |
| TSP | Simulated Annealing | O(n² × iterations) | O(n) |
| Tile Shatter | Dynamic Programming | O(n³) | O(n²) |
| Service Centers | Tree DP | O(n) | O(h) |
| Smart Grid | Greedy Allocation | O(h × d × s) | O(h × d) |
| Network MST | Kruskal's Algorithm | O(E log E) | O(V + E) |

*where: n = problem size, k = iterations, h = tree height/hours, d = districts, s = sources, V = vertices, E = edges*

---

## 🎯 Key Concepts Demonstrated

1. **Optimization Techniques**
   - Geometric algorithms
   - Metaheuristics (Simulated Annealing)
   - Greedy algorithms

2. **Dynamic Programming**
   - Interval DP
   - Tree DP

3. **Graph Algorithms**
   - Minimum Spanning Tree
   - Path finding
   - Network resilience

4. **Real-World Applications**
   - IoT network design
   - Route optimization
   - Resource allocation
   - Infrastructure planning
   - Energy management

---

## 📖 Usage Examples

### Running Individual Scripts

```bash
# Question 1a: Sensor placement
cd "Question One"
python a.py

# Question 1b: TSP optimization
python b.py

# Question 2: Tile shatter game
cd "../Question Two"
python trategictileshatter.py

# Question 3: Service center optimization
cd "../Question Three"
python ServiceCenter.py

# Question 4: Energy distribution
cd "../Question Four"
python SmartGrid.py

# Question 5: Network simulator GUI
cd "../Question Five"
python GUI.py
```

---

## 🔧 Customization

### Modifying Question 1a - Sensor Locations
Edit `a.py`:
```python
ex1_sensors = [[0,1], [1,0], [1,2], [2,1]]  # Add your coordinates
```

### Modifying Question 1b - City Count
Edit `b.py`:
```python
num_cities = 30  # Change to desired number
```

### Modifying Question 4 - Energy Data
Edit `SmartGrid.py`:
```python
demand_table = [
    {"hour": 6, "District A": 20, "District B": 15, "District C": 25},
    # Add more hourly data
]
```

### Modifying Question 5 - Network Topology
Edit `GUI.py`:
```python
edges = [
    ('City1', 'City2', distance),
    # Add more edges
]
```

---

## 📸 Screenshots

### Emergency Network Simulator (Question 5)
The GUI displays:
- Network graph with cities as nodes
- Weighted edges showing distances
- MST visualization in red
- Control panel with action buttons

---

## 🧪 Testing

All scripts include built-in test cases and can be run directly:

```bash
python <script_name>.py
```

Expected outputs are documented in the code comments.

---

## 🤝 Contributing

This is an academic project. For improvements or bug fixes:
1. Document the issue
2. Propose solution with complexity analysis
3. Test thoroughly

---

## 📝 Notes

- **Question 1a**: Uses Weiszfeld's algorithm for geometric median calculation
- **Question 1b**: Compares exponential vs linear cooling schedules
- **Question 2**: Implements interval DP similar to burst balloons problem
- **Question 3**: Uses tree DP with three states (uncovered, has center, covered)
- **Question 4**: Prioritizes renewable energy sources by cost
- **Question 5**: Interactive visualization requires display environment (X11, Wayland, etc.)

---

## 🐛 Troubleshooting

### GUI doesn't display (Question 5)
- Ensure `tkinter` is installed: `python -m tkinter`
- On Linux: `sudo apt-get install python3-tk`
- On macOS: Tkinter comes with Python
- On Windows: Reinstall Python with Tk/Tcl option

### Import errors
```bash
pip install --upgrade numpy networkx matplotlib
```

### matplotlib backend issues
Add to script:
```python
import matplotlib
matplotlib.use('TkAgg')
```

---

## 📚 References

- Geometric Median: Weiszfeld's Algorithm
- Simulated Annealing: Kirkpatrick et al. (1983)
- Dynamic Programming: Bellman's Principle of Optimality
- Kruskal's Algorithm: MST construction
- Graph Theory: NetworkX documentation

---

## 📄 License

This project is for educational purposes.

---

## 👥 Authors

Created as part of Advanced Algorithms coursework.

---

## 🎓 Learning Objectives

Students will learn:
- How to apply optimization algorithms to real problems
- Dynamic programming techniques
- Graph algorithm implementation
- GUI development with Python
- Algorithm complexity analysis
- Trade-offs between solution quality and computation time

---

**Last Updated**: January 2026