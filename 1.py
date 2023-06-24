class Node:
    def __init__(self, data):
        self.value = data
        self.next = None


nd1 = Node('A')
nd2 = Node('B')
nd3 = Node('C')

nd1.next = nd2
nd2.next = nd3

current = nd1
next = None
prev = None

while current != None:
    next = current.next
    current.next = prev
    prev = current
    current = next

reversedList = prev

while reversedList != None:
    print(reversedList.value, end=' ')
    reversedList = reversedList.next
