from models.Node import Node

class LinkedList:
    def __init__(self):
        self.start_node = Node

     # Põe o país na primeira posição
    def push(self, new_data):
        new_node = Node(new_data)
         
        #Make next of new Node as head
        new_node.next = self.head
         
        #Move the head to point to new Node
        self.head = new_node

    def append(self, new_data):
 
        # Create a new node, Put in the data, Set next as None
        new_node = Node(new_data)
 
        # If the Linked List is empty, then make the
        # new node as head
        if self.head is None:
            self.head = new_node
            return
 
        # Else traverse till the last node
        last = self.head
        while (last.next):
            last = last.next
 
        # Change the next of last node
        last.next =  new_node
    
class Node:
    def __init__(self, data):
        self.item = data
        self.ref = None
    
    def get_item(self):
        return self.item
    
    def get_ref(self):
        return self.ref