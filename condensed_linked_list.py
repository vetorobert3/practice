# Node Class
class Node:
    # Constructor to initialize the node object
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class LinkedList:
    # Function to initialize the head
    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning (for driver code)
    def push(self, new_value):
        new_node = Node(new_value)
        new_node.next = self.head
        self.head = new_node

    # Given a reference to the head of a list and a key, delete the first occurence of key in linked list
    def deleteNode(self, key):
        # store head node
        temp = self.head

        # If head node itself holds the key to be deleted
        if temp is not None:
            if temp.value == key:
                self.head = temp.next
                temp = None
                return

        # Search for the key to be deleted, keep track of the previous node as we need to change "prev.next"
        while temp is not None: # might need paranthese
            if temp.value == key:
                break
            prev = temp
            temp = temp.next

        # if key was not present in linked list
        if temp == None:
            return

        # Unlink the node from linked list
        prev.next == temp.next

        temp = None

    def condense_linked_list(node):
        if node is None or node.next is None:
            return node

        hash = set()
        current = node
        hash.add(node.value)

        while current.next is not None:
            if current.next.value in hash:
                current.next = current.next.next
            else:
                hash.add(current.next.value)
                current = current.next

        return node