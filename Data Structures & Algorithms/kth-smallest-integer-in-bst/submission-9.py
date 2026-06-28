class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        vals = []

        def inorder(node):
            if not node:
                return

            inorder(node.left)
            vals.append(node.val)
            inorder(node.right)

        inorder(root)
        return vals[k - 1]