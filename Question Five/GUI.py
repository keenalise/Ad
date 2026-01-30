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
        header = tk.Label(self.root, text="Emergency Network Simulator", font=("Segoe UI", 22, "bold"), fg="#283593", bg="#f0f4f8", pady=18)
        header.pack(side=tk.TOP, fill=tk.X)

        # Info Bar
        self.status_var = tk.StringVar(value="Welcome! Ready to simulate.")
        status_bar = tk.Label(self.root, textvariable=self.status_var, font=("Segoe UI", 11), bg="#e8eaf6", fg="#283593", anchor="w", padx=12, pady=6, relief=tk.FLAT)
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)

        # Control Panel
        control_frame = tk.Frame(self.root, padx=20, pady=20, bg="#e3eafc", bd=2, relief=tk.RIDGE)
        control_frame.pack(side=tk.LEFT, fill=tk.Y, padx=16, pady=16)

        tk.Label(control_frame, text="Network Controls", font=("Segoe UI", 15, "bold"), fg="#283593", bg="#e3eafc").pack(pady=(0,14))

        # Button style
        btn_style = {"font": ("Segoe UI", 13), "bg": "#fff", "fg": "#283593", "activebackground": "#c5cae9", "activeforeground": "#1a237e", "bd": 0, "relief": tk.FLAT, "highlightthickness": 0}

        # Tooltips helper
        def add_tooltip(widget, text):
            def on_enter(e):
                widget.tooltip = tk.Toplevel(widget)
                widget.tooltip.wm_overrideredirect(True)
                x = widget.winfo_rootx() + 60
                y = widget.winfo_rooty() + 20
                widget.tooltip.wm_geometry(f"+{x}+{y}")
                label = tk.Label(widget.tooltip, text=text, bg="#283593", fg="white", font=("Segoe UI", 10), padx=8, pady=4)
                label.pack()
            def on_leave(e):
                if hasattr(widget, 'tooltip'):
                    widget.tooltip.destroy()
            widget.bind("<Enter>", on_enter)
            widget.bind("<Leave>", on_leave)

        # Button icons (Unicode)
        btns = [
            {"text": "🗺️  Generate MST", "cmd": self.visualize_mst, "tip": "Show Minimum Spanning Tree"},
            {"text": "🔗 Find K-Disjoint Paths", "cmd": self.find_k_paths, "tip": "Find multiple reliable paths"},
            {"text": "⚠️  Simulate Node Failure", "cmd": self.fail_node, "tip": "Remove a node to simulate failure"},
            {"text": "🔄 Reset Network", "cmd": self.reset_graph, "tip": "Restore original network"},
        ]
        for btn in btns:
            b = tk.Button(control_frame, text=btn["text"], command=btn["cmd"], width=22, **btn_style)
            b.pack(pady=8, ipadx=2, ipady=6)
            b.configure(cursor="hand2")
            b.bind("<Enter>", lambda e, w=b: w.config(bg="#e8eaf6"))
            b.bind("<Leave>", lambda e, w=b: w.config(bg="#fff"))
            add_tooltip(b, btn["tip"])

        # Plotting Area
        plot_frame = tk.Frame(self.root, bg="#f0f4f8", bd=2, relief=tk.FLAT)
        plot_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=16, pady=16)
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
            node_color="#fffde7", node_size=1900, font_size=13,
            font_weight="bold", edge_color="#283593", width=2,
            linewidths=2
        )
        labels = nx.get_edge_attributes(self.G, 'weight')
        nx.draw_networkx_edge_labels(self.G, pos, edge_labels=labels, ax=self.ax, font_color="#283593", font_size=12)
        # Highlight MST or Paths if provided
        if highlight_edges:
            nx.draw_networkx_edges(self.G, pos, edgelist=highlight_edges, edge_color="#e53935", width=5, ax=self.ax)
        if highlighted_nodes:
            nx.draw_networkx_nodes(self.G, pos, nodelist=highlighted_nodes, node_color="#e53935", ax=self.ax)
        self.ax.set_facecolor('#e3eafc')
        self.ax.set_title("City Network Graph", fontsize=17, color="#283593", pad=18)
        self.ax.axis('off')
        self.canvas.draw()

    def visualize_mst(self):
        """Q1: Dynamic MST Visualization [cite: 234]"""
        mst_edges = list(nx.minimum_spanning_edges(self.G, algorithm='kruskal', data=False))
        self.draw_graph(highlight_edges=mst_edges)
        self.status_var.set("MST computed using Kruskal's Algorithm. Complexity: O(E log E)")
        messagebox.showinfo("MST Logic", "MST computed using Kruskal's Algorithm.\nComplexity: O(E log E)")

    def find_k_paths(self):
        """Q2: Reliable Path Finder [cite: 239]"""
        try:
            paths = list(nx.edge_disjoint_paths(self.G, 'Kathmandu', 'Chitwan'))
            self.status_var.set(f"Found {len(paths)} disjoint paths between Kathmandu and Chitwan.")
            messagebox.showinfo("K-Disjoint Paths", f"Found {len(paths)} disjoint paths.")
        except nx.NetworkXNoPath:
            self.status_var.set("No path exists between Kathmandu and Chitwan.")
            messagebox.showwarning("Error", "No path exists.")

    def fail_node(self):
        """Q4: Failure Simulation [cite: 249]"""
        if 'Pokhara' in self.G:
            self.G.remove_node('Pokhara')
            self.draw_graph()
            self.status_var.set("Node 'Pokhara' has failed. Rerouting required.")
            messagebox.showinfo("Failure", "Node 'Pokhara' has failed. Rerouting required.")
        else:
            self.status_var.set("Node 'Pokhara' is already removed.")

    def reset_graph(self):
        self.G.clear()
        self.add_sample_data()
        self.draw_graph()
        self.status_var.set("Network reset to original state.")

if __name__ == "__main__":
    root = tk.Tk()
    app = EmergencySimulator(root)
    root.mainloop()