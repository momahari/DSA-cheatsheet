
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    """
    Insert any data at the beginning of the list
    """
    def insert(self, data):
        node = Node(data, self.head)
        self.head = node

    """
    Insert any data at the end of the list
    """
    def insert_at_end(self, data):
        if self.head == None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def insert_list(self, list):
        self.head = None
        for data in list:
            self.insert_at_end(data)

    """
    display the linked list
    """
    def display(self):
        itr = self.head
        while itr:
           print(itr.data, end=" --> ")
           itr = itr.next

    def get_length(self):
        itr = self.head
        length = 0
        while itr:
            length += 1
            itr = itr.next
        return length

    def search(self, data):
        if(self.head == None):
            return "not found"

        itr = self.head
        index = 0
        while itr:
            if(itr.data == data):
                return f"{data} is in index {index}"
            itr = itr.next
            index += 1
        return "not found"

    def reverse_ll(self):
        l = self.get_length()
        itr = self.head
        rev_ll = LinkedList()
        for i in range(l):
            rev_ll.insert(itr.data)
            itr = itr.next
        rev_ll.display()

    """
    Insert at index ?
    """
    def insert_at_index(self, index, data):
        if index < 0 or index >= self.get_length():
            raise IndexError("Index out of range")

        if index == 0 :
            self.insert(data)
            return

        itr = self.head
        while index - 1 > 0:
            itr = itr.next
            index -= 1
        new_node = Node(data, itr.next)
        itr.next = new_node

    """
    Remove elements by index
    """
    def remove_at_index(self, index):
        if index < 0 or index >= self.get_length():
            raise IndexError("Index out of range")

        if index == 0:
            self.head = self.head.next
            return

        itr = self.head
        while index - 1 > 0:
            itr = itr.next
            index -= 1
        itr.next = itr.next.next

    def insert_after_value(self, data_after, data_to_insert):
        itr = self.head
        while itr:
            if itr.data == data_after:
                node = Node(data_to_insert, itr.next)
                itr.next = node
                return
            itr = itr.next

    def remove_by_value(self, data):
        if self.head == None:
            print("List is empty")
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        itr = self.head
        while itr:
            if itr.next.data == data:
                itr.next = itr.next.next
                return
            itr = itr.next

    def clear_ll(self):
        self.head = None

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_list(['sqlite3', 'PostgreSQL', 'Mysql', 'Oracle'])
    ll.insert_after_value('Mysql', 'NoSQL')
    print(ll.search('mn'))
    ll.display()
    print()
    ll.reverse_ll() # no need to use print to display the reversed linked list
    print(f"lenght of the linked list is {ll.get_length()}")