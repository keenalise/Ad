import heapq

# Graph based on Diagram (a) - Actual Road Distances
graph = {
    'Glogow': [('Poznań', 90), ('Leszno', 45), ('Wrocław', 140)],
    'Poznań': [('Glogow', 90), ('Bydgoszcz', 140), ('Konin', 120)],
    'Leszno': [('Glogow', 45), ('Poznań', 140), ('Kalisz', 100)],
    'Bydgoszcz': [('Poznań', 140), ('Włocławek', 110)],
    'Włocławek': [('Bydgoszcz', 110), ('Konin', 120), ('Plock', 55)],
    'Konin': [('Poznań', 120), ('Włocławek', 120), ('Łódź', 120)],
    'Plock': [('Włocławek', 55), ('Warsaw', 130)],
    'Wrocław': [('Glogow', 140), ('Opole', 100)],
    'Kalisz': [('Leszno', 100), ('Łódź', 160)],
    'Łódź': [('Konin', 120), ('Kalisz', 160), ('Warsaw', 150), ('Radom', 165), ('Katowice', 128)],
    'Warsaw': [('Plock', 130), ('Łódź', 150), ('Radom', 105)],
    'Opole': [('Wrocław', 100), ('Częstochowa', 118), ('Katowice', 80)],
    'Częstochowa': [('Opole', 118), ('Katowice', 80)],
    'Katowice': [('Opole', 80), ('Częstochowa', 80), ('Łódź', 128), ('Kraków', 85)],
    'Radom': [('Warsaw', 105), ('Łódź', 165), ('Kielce', 82)],
    'Kielce': [('Radom', 82), ('Kraków', 120)],
    'Kraków': [('Katowice', 85), ('Kielce', 120)]
}

# Heuristic based on Diagram (b) - Straight Line Distances to Plock
heuristic = {
    'Glogow': 200, 'Poznań': 150, 'Bydgoszcz': 90, 'Włocławek': 44,
    'Plock': 0, 'Konin': 96, 'Leszno': 160, 'Kalisz': 130,
    'Łódź': 95, 'Warsaw': 95, 'Radom': 140, 'Kielce': 180,
    'Kraków': 220, 'Katowice': 200, 'Częstochowa': 190, 'Wrocław': 210, 'Opole': 230
}

def search_algo(type='BFS'):
    start, goal = 'Glogow', 'Plock'
    # Container structure: (priority/cost, current_node, path)
    if type == 'DFS':
        stack = [(start, [start])]
    elif type == 'BFS':
        queue = [(start, [start])]
    else: # A*
        pq = [(heuristic[start], 0, start, [start])]
    
    visited = set()

    while True:
        # Implementation of Open/Closed containers logic
        if type == 'DFS':
            if not stack: break
            (node, path) = stack.pop()
        elif type == 'BFS':
            if not queue: break
            (node, path) = queue.pop(0)
        else:
            if not pq: break
            (f, g, node, path) = heapq.heappop(pq)

        if node == goal: return path
        
        if node not in visited:
            visited.add(node)
            for (neighbor, weight) in graph.get(node, []):
                if neighbor not in visited:
                    if type == 'DFS':
                        stack.append((neighbor, path + [neighbor]))
                    elif type == 'BFS':
                        queue.append((neighbor, path + [neighbor]))
                    else: # A*
                        new_g = g + weight
                        new_f = new_g + heuristic[neighbor]
                        heapq.heappush(pq, (new_f, new_g, neighbor, path + [neighbor]))
    return None

def main():
    for mode in ['DFS', 'BFS', 'A*']:
        print(f"{mode} Path: {search_algo(mode)}")

if __name__ == "__main__":
    main()