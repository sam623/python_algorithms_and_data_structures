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
  
# Append to the end of Linked List
    def append(self,data):
        new_node = Node(data)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
# Pop from the end of the Linked List
    def pop(self):
        if self.head.next is None:
            self.head = None
            self.tail = None
            self.length = 0
            return None
            
        else:
            temp = self.head
            while temp.next is not self.tail:
                temp = temp.next
            self.tail = temp
            self.tail.next = None
            self.length -= 1    
        return self.tail.data
    
    def prepend(self,data):
        new_node = Node(data)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += self.length
        return True
    def pop_first(self):
        if self.head.next is None:
            self.head = None
            self. tail = None
            self.length = 0
        else:
            temp = self.head
            self.head = temp.next
            temp.next = None
            self.length -+ self.length
        return True 
