class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
TC: O(n)
AS: O(h)
'''

'''BOOLEAN-based CONDITIONAL Recursive Soultion'''
class Solution:
    def isValidBST(self, root):
        prev = None

        def inorder_dfs_helper(root):
            nonlocal prev

            # base condition
            if root is None:
                return True

            # logic
            left = inorder_dfs_helper(root.left)
            if not left:
                return False
            print(f"UP{root.val}")

            # breach check
            if (prev != None and prev.val >= root.val):
                return False

            prev = root

            right = inorder_dfs_helper(root.right)
            if not right:
                return False
            print(f"DOWN{root.val}")
            
            return True

        return inorder_dfs_helper(root)
    
    
if __name__ == "__main__":
    # root = [10, 5, 15, 2, 8, 13, 18, 1, 3, 6, 9, None, 14, None, 20]

    # Manually build the tree nodes and link them
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)

    root.left.left = TreeNode(2)
    root.left.right = TreeNode(8)

    root.right.left = TreeNode(13)
    root.right.right = TreeNode(18)

    root.left.left.left = TreeNode(1)
    root.left.left.right = TreeNode(3)

    root.left.right.left = TreeNode(6)
    root.left.right.right = TreeNode(9)

    root.right.left.right = TreeNode(14)
    root.right.right.right = TreeNode(20)


    # ## Conditional
    s2 = Solution()
    print(s2.isValidBST(root))
