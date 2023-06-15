class Node:

    def __init__(self, elem):
        self.elem = elem
        self.cld = None


class Tree:
    def __init__(self):
        self.node_b = None
        self.node_a = None
        self.res = None
        self.root = None

    def __call__(self, elem):
        node = Node(elem)
        if self.root is None:
            self.root = node
        else:
            current_node = self.root
            while current_node.cld is not None:
                current_node = current_node.cld
            current_node.cld = node

    def find_common_node(self, find_a, find_b):
        self.node_a = find_a
        self.node_b = find_b
        try:
            return self._find_common_node(self.root)
        except Exception:
            return self.res

    def _find_common_node(self, root):
        if root is None or root == self.node_a or root == self.node_b:
            return root

        left = self._find_common_node(root.cld)
        right = self._find_common_node(root.cld.cld if root.cld else None)

        if left and right:
            self.res = root
            raise Exception(f'res root:{root.elem}')

        return left or right


if __name__ == "__main__":
    tree = Tree()
    [tree(x) for x in range(0, 10)]

    node_a = tree.root.cld.cld.cld
    node_b = node_a.cld.cld
    common_node = tree.find_common_node(node_a, node_b)
    print(f'node a:{node_a.elem}\tnode b:{node_b.elem}')
    print(f"node: {common_node}\nvalue: {common_node.elem}")
