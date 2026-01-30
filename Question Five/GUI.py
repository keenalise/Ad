import tkinter as tk
from tkinter import messagebox
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class EmergencySimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("🚨 Emergency Network Simulator 🚨")
        self.root.configure(bg="#f0f4f8")
        self.G = nx.Graph()
        self.add_sample_data()
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
        # Header
        header = tk.Label(self.root, text="Emergency Network Simulator", font=("Segoe UI", 20, "bold"), fg="#1a237e", bg="#f0f4f8", pady=20)
        header.pack(side=tk.TOP, fill=tk.X)

        # Control Panel
        control_frame = tk.Frame(self.root, padx=18, pady=18, bg="#e3eafc", bd=2, relief=tk.RIDGE)
        control_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

        tk.Label(control_frame, text="Network Controls", font=("Segoe UI", 14, "bold"), fg="#3949ab", bg="#e3eafc").pack(pady=(0,10))

        # Button style
        btn_style = {"font": ("Segoe UI", 12), "bg": "#bbdefb", "fg": "#1a237e", "activebackground": "#90caf9", "activeforeground": "#0d133d", "bd": 2, "relief": tk.RAISED}

        # Tooltips helper
        def add_tooltip(widget, text):
            def on_enter(e):
                widget.tooltip = tk.Toplevel(widget)
                widget.tooltip.wm_overrideredirect(True)
                x = widget.winfo_rootx() + 60
                y = widget.winfo_rooty() + 20
                widget.tooltip.wm_geometry(f"+{x}+{y}")
                label = tk.Label(widget.tooltip, text=text, bg="#3949ab", fg="white", font=("Segoe UI", 10), padx=8, pady=4)
                label.pack()
            def on_leave(e):
                if hasattr(widget, 'tooltip'):
                    widget.tooltip.destroy()
            widget.bind("<Enter>", on_enter)
            widget.bind("<Leave>", on_leave)

        btn_mst = tk.Button(control_frame, text="Generate MST", command=self.visualize_mst, width=20, **btn_style)
        btn_mst.pack(pady=6)
        add_tooltip(btn_mst, "Show Minimum Spanning Tree")

        btn_kpaths = tk.Button(control_frame, text="Find K-Disjoint Paths", command=self.find_k_paths, width=20, **btn_style)
        btn_kpaths.pack(pady=6)
        add_tooltip(btn_kpaths, "Find multiple reliable paths")

        btn_fail = tk.Button(control_frame, text="Simulate Node Failure", command=self.fail_node, width=20, **btn_style)
        btn_fail.pack(pady=6)
        add_tooltip(btn_fail, "Remove a node to simulate failure")

        btn_reset = tk.Button(control_frame, text="Reset Network", command=self.reset_graph, width=20, **btn_style)
        btn_reset.pack(pady=6)
        add_tooltip(btn_reset, "Restore original network")

        # Plotting Area
        plot_frame = tk.Frame(self.root, bg="#f0f4f8", bd=2, relief=tk.FLAT)
        plot_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.fig, self.ax = plt.subplots(figsize=(6, 5))
        self.fig.patch.set_facecolor('#e3eafc')
        self.canvas = FigureCanvasTkAgg(self.fig, master=plot_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        self.draw_graph()

    def draw_graph(self, highlight_edges=None, highlighted_nodes=None):
        self.ax.clear()
        pos = nx.spring_layout(self.G, seed=42)
        # Draw basic graph
        nx.draw(
            self.G, pos, ax=self.ax, with_labels=True,
            node_color="#90caf9", node_size=1800, font_size=12,
            font_weight="bold", edge_color="#3949ab", width=2
        )
        labels = nx.get_edge_attributes(self.G, 'weight')
        nx.draw_networkx_edge_labels(self.G, pos, edge_labels=labels, ax=self.ax, font_color="#1a237e", font_size=11)
        # Highlight MST or Paths if provided
        if highlight_edges:
            nx.draw_networkx_edges(self.G, pos, edgelist=highlight_edges, edge_color="#e53935", width=4, ax=self.ax)
        if highlighted_nodes:
            nx.draw_networkx_nodes(self.G, pos, nodelist=highlighted_nodes, node_color="#e53935", ax=self.ax)
        self.ax.set_facecolor('#e3eafc')
        self.ax.set_title("City Network Graph", fontsize=16, color="#1a237e", pad=16)
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