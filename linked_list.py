class Node:
    def __init__(self, item, next=None):
        self.data = item
        self.next = next


class LinkedList:
    def __init__(self, head):
        self.head = head

    def prepend(self, item):
        new_node = Node(item, self.head)
        self.head = new_node

    def append(self, item):
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next

            current_node.next = new_node

    def print_linked_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data, end=' ')
            current_node = current_node.next

        print()

    def remove_node(self, node):
        if node is self.head:
            self.head = self.head.next
        else:
            current_node = self.head
            while current_node.next is not node:
                current_node = current_node.next

            current_node.next = node.next

    def insert(self, node, item):
        new_node = Node(item, node.next)
        node.next = new_node


head = Node(5)

new_ll = LinkedList(head)

new_ll.prepend(8)
new_ll.prepend(20)
new_ll.prepend(10)
new_ll.append(10)
new_ll.remove_node(new_ll.head)

new_ll.insert(new_ll.head, 5)

new_ll.print_linked_list()
