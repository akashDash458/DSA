class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def levelOrder(root) :
    if not root:
        return []

    res = []
    q = [root]
    while q:
        n = len(q)
        level = []
        while n:
            n -= 1
            root = q.pop(0)
            level.append(root.val)
            if root.left:
                q.append(root.left)
            if root.right:
                q.append(root.right)
        
        res.append(level)
    
    return res


def main():
    r3 = TreeNode(20, TreeNode(15), TreeNode(7))
    r4 = TreeNode(9)
    root = TreeNode(3, r4, r3)
    
    res = levelOrder(root)
    for inner_list in res:
        print(', '.join(map(str, inner_list)))

    
if __name__ == "__main__":
    main()
            
            