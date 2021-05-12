# coding:utf-8


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class NodeList:
    def __init__(self):
        self.head = Node(None)

    def __repr__(self):
        node = self.head.next
        prt_list = []
        while node is not None:
            if isinstance(node.val, int):
                prt_list.append(str(node.val))
            else:
                prt_list.append(node.val)
            node = node.next

        return ', '.join(prt_list)

    def add_node(self, node):
        if self.head is None:
            self.head.next = node
        else:
            temp = self.head.next
            self.head.next = node
            node.next = temp

    def del_node(self, val):
        node = self.head
        while node.next is not None:
            if node.next.val == val:
                if node.next.next is None:
                    node.next = None
                else:
                    node.next = node.next.next
                break
            else:
                node = node.next


if __name__ == "__main__":
    linked_list = NodeList()
    linked_list.add_node(Node(1))
    linked_list.add_node(Node(3))
    linked_list.add_node(Node(5))
    print(linked_list)
    linked_list.del_node(5)
    print(linked_list)
