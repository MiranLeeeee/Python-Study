class Node :
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, data):
        self.head = Node(data)

    def append(self,data):
        if self.head is None:
            self.head = Node(data)
            return

        cur = self.head

        while cur.next is not None:
            cur = cur.next
        cur.next = Node(data)

    def print_all(self):
        cur = self.head

        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        cur = self.head
        count = 0
        while count < index:
            cur = cur.next
            count += 1
        return cur


linked_list =LinkedList(3)
linked_list.append(4)

# linked_list.print_all()
print(linked_list.get_node(1).data)
