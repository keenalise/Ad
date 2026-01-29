class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def min_service_centers(root):
    # State 0: Node is NOT covered
    # State 1: Node HAS a service center
    # State 2: Node IS covered by someone else
    
    count = 0
    
    def dfs(node):
        nonlocal count
        if not node:
            return 2  # Consider null nodes as covered
        
        left = dfs(node.left)
        right = dfs(node.right)
        
        # If any child is NOT covered, this node MUST have a service center
        if left == 0 or right == 0:
            count += 1
            return 1
        
        # If any child has a center, this node is now covered
        if left == 1 or right == 1:
            return 2
        
        # Otherwise, the node is not covered (it's a leaf or its children are covered but don't have centers)
        return 0

    # If the root itself is not covered after DFS, add one final center
    if dfs(root) == 0:
        count += 1
        
    return count

# Helper function to build the tree from the brief's example format
def build_tree():
    # Representing the tree structure: tree = {0,0, null, 0, null, 0, null, null, 0}
    # This specific structure results in a chain-like or sparse binary tree.
    root = TreeNode(0)
    root.left = TreeNode(0)
    root.left.left = TreeNode(0)
    root.left.left.left = TreeNode(0)
    root.left.left.left.right = TreeNode(0)
    return root

def main():
    root = build_tree()
    result = min_service_centers(root)
    print(f"Minimum Service Centers Required: {result}") # Expected Output: 2

if __name__ == "__main__":
    main()