# Create node for BinaryTree
# Properties of binary Search Tree:
    # The left subtree of a node contains only nodes with keys lesser than the node’s key.
    # The right subtree of a node contains only nodes with keys greater than the node’s key.
    # The left and right subtree each must also be a binary search tree.
    # There must be no duplicate nodes.

class BinaryTreeNode:
    # here we expect some value and a left child value and a right child value
    def __init__(self,val, left=None, right= None):
        self.val = val
        self.left = left
        self.right = right

    # adding a child
    def add_child(self,new_val):
        if self.val:
            # in Binary search Tree , we dont have duplicates
            if self.val == new_val:
                return

            elif new_val < self.val:
            # go to the left
                #if left child exists
                if self.left:
                    self.left.add_child(new_val)
                #if there is no left child
                else:
                    self.left = BinaryTreeNode(new_val)

            else:
                #go to the right
                # if right child exists
                if self.right:
                    self.right.add_child(new_val)
                # if there is no left child
                else:
                    self.right = BinaryTreeNode(new_val)
        else:
            self.val = new_val


    def printTree(self):
        if self.left:
            #print left
            self.left.printTree()
        print(self.val)
        if self.right:
            #print right
            self.right.printTree()

    #print left -> root -> right
    def inorder_traversal(self):
        elements = []
        if self.left:
            elements += self.left.inorder_traversal()
        elements.append(self.val)
        if self.right:
            elements += self.right.inorder_traversal()
        return elements

    #print root -> left -> right
    def preorder_traversal(self):
        elements = []
        elements.append(self.val)
        if self.left:
            elements += self.left.inorder_traversal()
        if self.right:
            elements += self.right.inorder_traversal()
        return elements

    #print left -> right -> root
    def postorder_traversal(self):
        elements = []
        if self.left:
            elements += self.left.inorder_traversal()
        if self.right:
            elements += self.right.inorder_traversal()
        elements.append(self.val)
        return elements

    def search(self,data):
        #check if the val is here

        if data == self.val:
            return True
        if data < self.val:
            if self.left:
                return self.left.search(data)
            else:
                return False
        if data > self.val:
            if self.right:
                return self.right.search(data)
            else:
                return False

    def find_min(self):
        if self.left is None:
            return self.val
        else:
            return self.left.find_min()

    def find_max(self):
        if self.right is None:
            return self.val
        else:
            return self.right.find_max()

    def calculate_sum(self):
        sum = 0
        if self.left:
            sum += self.left.calculate_sum()
        sum+= self.val
        if self.right:
            sum += self.right.calculate_sum()

        return sum

    def delete(self,data):
        if data < self.val:
            # go and check val in left and delete
            #check if left exists:
            if self.left:
                self.left = self.left.delete(data)
            else:
                return
        if data > self.val:
            # go and chack val in right and delete
            if self.right:
                self.right = self.right.delete(data)
            else:
                return
        else:
            # delete the node you are in
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left

            #way_1: find the min in right sub tree and replace the values after deleting the current val
            # min_right = self.right.find_min()
            # self.val = min_right
            # self.right=self.right.delete(min_right)

            # way_2: find the max in left sub tree and replace the values after deleting the current val
            max_left = self.left.find_max()
            self.val = max_left
            self.left = self.left.delete(max_left)

        return self


def buildTree(elements):
    root  = BinaryTreeNode(elements[0])
    for each in range(1,len(elements)):
        root.add_child(elements[each])
    return root


if __name__ =="__main__":
    root = BinaryTreeNode(10)
    #root.print_tree()
    root.add_child(12)
    root.add_child(8)
    #root.print_tree()
    #root.printTree()
    root.add_child(13)
    root.add_child(18)
    root.add_child(10)
    root.add_child(11)
    #root.printTree()
    print(root.inorder_traversal())
    print(root.preorder_traversal())
    print(root.postorder_traversal())
    print(root.search(12))
    print(root.search(25))

    #build tree using helper method
    lst = ["India","Australia","Germany","US"]
    my_tree = buildTree(lst)
    print(my_tree.inorder_traversal())
    print(my_tree.preorder_traversal())
    print(my_tree.postorder_traversal())
    print(my_tree.search("Pak"))

    print(root.find_min())
    print(root.find_max())
    print(root.calculate_sum())
    root.delete(12)
    print(root.inorder_traversal())




