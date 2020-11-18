# -*- coding: utf-8 -*-
"""

@author: AASHISH
"""
from collections import deque

# Data structure to store a Binary Tree node
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


# Function to check if given node is a leaf node or not
def isLeaf(node):
    return node.left is None and node.right is None


# Recursive function to find paths from root node to every leaf node
def printRootToLeafPaths(node, path):

    # base case
    if node is None:
        return

    # include current node to the path
    path.append(node.data)

    # if leaf node is found, print the path
    if isLeaf(node):
        print(list(path))

    # recur for left and right subtree
    printRootToLeafPaths(node.left, path)
    printRootToLeafPaths(node.right, path)

    # remove current node after left and right subtree are done
    path.pop()


# Main function to print paths from root node to every leaf node
def printRootToLeafPath(node):

    # list to store root to leaf path
    path = deque()
    printRootToLeafPaths(node, path)


if __name__ == '__main__':

    """ Construct below tree
              1
            /   \
           /     \
          2       3
         / \     / \
        4   5   6   7
               /     \
              8       9
    """

    root = Node(3)
    root.left = Node(4)
    root.right = Node(0)
    
    '''
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.right.left.left = Node(8)
    root.right.right.right = Node(9)
    '''
    
    # print all root to leaf paths
    printRootToLeafPath(root)
