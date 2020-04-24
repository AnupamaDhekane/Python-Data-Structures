from typing import Type


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, data):
        self.head = Node(data)

    def addition(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def deletion(self, index):
        if index > self.length():
            print("Invalid Index")
            return
        if self.head is None:
            print("Empty Linked list")
            return
        current_index = 0
        currentnode = self.head
        while True:
            if current_index == index:
                if index == 0:
                    currentnode.next = self.head
                    print("deleted the node at index" + index, currentnode.data)
                    self.display()
                else:
                    lastnode.next = currentnode.next
                    print("Deleted the node at index", index, currentnode.data)
                    self.display()
            lastnode: Type[Node] = currentnode
            currentnode = currentnode.next
            current_index += 1

    def length(self):
        if self.head is None:
            return
        len = 0
        current = self.head
        while current.next is not None:
            current = current.next
            len += 1
        print("Length of Linked list is",len)
        return len

    def display(self):
        current = self.head
        nodes = []
        while current.next is not None:
            nodes.append(current.data)
            current = current.next
        print(nodes)

new_list: LinkedList = LinkedList(12)
new_list.addition(23)
new_list.addition(230)
new_list.addition(19)
new_list.addition(33)
new_list.addition(24)
new_list.addition(34)

new_list.display()
new_list.length()

new_list.deletion(3)



