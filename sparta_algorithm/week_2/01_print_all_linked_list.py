class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

node = Node(3)
first_node = Node(4)

node.next = first_node
# print(node.next.data)

class LinkedList:
    '''
    링크드 리스트는 노드들이 연결되어 있는 형태이므로
    head만 초기화하여 데이터와 포인터를 가진 노드를 추가하여 구현
    '''
    def __init__(self, data):
        self.head = Node(data)

    # 데이터 추가
    # 맨 끝 노드의 next 노드는 None
    def append(self, data):

        # 예외처리: head가 없는 경우 -> 추가할 노드가 head가 됨
        if self.head is None:
            self.head= Node(data)
            return

        # head 노드가 있다면
        cur = self.head

        # cur: 탐색노드
        # 다음노드가 있으면 계속 노드를 이동
        while cur.next is not None:
            cur = cur.next

        # next노드가 None인 노드의 next노드에 새 노드 삽입
        cur.next = Node(data)

    def print_all(self):
        cur = self.head

        # 탐색노드가 None이 아닐때까지 출력
        while cur is not None:
            print(cur.data)
            cur = cur.next

linked_list = LinkedList(3) # 링크드 리스트 초기화
# print(linked_list.head.data) # head노드에 있는 데이터 출력
linked_list.append(4)
linked_list.append(5)
linked_list.print_all()
