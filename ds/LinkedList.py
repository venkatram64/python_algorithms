
#definition of Node
class Node:
    def __init__(self, data=None, next=None):
        self.data = data # to store data
        self.next = next # to point next node


class LinkedList:
    def __init__(self):
        self.head = None # head pointer to point to the node
        self.tail = None # tail pointer to point to the node

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

    def insert_values(self, lst):
        self.head = None
        for data in lst:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next

        return count

    def remove_by_index(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index.")
        if index == 0:
            self.head = self.head.next
            return
        count = 0
        current = self.head
        while current:
            if count == index - 1:  #check prior index
                current.next = current.next.next
                break
            current = current.next
            count += 1

    def remove_by_value(self, data):
        if data is None:
            return
        #first element data
        if self.head.data == data:
            self.head = self.head.next
            print(f'{data} is deleted')
        current = self.head
        #keep the previous node, after deleting the node previous should hold
        #the deleted node's next element
        previous = current
        while current:
            if current.data == data:
                previous.next = current.next
                break
            previous = current
            current = current.next




    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index.")
        if index == 0:
            self.insert_at_beginning(data)
            return
        count = 0
        current = self.head
        while current:
            if count == index - 1: #stop at previous index
                node = Node(data, current.next)
                current.next = node
                break
            current = current.next
            count += 1

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
    #adding elements
    ll3 = LinkedList()
    ll3.insert_values(["banana", "mango", "grapes", "apples", "pine apple"])
    print("Length of list: ", ll3.get_length())
    ll3.display()
    #remove the element
    ll3.remove_by_index(3)
    ll3.display()
    #inserting element at a perticular location
    ll4 = LinkedList()
    ll4.insert_values(["banana", "mango", "grapes", "apples", "pine apple"])
    print("Length of list: ", ll4.get_length())
    ll4.display()
    # remove the element
    ll4.insert_at(2, "sapota")
    ll4.display()
    #deleting by value

    ll5 = LinkedList()
    ll5.insert_values(["banana", "mango", "grapes", "apples", "pine apple"])
    print("Length of list: ", ll5.get_length())
    ll5.display()
    # remove the element
    ll5.remove_by_value("grapes")
    ll5.display()

