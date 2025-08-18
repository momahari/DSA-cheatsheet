
class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        new_node = Node(data, prev=itr, next=None)
        itr.next = new_node

    def insert_list(self, list):
        self.head = None
        for data in list:
            self.insert_at_end(data)

    def print_forward(self):
        if self.head == None:
            print("List is empty")
            return

        itr = self.head
        while itr:
            print(' <-- ' + itr.data, end = ' --> ')
            itr = itr.next
        print()

    def print_backward(self):
        if self.head is None:
            print("List is empty")
            return

        # Go to last node
        itr = self.head
        while itr.next:
            itr = itr.next

        # Traverse backward using .prev
        while itr:
            print(' <-- ' + itr.data, end=' --> ')
            itr = itr.prev
        print()

    # def print_backward(self):
    #     if self.head == None:
    #         print("List is empty")
    #         return
    #
    #     itr = self.head
    #     nodes_data = []
    #     while itr:
    #         nodes_data.append(itr.data)
    #         itr = itr.next
    #
    #     for i in range(len(nodes_data)-1, -1, -1):
    #         print(' <-- ' + nodes_data[i], end = ' --> ')

if __name__ == '__main__':
    dll = DoublyLinkedList()
    dll.insert_list(['GSIT', 'EI', 'ME', 'RE', 'ER'])
    dll.print_forward()
    dll.print_backward()