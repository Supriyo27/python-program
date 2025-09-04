#write a program to convert a string into linked list oofcharacters
class Node:
    def __init__(self, data):
        self.data = data  # One character
        self.next = None  # Pointer to next node


class CharLinkedList:
    def __init__(self):
        self.head = None

    def string_to_linked_list(self, input_string):
        if not input_string:
            return

        self.head = Node(input_string[0])  # Create head node
        current = self.head

        for char in input_string[1:]:
            new_node = Node(char)
            current.next = new_node
            current = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Example usage
if __name__ == "__main__":
    input_str = "hello"
    cll = CharLinkedList()
    cll.string_to_linked_list(input_str)

    print(f"Linked list for string '{input_str}':")
    cll.display()
