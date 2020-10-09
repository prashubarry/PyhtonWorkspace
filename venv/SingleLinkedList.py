"""
LinkedList
using python
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Insertion using linked List
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insertAfter(self, prev_node, new_data):
        if prev_node is None:
            print("The given previous node must be in the LinkedList")
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while (last.next):
            last = last.next
        last.next = new_node

    def deleteNode(self, key):
        temp = self.head

        if (temp is not None):
            if (temp.data == key):
                self.head = temp.next
                temp = None
                return
        while (temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        if (temp == None):
            return

        prev.next = temp.next
        temp = None

    def deleteNodePosition(self, position):
        if self.head == None:
            return
        temp = self.head
        if position == 1:
            self.head = temp.next
            temp = None
            return
        # Find previous node of the node to be deleted
        for i in range(position - 1):
            temp = temp.next
            if temp is None:
                break
        if temp is None:
            return
        if temp.next is None:
            return
        next = temp.next.next
        temp.next = None

        temp.next = next

    """
                Finding the length of the linked list
                1.Iterative Approach Function Name(getCountI)
                2.Recursive Approach Function Name(getCountR)
    """
    def getCountI(self):
        temp=self.head
        count=0
        while(temp):
            count+=1
            temp=temp.next
        return count
    def getCountRec(self,node):
        if not node:
            return 0
        else:
            return 1+self.getCountRec(node.next)
    def getCountR(self):
        return self.getCountRec(self.head)
    def searchS(self,x):
        temp=self.head
        while(temp):
            if temp.data==x:
                return True
            temp=temp.next

    def searchR(self,li,key):
        if not li:
            return False
        if li.data==key:
            return True
        return self.searchR(li.next,key)

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next


# Start of the execution----
if __name__ == '__main__':
    llist = LinkedList()
    print("Enter the number of nodes:")
    n = int(input())
    print("Enter the numbers:")
    l1 = list(map(int, input().rstrip().split()))[:n]
    print("Choose from the following:")
    for i in range(len(l1)):
        print("1.Insert at Beginning\n2.Insert after\n3.Append")
        sc = int(input())
        if sc == 1:
            llist.push(l1[i])
        elif sc == 2:
            print("Insert after:")
            n1 = int(input())
            llist.insertAfter(llist.head.next, n1)
        elif sc == 3:
            llist.append(l1[i])
        else:
            print("No valid choice")
    print("The single Linked List is:")
    llist.printList()
    print("Count of the nodes in the linked list(Iterative):",llist.getCountI())
    print("Count of the nodes in the linked list(Recursive):", llist.getCountR())
    print("Do you want to delete a node(Y/n):")
    sc1 = input()

    if sc1 == 'Y':
        print("Choose from the following:")
        print("1.SimpleDelete\n2.PositionDelete")
        sc3 = int(input())
        if sc3 == 1:
            print("Enter the node no. you want to delete:")
            n2 = int(input())
            llist.deleteNode(n2)
            print("New Single Linked List:")
            llist.printList()
            print("Count of the nodes in the linked list(Iterative):", llist.getCountI())
            print("Count of the nodes in the linked list(Recursive):", llist.getCountR())
        elif sc3 == 2:
            print("Enter the node position you want to delete:")
            n2 = int(input())
            llist.deleteNodePosition(n2)
            print("New Single Linked List:")
            llist.printList()
            print("Count of the nodes in the linked list(Iterative):", llist.getCountI())
            print("Count of the nodes in the linked list(Recursive):", llist.getCountR())
    else:
        print("No Change in the original list:")
        llist.printList()
        print("Count of the nodes in the linked list(Iterative):", llist.getCountI())
        print("Count of the nodes in the linked list(Recursive):", llist.getCountR())
    """
    Search an element in a linked list
    """
    print("You want to search something in the linked list(Y/n):")
    choice=input()

    if choice == 'Y':
        print("The element to be searched:")
        n4=int(input())
        if llist.searchS(n4):
            print("Yes")
        else:
            print("No")




