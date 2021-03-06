from node import Node

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
            return

        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next

        current_node.next = node

    def __len__(self):
        length = 0

        current_node = self.head
        while current_node is not None:
            length += 1
            current_node = current_node.next

        return length

    def __str__(self):
        result = ''
        
        if len(self) == 0:
            return result

        node = self.head
        while node.next:
            result += f"{node.data} -> "
            node = node.next

        result += f"{node.data}"

        return result

    def prepend(self, data):
        node = Node(data)
        if not self.head:
            self.append(node)

        node.next = self.head
        self.head = node

    def insert_after_node(self, data, new_data):
        # foolishly assumes that data _is_ in the list
        node = self.head
        new_node = Node(new_data)
        while node.data is not data:
            node = node.next
        
        new_node.next = node.next
        node.next = new_node

    def delete_by_value(self, value):
    # foolishly assumes that value _is_ in the list
        if self.head.data is value:
            self.head = None

        previous = None
        node = self.head
        while node and node.data is not value:
            previous, node = node, node.next
        
        if node:
            previous.next = node.next
            node.next = None

    def delete_by_position(self, position):
        current_position = 0
        current_node = self.head

        while current_position is not position:
            current_node = current_node.next
            current_position += 1

if __name__ == '__main__':
    import unittest

    class TestLinkedList(unittest.TestCase):

        def test_append(self):
            ll = LinkedList()
            ll.append("A")
            self.assertEqual(ll.head.data, "A")

            ll.append("B")

        def test__len__(self):
            ll = LinkedList()
            self.assertEqual(len(ll), 0)

            for letter in ["A", "B", "C"]:
                ll.append(letter)

            self.assertEqual(len(ll), 3)

        def test__str__(self):
            ll = LinkedList()
            for letter in ["A", "B", "C"]:
                ll.append(letter)

            self.assertEqual(str(ll), "A -> B -> C")

        def test_prepend(self):
            ll = LinkedList()
            for letter in ["A", "B", "C"]:
                ll.append(letter)

            ll.prepend("Z")
            self.assertEqual(ll.head.data, "Z")
            self.assertEqual(str(ll), "Z -> A -> B -> C")
            self.assertEqual(len(ll), 4)

        def test_insert_after_node(self):
            ll = LinkedList()
            for letter in ["A", "B", "C"]:
                ll.append(letter)

            ll.insert_after_node("B", "Z")
            self.assertEqual(str(ll), "A -> B -> Z -> C")
            self.assertEqual(len(ll), 4)

        def test_deletion_by_value(self):
            ll = LinkedList()
            for letter in ["A", "B"]:
                ll.append(letter)

            ll.delete_by_value("B")
            self.assertEqual(str(ll), "A")
            self.assertEqual(len(ll), 1)

            ll.delete_by_value("A")
            self.assertEqual(str(ll), "")
            self.assertEqual(len(ll), 0)

        def test_deletion_by_position(self):
            ll = LinkedList()
            for letter in ["A", "B"]:
                ll.append(letter)

            ll.delete_by_position(1)
            self.assertEqual(str(ll), "A")
            self.assertEqual(len(ll), 1)

            ll.delete_by_position(0)
            self.assertEqual(str(ll), "")
            self.assertEqual(len(ll), 0)


    unittest.main()


