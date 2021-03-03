def deleteDuplicates(head):
    current = head

    while current != None and current.next != None:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next

    return head


list = [1, 1, 2, 3, 3]

print(deleteDuplicates(list))