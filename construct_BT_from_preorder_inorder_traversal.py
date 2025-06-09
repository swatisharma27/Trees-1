'''
PREORDER >>> Root at the first index
Recursion should be first left and then right

Preorder ---> Root, Left, Right
So, we get the root from the first index of the list, then do LEFT traversal, and then RIGHT traversal
-------------------
ROOT > LEFT > RIGHT
-------------------
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

## Brute Sources
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]):
        '''
        TC: O(n^2); O(n)-for searching & O(n)-for recursion so O(n)* O(n) = O(n^2)
        AS: O(n^2)
        '''
    
        ## base condition
        if not preorder or not inorder:
            return None 
        
        ## logic
        rootVal = preorder[0]
        root = TreeNode(rootVal) # Create the root node
        rootIdx = -1

        # Get the index of the root >>>> O(n)
        for idx, element in enumerate(inorder):  
            if element == rootVal:
                rootIdx = idx 
                break

        # get the left array from inorder
        inorderLeft = inorder[:rootIdx]
        # get the right array from inorder
        inorderRight = inorder[rootIdx+1:]

        # get the left array from preorder
        preorderLeft = preorder[1: len(inorderLeft)+1]
        # get the right array from preorder
        preorderRight = preorder[len(inorderLeft)+1:]

        root.left = self.buildTree(preorderLeft, inorderLeft)
        root.right = self.buildTree(preorderRight, inorderRight)

        return root
    


## Using hashmap to search; and using two pointers to do recursion 
class Solution2:
    def buildTree(self, preorder: list[int], inorder: list[int]):
        '''
        TC: O(n); O(1)-for searching & O(n)-for recursion
        AS: O(n)
        '''
        ## hashMap of the Inorder List to improve search from O(n) to O(1) 
        inorder_map = {} # {element : index}
        for idx, element in enumerate(inorder):
            inorder_map[element] = idx

        ## root index from Preorder List
        preorder_idx = 0

        ## start, end index from inorder list 
        def helper(preorder, inorder_map, start, end):

            ## updates preorder_idx each recursive calls 
            nonlocal preorder_idx

            ## base condition
            if start > end:
                return None 

            ## logic
            rootVal = preorder[preorder_idx]
            root = TreeNode(rootVal) # Create the root node
            preorder_idx += 1

            # Get the index of the root >>>> O(1)
            rootIdx = inorder_map[rootVal]

            # helper(preorder, inorder_map, start, end) >>> start and end here are from the inorder list
            # Recursion with two pointers >> O(n)
            root.left = helper(preorder, inorder_map, start, rootIdx-1)
            root.right = helper(preorder, inorder_map, rootIdx+1, end)

            return root


        return helper(preorder, inorder_map, 0, len(inorder)-1)



if __name__ == "__main__":

    preorder = [4, 9, 5, 1, 0]
    inorder = [5, 9, 1, 4, 0]

    s = Solution2()
    root = s.buildTree(preorder, inorder)


    def print_inorder(root):
        if root:
            print_inorder(root.left)
            print(root.val, end=' ')
            print_inorder(root.right)

    print_inorder(root)