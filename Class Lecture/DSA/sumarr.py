# num = int(input("Enter How many numbers you write in the List :\n"))
# lst =[]
# for  i in range (num):
#     n = int(input("Enter the numbers:"))
#     lst.append(n)
# largest =lst[0]
# for i in lst:
#     if i > largest:
#         largest = i

# print(largest)

# second_largest = lst[0]
# for i in lst:
#     if i > second_largest:
#         if i != largest:
#             second_largest = i
        


class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def insert(self, new_node, pos):
        if pos < 1:
            return

        if pos == 1:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head
        p = 1

        while temp and p < pos - 1:
            temp = temp.next
            p += 1

        if temp is None:
            return

        new_node.next = temp.next
        temp.next = new_node

    def middle(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        if slow:
            print("Middle node:", slow.data)

    def del_node(self, value):
        temp = self.head

        if temp is None:
            return

        if temp.data == value:
            self.head = temp.next
            return

        prev = temp
        temp = temp.next

        while temp:
            if temp.data == value:
                prev.next = temp.next
                return

            prev = temp
            temp = temp.next

        print("Value is not in the list")

    def reverse(self):
        prev = None
        temp = self.head

        while temp:
            next_node = temp.next
            temp.next = prev
            prev = temp
            temp = next_node

        self.head = prev

    def sum(self):
        temp = self.head

        while temp and temp.next:
            total = temp.data + temp.next.data
            print(temp.data, "+", temp.next.data, "=", total)
            temp = temp.next

    def print_list(self):
        temp = self.head
        print("Linked list data")

        while temp:
            print(temp.data)
            temp = temp.next


list = LinkedList()

n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(50)

list.append(n1)
list.append(n2)
list.append(n3)
list.append(n4)

list.print_list()

print("List after insertion")
list.insert(Node(100), 3)
list.insert(Node(70), 4)
list.print_list()

print("Middle node:")
list.middle()

list.del_node(100)
print("Linked list after deleting")
list.print_list()

print("Reversed list")
list.reverse()
list.print_list()

print("Sum of consecutive pairs")
list.sum()
