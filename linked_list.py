class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node


    def insert_at_end(self, data):
        if (self.get_size() == 0):
            self.head = Node(data)
            return

        node = Node(data, None)

        curr = self.head

        while (curr.next is not None):
            curr = curr.next

        curr.next = node

    def print(self):
        if self.head is None:
            print("Linked List doesn't exist!")
            return
        
        curr = self.head
        out = ""

        while curr:
            if (curr.next is not None):
                out += str(curr.data) + "->"
            else:
                out += str(curr.data)
            curr = curr.next

        print(out)

    def get_middle_node(self):
        slow = self.head
        fast = self.head

        while (fast and fast.next):
            slow = slow.next
            fast = fast.next.next

        print(slow.data)

    def get_size(self):
        length = 0

        curr = self.head

        while curr:
            length += 1
            curr = curr.next

        return length


    def remove_index(self, index):

        if index == 0:
            self.head = self.head.next
            return
        
        if (index < 0 or index >= self.get_size()):
            raise Exception("Invalid index")
        
        curr_index = 0
        curr = self.head

        while (curr and curr_index < index - 1):
            curr_index += 1
            curr = curr.next
        
        if curr and curr.next:
            curr.next = curr.next.next

    def remove_value(self, value):
        if self.get_size() == 0:
            raise Exception("Empty linked list!")
        
        curr = self.head

        while (curr and curr.next.data != value):
            curr = curr.next

        if (curr and curr.next):
            curr.next = curr.next.next

    def value_in_list(self, value):
        if self.get_size == 0:
            raise Exception("Empty linked list!")
        
        curr = self.head

        while (curr):
            if (curr.data == value):
                return True
        
            curr = curr.next

        return False
    
    def insert_at(self, index, val):
        if index < 0 or index >= self.get_size():
            raise Exception("Not a valid index")
        
        curr_index = 0
        curr = self.head

        while curr and curr_index < index - 1:
            curr = curr.next
            curr_index += 1

        temp = curr.next
        curr.next = Node(val, temp)

    def has_cycle(self):

        fast = self.head
        slow = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if (fast.data == slow.data):
                return True
            
        return False
    
    def reverse(self):

        prev = None
        curr = self.head

        while (curr):
            next_ = curr.next
            curr.next = prev
            prev = curr
            curr = next_


# -------- Tester --------


linked_list = LinkedList()

linked_list.insert_at_end(1)
linked_list.insert_at_end(2)
linked_list.insert_at_end(3)
linked_list.insert_at_end(4)
linked_list.insert_at(2, 10)

linked_list.reverse()

linked_list.print()
