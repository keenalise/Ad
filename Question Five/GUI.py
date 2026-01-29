import tkinter as tk
from tkinter import messagebox
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class EmergencySimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Emergency Network Simulator")
        
        # Initialize Graph
        self.G = nx.Graph()
        self.add_sample_data()
        
        # GUI Layout
        self.setup_gui()

    def add_sample_data(self):
        """Pre-load some cities and roads."""
        edges = [
            ('Kathmandu', 'Lalitpur', 5), ('Lalitpur', 'Bhaktapur', 8),
            ('Kathmandu', 'Pokhara', 200), ('Pokhara', 'Chitwan', 150),
            ('Chitwan', 'Lalitpur', 100), ('Bhaktapur', 'Banepa', 12)
        ]
        self.G.add_weighted_edges_from(edges)

    def setup_gui(self):
        # Control Panel
        control_frame = tk.Frame(self.root, padx=10, pady=10)
        control_frame.pack(side=tk.LEFT, fill=tk.Y)

        tk.Label(control_frame, text="Network Controls", font=('Arial', 14, 'bold')).pack()
        
        tk.Button(control_frame, text="Generate MST", command=self.visualize_mst, width=20).pack(pady=5)
        tk.Button(control_frame, text="Find K-Disjoint Paths", command=self.find_k_paths, width=20).pack(pady=5)
        tk.Button(control_frame, text="Simulate Node Failure", command=self.fail_node, width=20).pack(pady=5)
        tk.Button(control_frame, text="Reset Network", command=self.reset_graph, width=20).pack(pady=5)

        # Plotting Area
        self.fig, self.ax = plt.subplots(figsize=(6, 5))
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        self.draw_graph()

    def draw_graph(self, highlight_edges=None, highlighted_nodes=None):
        self.ax.clear()
        pos = nx.spring_layout(self.G)
        
        # Draw basic graph
        nx.draw(self.G, pos, ax=self.ax, with_labels=True, node_color='skyblue', node_size=1500, font_size=10)
        labels = nx.get_edge_attributes(self.G, 'weight')
        nx.draw_networkx_edge_labels(self.G, pos, edge_labels=labels, ax=self.ax)

        # Highlight MST or Paths if provided
        if highlight_edges:
            nx.draw_networkx_edges(self.G, pos, edgelist=highlight_edges, edge_color='r', width=3, ax=self.ax)
        
        if highlighted_nodes:
            nx.draw_networkx_nodes(self.G, pos, nodelist=highlighted_nodes, node_color='red', ax=self.ax)

        self.canvas.draw()

    def visualize_mst(self):
        """Q1: Dynamic MST Visualization [cite: 234]"""
        mst_edges = list(nx.minimum_spanning_edges(self.G, algorithm='kruskal', data=False))
        self.draw_graph(highlight_edges=mst_edges)
        messagebox.showinfo("MST Logic", "MST computed using Kruskal's Algorithm.\nComplexity: O(E log E)")

    def find_k_paths(self):
        """Q2: Reliable Path Finder [cite: 239]"""
        # Example: Find paths between Kathmandu and Chitwan
        try:
            paths = list(nx.edge_disjoint_paths(self.G, 'Kathmandu', 'Chitwan'))
            messagebox.showinfo("K-Disjoint Paths", f"Found {len(paths)} disjoint paths.")
        except nx.NetworkXNoPath:
            messagebox.showwarning("Error", "No path exists.")

    def fail_node(self):
        """Q4: Failure Simulation [cite: 249]"""
        if 'Pokhara' in self.G:
            self.G.remove_node('Pokhara')
            self.draw_graph()
            messagebox.showinfo("Failure", "Node 'Pokhara' has failed. Rerouting required.")

    def reset_graph(self):
        self.G.clear()
        self.add_sample_data()
        self.draw_graph()

if __name__ == "__main__":
    root = tk.Tk()
    app = EmergencySimulator(root)
    root.mainloop()