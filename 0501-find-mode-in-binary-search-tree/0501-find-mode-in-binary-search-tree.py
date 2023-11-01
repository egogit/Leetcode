# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        q, cnt = list(), dict();
        q.append(root)

        while(q):
            node = q.pop(0);
            if node.val not in cnt:
                cnt[node.val] = 0;
            cnt[node.val] += 1;

            if node.left: q.append(node.left)
            if node.right: q.append(node.right)

        maxcnt = max(cnt.values());
        ans = [item for item, c in cnt.items() if c == maxcnt]

        return ans;