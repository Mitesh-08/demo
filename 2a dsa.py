class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insertAtBeginning(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    def insertAfter(self, prev_node, new_data):
        if prev_node is None:
            print("The given previous node must be in LinkedList.")
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node
    def insertAtEnd(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
    def deleteNode(self, position):
        if self.head is None:
            return
        temp = self.head
        if position == 0:
            self.head = temp.next
            return
        for i in range(position - 1):
            temp = temp.next
            if temp is None:
                return
        if temp.next is None:
            return
        next_node = temp.next.next
        temp.next = next_node
    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False
    def sortLinkedList(self):
        if self.head is None:
            return
        current = self.head
        while current:
            index = current.next
            while index:
                if current.data > index.data:
                    current.data, index.data = index.data, current.data
                index = index.next
            current = current.next
    def printList(self):
        temp = self.head
        while temp:
            print(str(temp.data), end=" ")
            temp = temp.next
        print()
if __name__ == '__main__':
    llist = LinkedList()
    llist.insertAtEnd(1)
    llist.insertAtBeginning(2)
    llist.insertAtBeginning(3)
    llist.insertAtEnd(4)
    llist.insertAfter(llist.head.next, 5)
    print('Singly Linked List')
    print('Linked list:')
    llist.printList()
    print("\nAfter deleting an element:")
    llist.deleteNode(3)
    llist.printList()
    item_to_find = 3
    if llist.search(item_to_find):
        print(str(item_to_find) + " is found")
    else:
        print(str(item_to_find) + " is not found")
    llist.sortLinkedList()
    print("Sorted List:")
    llist.printList()
