"""Return reference of new head of the reverse linked list
  The input list will have at least one element
  Node is defined as

class Node:
    def __init__(self, data):
		self.data = data
		self.next = None
  This is method only submission.
  You only need to complete the method.
"""
def reverse(head, k):
    
    def reverseList(head):
        prev = None
        current = head
        tail = head
        while(current is not None):
            next = current.next
            current.next = prev 
            prev = current 
            current = next
        head = prev
        return head, tail

    old_tail = head
    cur_tail = head
    cur_head = head
    new_head = head
    j = 0

    while(True):

        for i in range(k-1):
            if cur_tail.next != None:
                cur_tail = cur_tail.next
            else:
                break

        new_head = cur_tail.next

        cur_tail.next = None

        cur_head, cur_tail = reverseList(cur_head)

        if j==0:
            master_head = cur_head
            j+=1
        else:
            old_tail.next = cur_head 

        old_tail = cur_tail
        cur_tail = new_head
        cur_head = new_head

        if new_head == None:
            break

    return master_head

#{ 
#  Driver Code Starts
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        # self.tail

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            # arr.append(str(temp.data))
            temp = temp.next
        print()

if __name__ == '__main__':
    t = int(input())
    while (t > 0):
        llist = LinkedList()
        n = input()
        values = list(map(int, input().split()))
        for i in reversed(values):
            llist.push(i)
        k = int(input())
        new_head = LinkedList()
        new_head = reverse(llist.head, k)
        llist.head = new_head
        llist.printList()
        t -= 1




# } Driver Code Ends