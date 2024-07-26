class Node:
    def __init__(self, data):
        self.data = data  # Data stored in the node
        self.next = None  # Pointer to the next node

    def display(self, node):
        while node is not None:
            print(node.data)
            node = node.next


class LinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the list as None

    def create(self, arr, n):
        if n == 0:
            return  # No elements to add

        self.head = Node(arr[0])  # Create the head node
        last = self.head  # Set the last node as the head initially

        for i in range(1, n):
            t = Node(arr[i])
            last.next = t
            last = t

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        # print("None")

    def recDisplay(self, node):
        if node is None:  # Base case: if the node is None, end the recursion
            return
        print(node.data, end=" -> ")
        self.recDisplay(node.next)  # Recursive case: call recDisplay on the next node


# Example Usage
ll = LinkedList()
arr = [3, 5, 7, 10, 15]
ll.create(arr, len(arr))
print("Iterative Display:",end="\n")
ll.display()  # Output: 3 -> 5 -> 7 -> 10 -> 15 -> None

print()
print("Recursive Display:",end="\n")
ll.recDisplay(ll.head)  # Output: 3 -> 5 -> 7 -> 10 -> 15 -> None
# print("None")
print()