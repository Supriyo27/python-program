#write a program to impliment a singly linked list
class Node:
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null


class SinglyLinkedList:
    def __init__(self):
        self.head = None  # Start with empty list

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:  # If list is empty
            self.head = new_node
            return
        current = self.head
        while current.next:  # Traverse to the last node
            current = current.next
        current.next = new_node

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head  # New node points to old head
        self.head = new_node  # Head is updated to new node

    def delete_node(self, key):
        current = self.head

        # If head node holds the key to be deleted
        if current and current.data == key:
            self.head = current.next
            current = None
            return

        # Search for the key
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        # If key not found
        if current is None:
            print("Node not found.")
            return

        prev.next = current.next
        current = None

    def search(self, key):
        current = self.head
