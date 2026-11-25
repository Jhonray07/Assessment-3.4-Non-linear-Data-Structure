
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


def preorder(node, result=None):

    if result is None:
        result = []
    if node is None:
        return result
    result.append(node.data)
    preorder(node.left, result)
    preorder(node.right, result)
    return result


def inorder(node, result=None):

    if result is None:
        result = []
    if node is None:
        return result
    inorder(node.left, result)
    result.append(node.data)
    inorder(node.right, result)
    return result


def postorder(node, result=None):

    if result is None:
        result = []
    if node is None:
        return result
    postorder(node.left, result)
    postorder(node.right, result)
    result.append(node.data)
    return result


if __name__ == "__main__":
    root = build_tree()
    print("DFS Pre-order :", " - ".join(preorder(root)))
    print("DFS In-order  :", " - ".join(inorder(root)))
    print("DFS Post-order:", " - ".join(postorder(root)))