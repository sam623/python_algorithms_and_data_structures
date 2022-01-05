# Node class that creates individual nodes
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
    
    
# Linked List Class
class LinkedList:
  def __init__(self,data):
    new_node = Node(data)
    self.head = new_node
    self.tail = new_node
    self.length = 1

# Print Linked List
  def print_Linked_List(self):
    temp = self.head
    while temp is not None:
      print(temp.data)
      temp = temp.next

  
