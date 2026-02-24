class Solution:
    def sumRootToLeaf(self, root):
        
        def dfs(node, current):
            if not node:
                return 0
            
            # binary number update
            current = current * 2 + node.val
            
            # if leaf node
            if not node.left and not node.right:
                return current
            
            # left + right subtree
            return dfs(node.left, current) + dfs(node.right, current)
        
        return dfs(root, 0)