class ListNode:
    def __init__(self, value, next_ = None, prev = None):
        self.value = value
        self.next = next_
        self.prev = prev

class DoubleLinkedList:
    def __init__(self, value):
        self.head = ListNode(value)
        self.tail = self.head
        self.length = 1

    def append(self, value):
        _new_node = ListNode(value)
        _new_node.prev = self.tail
        self.tail.next = _new_node
        self.tail = _new_node
        self.length += 1
        return self

    def prepend(self, value):
        _new_node = ListNode(value)
        self.head.prev = _new_node
        _new_node.next = self.head
        self.head = _new_node
        self.length += 1
        return self

    def reverse(self):
        if not self.head.next:
            return self.head

        first = self.head
        self.tail = self.head
        second = first.next

        while second:
            _temp = second.next
            second.next = first
            first = second
            second = _temp

        self.head.next = None
        self.head = first
        return self

    def print_list(self):
        print(f'HEAD: {self.head.value}')
        current_node = self.head

        while current_node.next:
            print(current_node.value)
            current_node = current_node.next

        print(current_node.value)
        print(f'TAIL: {self.tail.value}')
