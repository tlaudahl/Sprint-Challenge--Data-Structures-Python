from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def __len__(self):
        return self.storage.length

    def append(self, item):
        # If length of storage is less than the capacity
        if self.storage.length < self.capacity:
            # Append new item to end of buffer
            self.storage.add_to_tail(item)
            # Set the current element to the newly added tail element
            self.current = self.storage.tail
        # If length of storage is equal to the capacity
        if self.storage.length == self.capacity:
            # Set the current value equal to the item
            self.current.value = item
            # Check if current is equal to tail
            if self.current == self.storage.tail:
                # If it is set current to the head value to start over writing the oldest in the storage
                self.current = self.storage.head
            else:
                # Otherwise change current to the next node
                self.current = self.current.next

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []


        # Get the current head
        current_node = self.storage.head
        # While there is a current_node
        while current_node:
            # Append current node value to list
            list_buffer_contents.append(current_node.value)
            # Set the current node to the next node
            current_node = current_node.next
        return list_buffer_contents

# ----------------Stretch Goal-------------------

buffer = RingBuffer(5)
buffer.append(1)
buffer.append(2)
buffer.append(3)
buffer.append(4)
buffer.append(5)
buffer.append(6)
buffer.append(7)

print(buffer.storage.length)
print(buffer.get())

class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
