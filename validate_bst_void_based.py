# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
TC: O(n)
AS: O(h)

'''

'''Recursion'''
class Solution1(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        rtype = True
        prev = None

        def inorder_dfs_helper(root):

            nonlocal rtype, prev

            # base condition
            if root is None:
                return 

            # logic
            inorder_dfs_helper(root.left, prev)
            # print(f"Up{root.val}")
            # breeach
            if (prev is not None and prev.val >= root.val):
                rtype = False
        
            prev = root
            inorder_dfs_helper(root.right, prev)
            # print(f"Down{root.val}")

        inorder_dfs_helper(root)
        return rtype

'''Conditional Based Recursion - WAY I'''
class Solution2(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        prev = None
        flag = True

        def inorder_dfs_helper(root):

            nonlocal prev, flag

            # base condition
            if root is None or not flag:  ## "not flag" - to not to add more nodes in the stack after the breech
                return 

            # logic
            inorder_dfs_helper(root.left)
            # print(f"Up{root.val}")
            # breeach
            if (prev is not None and prev.val >= root.val):
                flag = False
        
            prev = root
            inorder_dfs_helper(root.right)
            # print(f"Down{root.val}")

        inorder_dfs_helper(root)
        return flag


'''Conditional Based Recursion - WAY II'''
class Solution3(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        prev = None
        flag = True

        def inorder_dfs_helper(root):

            nonlocal prev, flag

            # base condition
            if root is None: 
                return 

            # logic
            inorder_dfs_helper(root.left)
            # print(f"Up{root.val}")
            # breeach
            if (prev is not None and prev.val >= root.val):
                flag = False
        
            prev = root

            ## "Check if flag is True" - then only add more nodes in the stack after the breech
            if flag:
                inorder_dfs_helper(root.right)
                # print(f"Down{root.val}")

        inorder_dfs_helper(root)
        return flag


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

    # Conditional
    s1 = Solution1()
    print(s1.isValidBST(root))

    ## Non-conditional
    s2 = Solution2()
    print(s2.isValidBST(root))

    ## Non-conditional
    s3 = Solution3()
    print(s3.isValidBST(root))