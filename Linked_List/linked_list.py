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

# Prepend to the beginning of the Linked List
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
    
# Pop from the beginning of the Linked List
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
         
# Get the node at index location of the Linked List     
    def get(self,index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

# set the node at index location of the Linked List
    def set(self, index, data):
        temp = self.get(index)
        if temp:
            temp.data = data
            return True
        return False

# Insert a new node at specified index into the Linked List
    def insert(self, index, data):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(data)
        
        if index == self.length:
            return self.append(data)
        
        new_node = Node(data)
        temp = self.get(index-1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += self.length
        
        return True
