# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    '''
    TC: O(n), where n = number of nodes of the tree
    As: O(h), where h = height of the tree
    '''
    def inorderTraversal(self, root) -> list[int]:
        inorder = []
        postorder = []

        def dfs_helper(root):
            ## base condition
            if root is None:
                return

            ## logic
            dfs_helper(root.left)
            # st.pop()
            print(f"Up {root.val}") ## All Up values will be inorder (root-left-right)
            inorder.append(root.val)


            dfs_helper(root.right)
            # st.pop()
            print(f"Down {root.val}") ## All down values will be inorder (root-left-right)
            postorder.append(root.val)


        dfs_helper(root)
        return inorder
    

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

    s = Solution()
    print(s.inorderTraversal(root))
