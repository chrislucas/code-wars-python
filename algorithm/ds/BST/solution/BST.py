'''
https://www.geeksforgeeks.org/binary-search-tree-data-structure/
https://www.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/
https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/
'''


class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.root = None

    def get(self):
        return self.data

    def set(self, data):
        self.data = data


class BST:

    def __init__(self):
        self.root = None

    def root(self):
        return self.root

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.insert_node(self.root, data)

    def insert_node(self, node, data):
        if data < node.data:
            if node.left is not None:
                self.insert_node(node.left, data)
            else:
                node.left = Node(data)
        elif data > node.data:
            if node.right is not None:
                self.insert_node(node.right, data)
            else:
                node.right = Node(data)

    def search(self, data):
        return self.search_data(self.root, data)

    def search_data(self, node, data):
        if node is None:
            return None
        elif data < node.data:
            return self.search_data(node.left, data)
        elif data > node.data:
            return self.search_data(node.right, data)
        else:
            return node


    def delete(self, data):
        self.__delete(self.root, data)

    def __delete(self, node, data):
        if node:
            if node.data == data:
                if node.left and node.right:
                    pass

    def __inorder(self, root):
        if root:
            self.__inorder(root.left)
            print(root.data)
            self.__inorder(root.right)

    def inorder(self):
        self.__inorder(self.root)

    def __preorder(self, root):
        if root:
            print(root.data)
            self.__preorder(root.left)
            self.__preorder(root.right)

    def preorder(self):
        self.__preorder(self.root)

    def __postorder(self, root):
        if root:
            self.__postorder(root.left)
            self.__postorder(root.right)
            print(root.data)

    def postorder(self):
        self.__postorder(self.root)


def test():
    bst.preorder()
    print()
    bst.inorder()
    print()
    bst.postorder()


'''
50 30 70 20 40 60 80
'''
bst = BST()
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)
bst.insert(60)
bst.insert(80)

test()

node = bst.search(85)
print(node.data if node else 'None')
