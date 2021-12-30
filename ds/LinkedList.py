
class Node:
    def __init__(self, data=None, nxt=None):
        self.data = data
        self.next = nxt


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def display(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        lstr = ''
        while itr:
            lstr += str(itr.data) + '-->'
            itr = itr.next

        print(lstr)

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_beginning(4)
    ll.insert_at_beginning(8)
    ll.insert_at_beginning(10)
    ll.display()