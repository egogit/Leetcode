# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1. 후위 순위  => 적합하다고 판단.
# 2. array에 binary trees의 원소를 옮겨서 처리하기 
# => skewed tree인 경우 2^0+2^1+2^2+.. +2^1000의 크기를 생각해야하기에 비현실적.

class Solution:
    ans = 0;
    
    def printPostOrder(self, node):
            if node:
                lsum, lcnt = self.printPostOrder(node.left) if node.left else [0,0]
                rsum, rcnt = self.printPostOrder(node.right) if node.right else [0,0]

                if (lsum + rsum + node.val)//(lcnt+rcnt+1) == node.val:
                    self.ans += 1;
                
                return [lsum + rsum + node.val, lcnt + rcnt + 1];
            else:
                return [0,0]

    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:

        self.printPostOrder(root);

        return self.ans;