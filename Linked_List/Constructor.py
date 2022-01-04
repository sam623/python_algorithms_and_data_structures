
# Node class that creates individual nodes
class Node:
  def __init__(self, value):
    self.value = value
    self.next = None
    
    
# Linked List Class
class LinkedList:
  def __init__(self,value):
    new_node = Node(value)
    self.head = new_node
    self.tail = new_node
    self.length = 1
  
