""" just a basic tree """


class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def search(self, target):
        if self.data == target:
            print("Found it")
            return self

        if self.left and self.data > target:
            return self.left.search(target)

        if self.right and self.data < target:
            return self.right.search(target)

        print("Value is not present in the tree")

    def traversePreOrder(self):
        print(self.data)
        if self.left:
            self.left.traversePreOrder()
        if self.right:
            self.right.traversePreOrder()

    def traverseInOrder(self):
        if self.left:
            self.left.traverseInOrder()
        print(self.data)
        if self.right:
            self.right.traverseInOrder()

    def traversePostOrder(self):
        if self.left:
            self.left.traversePostOrder()
        if self.right:
            self.right.traversePostOrder()
        print(self.data)

    def treeHeight(self, h=0):
        leftHeight = self.left.treeHeight(h+1) if self.left else h
        rightHeight = self.right.treeHeight(h+1) if self.right else h
        return max(leftHeight, rightHeight)

    def getNodesAtDepth(self, depth, nodes=[]):
        if depth == 0:
            nodes.append(self.data)
            return nodes

        if self.left:
            self.left.getNodesAtDepth(depth-1, nodes)
        if self.right:
            self.right.getNodesAtDepth(depth-1, nodes)
        return nodes


class Tree():
    def __init__(self, root, name=''):
        self.root = root
        self.name = name

    def search(self, target):
        return self.root.search(target)


node = Node(10)
node.left = Node(5)
node.right = Node(15)
node.left.left = Node(3)
node.left.right = Node(7)
node.right.left = Node(12)
node.right.right = Node(18)

# print(node.data)
# print(node.left.data)
# found = node.search(18)
# print("Data found:", found.data)

# myTree = Tree(root=node, name="Jijo's tree")
# print("tree left data", myTree.root.left.left.data)
# print("tree right data", myTree.root.right.right.data)

# found_from_tree = myTree.search(12)
# print(found_from_tree.data)

# print(node.traversePostOrder())
# print(node.treeHeight())
print(node.getNodesAtDepth(1))
