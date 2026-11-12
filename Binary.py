from collections import deque


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def build_tree():
    #        S
    #       / \
    #      I   L
    #     / \
    #    V   A
    return Node("S", Node("I", Node("V"), Node("A")), Node("L"))


def bfs_tree(root):
    result = []
    if root is None:
        return result
    q = deque([root])
    while q:
        node = q.popleft()
        result.append(node.data)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    return result


def dfs_tree(node, result=None):

    if result is None:
        result = []
    if node is None:
        return result
    result.append(node.data)
    dfs_tree(node.left, result)
    dfs_tree(node.right, result)
    return result


if __name__ == "__main__":
    root = build_tree()
    print("Binary Tree BFS:", " - ".join(bfs_tree(root)))
    print("Binary Tree DFS:", " - ".join(dfs_tree(root)))