
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    #adding element at the front
    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    #adding element at the end
    def insert_at_end(self, data):
        temp = Node(data, None)
        if self.head is None:
            self.head = temp
            self.tail = temp
        else:
            self.tail.next = temp
            self.tail = temp


    #another way adding element at the end
    def insert_at_end2(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        # moving at the end
        current = self.head
        while current.next:
            current = current.next

        current.next = Node(data, None)

    def display(self):
        if self.head is None:
            print("Linked list is empty")
            return
        current = self.head
        lstr = ''
        while current:
            lstr += str(current.data) + '-->'
            current = current.next

        print(lstr)

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_beginning(4)
    ll.insert_at_beginning(8)
    ll.insert_at_beginning(10)
    ll.display()

    ll2 = LinkedList()
    ll2.insert_at_end(3)
    ll2.insert_at_end(7)
    ll2.insert_at_end(9)
    ll2.insert_at_end(12)
    ll2.display()