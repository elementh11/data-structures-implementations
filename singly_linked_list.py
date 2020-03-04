class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next_node is not None:
            current = current.next_node
        current.next_node = new_node

    def insert_after_item(self, x, data):

        current = self.head
        print(current.next_node)
        while current is not None:
            if current.data == x:
                break
            current = current.next_node
        if current is None:
            print("data not in the list")
        else:
            new_node = Node(data)
            new_node.next_node = current.next_node
            current.next_node = new_node

    def insert_before_item(self, x, data):
        if self.head is None:
            print("List has no element")
            return

        if x == self.head.data:
            new_node = Node(data)
            new_node.next_node = self.head
            self.head = new_node
            return

        current = self.head
        print(current.next_node)
        while current.next_node is not None:
            if current.next_node.data == x:
                break
            current = current.next_node
        if current.next_node is None:
            print("data not in the list")
        else:
            new_node = Node(data)
            new_node.next_node = current.next_node
            current.next_node = new_node

    def insert_at_index(self, index, data):
        if index == 1:
            new_node = Node(data)
            new_node.next_node = self.head
            self.head = new_node
        i = 1
        current = self.head
        while i < index - 1 and current is not None:
            current = current.next_node
            i = i + 1
        if current is None:
            print("Index out of bound")
        else:
            new_node = Node(data)
            new_node.next_node = current.next_node
            current.next_node = new_node

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    def search(self, data):
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        return current

    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def traverse_list(self):
        if self.head is None:
            print("List has no element")
            return
        else:
            current = self.head
            while current is not None:
                print(current.data, " ")
                current = current.next_node

    def reverse_linkedlist(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next_node
            current.next_node = prev
            prev = current
            current = next
        self.head = prev
