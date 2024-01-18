class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def getIntersectionNode(headA, headB):
    def getLength(node):
        length = 0
        while node:
            length += 1
            node = node.next
        return length

    lenA, lenB = getLength(headA), getLength(headB)

    # Adjust starting points for longer linked list
    while lenA > lenB:
        headA = headA.next
        lenA -= 1

    while lenB > lenA:
        headB = headB.next
        lenB -= 1

    # Move both pointers until intersection or end is reached
    while headA and headB:
        if headA == headB:
            return headA
        headA = headA.next
        headB = headB.next

    return None

# Example usage:
# Create linked lists A and B
A = ListNode(1, ListNode(2))
common = ListNode(3, ListNode(4, ListNode(5)))
B = ListNode(6, ListNode(7, common))

# Connect the common part to both linked lists
A.next.next = common
B.next.next.next = common

# Find the intersection node
intersection_node = getIntersectionNode(A, B)

if intersection_node:
    print("Intersection node value:", intersection_node.value)
else:
    print("No intersection")
