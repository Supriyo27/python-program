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
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Example usage
if __name__ == "__main__":
    ll = SinglyLinkedList()

    ll.insert_at_end(10)
    ll.insert_at_end(20)
    ll.insert_at_beginning(5)
    ll.insert_at_end(30)

    print("Linked List:")
    ll.display()

    print("Searching for 20:", ll.search(20))
    print("Searching for 99:", ll.search(99))

    print("Deleting node with value 10")
    ll.delete_node(10)
    ll.display()
