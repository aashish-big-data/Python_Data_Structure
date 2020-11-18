# -*- coding: utf-8 -*-
"""

@author: AASHISH
"""
# Binary Search Tree in Python

class Node_Tree:
	def __init__(self, val):
		self.value = val
		self.leftChild = None
		self.rightChild = None
		
	def insert(self, data):
		if self.value == data:
			return False
			
		elif self.value > data:
			if self.leftChild:
				return self.leftChild.insert(data)
			else:
				self.leftChild = Node_Tree(data)
				return True

		else:
			if self.rightChild:
				return self.rightChild.insert(data)
			else:
				self.rightChild = Node_Tree(data)
				return True
				
	def find(self, data):
		if(self.value == data):
			return True
		elif self.value > data:
			if self.leftChild:
				return self.leftChild.find(data)
			else:
				return False
		else:
			if self.rightChild:
				return self.rightChild.find(data)
			else:
				return False
				
	def getHeight(self):
		if self.leftChild and self.rightChild:
			return 1 + max(self.leftChild.getHeight(), self.rightChild.getHeight())
		elif self.leftChild:
			return 1 + self.leftChild.getHeight()
		elif self.rightChild:
			return 1 + self.rightChild.getHeight()
		else:
			return 1

	def preorder(self):
		if self:
			print (str(self.value),end=" ")
			if self.leftChild:
				self.leftChild.preorder()
			if self.rightChild:
				self.rightChild.preorder()

	def postorder(self):
		if self:
			if self.leftChild:
				self.leftChild.postorder()
			if self.rightChild:
				self.rightChild.postorder()
			print (str(self.value),end=" ")

	def inorder(self):
		if self:
			if self.leftChild:
				self.leftChild.inorder()
			print (str(self.value),end=" ")
			if self.rightChild:
				self.rightChild.inorder()

class Main_Tree:
	def __init__(self):
		self.root = None

	def insert(self, data):
		if self.root:
			return self.root.insert(data)
		else:
			self.root = Node_Tree(data)
			return True

	def find(self, data):
		if self.root:
			return self.root.find(data)
		else:
			return False
			
	def getHeight(self):
		if self.root:
			return self.root.getHeight()
		else:
			return -1
	
	def remove(self, data):
		# empty tree
		if self.root is None:
			return False
			
		# data is in root node	
		elif self.root.value == data:
			if self.root.leftChild is None and self.root.rightChild is None:
				self.root = None
			elif self.root.leftChild and self.root.rightChild is None:
				self.root = self.root.leftChild
			elif self.root.leftChild is None and self.root.rightChild:
				self.root = self.root.rightChild
			elif self.root.leftChild and self.root.rightChild:
				delNodeParent = self.root
				delNode = self.root.rightChild
				while delNode.leftChild:
					delNodeParent = delNode
					delNode = delNode.leftChild
					
				self.root.value = delNode.value
				if delNode.rightChild:
					if delNodeParent.value > delNode.value:
						delNodeParent.leftChild = delNode.rightChild
					elif delNodeParent.value < delNode.value:
						delNodeParent.rightChild = delNode.rightChild
				else:
					if delNode.value < delNodeParent.value:
						delNodeParent.leftChild = None
					else:
						delNodeParent.rightChild = None
						
			return True
		
		parent = None
		node = self.root
		
		# find node to remove
		while node and node.value != data:
			parent = node
			if data < node.value:
				node = node.leftChild
			elif data > node.value:
				node = node.rightChild
		
		#  data not found
		if node is None or node.value != data:
			return False
			
		#  remove-node has no children
		elif node.leftChild is None and node.rightChild is None:
			if data < parent.value:
				parent.leftChild = None
			else:
				parent.rightChild = None
			return True
			
		#  remove-node has left child only
		elif node.leftChild and node.rightChild is None:
			if data < parent.value:
				parent.leftChild = node.leftChild
			else:
				parent.rightChild = node.leftChild
			return True
			
		#  remove-node has right child only
		elif node.leftChild is None and node.rightChild:
			if data < parent.value:
				parent.leftChild = node.rightChild
			else:
				parent.rightChild = node.rightChild
			return True
			
		#   remove-node has left and right children
		else:
			delNodeParent = node
			delNode = node.rightChild
			while delNode.leftChild:
				delNodeParent = delNode
				delNode = delNode.leftChild
				
			node.value = delNode.value
			if delNode.rightChild:
				if delNodeParent.value > delNode.value:
					delNodeParent.leftChild = delNode.rightChild
				elif delNodeParent.value < delNode.value:
					delNodeParent.rightChild = delNode.rightChild
			else:
				if delNode.value < delNodeParent.value:
					delNodeParent.leftChild = None
				else:
					delNodeParent.rightChild = None

	def preorder_Traversal(self):
		if self.root is not None:
			print("Pre")
			self.root.preorder()
		
	def postorder_Traversal(self):
		if self.root is not None:
			print("Post")
			self.root.postorder()
			
	def inorder_Traversal(self):
		if self.root is not None:
			print("In")
			self.root.inorder()

bst = Main_Tree()
print(bst.insert(10))
print(bst.insert(1))
print(bst.insert(7))
print(bst.insert(12))
print(bst.insert(15))
print(bst.insert(13))

#print(bst.insert(5))
#bst.preorder()
#print(bst.getHeight())
#bst.postorder()
bst.inorder_Traversal()
print(bst.remove(10))
bst.preorder_Traversal()
