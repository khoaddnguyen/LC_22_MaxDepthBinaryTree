def maxDepth(self, root: Optional[TreeNode]) -> int:

    if not root:
         return 0

    # DFS recursion: [1 + max(dfs(left), dfs(right))]

    # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))



    # BFS - traverse through all levels

    # level = 0
    # q = deque([root])
    # while q:
    #
    #     for i in range(len(q)):
    #         node = q.popleft()
    #         if node.left:
    #             q.append(node.left)
    #         if node.right:
    #             q.append(node.right)
    #     level += 1
    # return level



    # Iterative DFS - DFS without recursion

    stack = [[root, 1]]
    result = 1

    while stack:
        node, depth = stack.pop()

        if node:
            result = max(result, depth)
            stack.append([node.left, depth + 1])
            stack.append([node.right, depth + 1])

    return result