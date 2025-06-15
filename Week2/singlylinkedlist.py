class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            print(f"Added head node with value {data}")
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            print(f"Added node with value {data}")

    def print_list(self):
        if not self.head:
            print("The list is empty.")
            return

        current = self.head
        print("Linked List:", end=" ")
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def delete_nth_node(self, n):
        if not self.head:
            raise IndexError("Cannot delete from an empty list.")

        if n <= 0:
            raise ValueError("Index should be a positive integer starting from 1.")

        if n == 1:
            print(f"Deleted node at position 1 with value {self.head.data}")
            self.head = self.head.next
            return

        current = self.head
        count = 1
        while current and count < n - 1:
            current = current.next
            count += 1

        if not current or not current.next:
            raise IndexError("Index out of range.")

        deleted_value = current.next.data
        current.next = current.next.next
        print(f"Deleted node at position {n} with value {deleted_value}")


if __name__ == "__main__":

    ll = LinkedList()


    ll.add_node(10)
    ll.add_node(30)
    ll.add_node(50)
    ll.add_node(70)
    ll.add_node(80)


    ll.print_list()


    try:
        ll.delete_nth_node(3)
    except (IndexError, ValueError) as e:
        print(f"Error: {e}")


    ll.print_list()


    try:
        ll.delete_nth_node(10)
    except (IndexError, ValueError) as e:
        print(f"Error: {e}")


    empty_list = LinkedList()
    try:
        empty_list.delete_nth_node(1)
    except (IndexError, ValueError) as e:
        print(f"Error: {e}")
