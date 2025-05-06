"""
Stack Implementation Using Linked List

This module implements a Stack data structure using a LinkedList.
A stack is a linear data structure that follows the Last In First Out (LIFO) principle.

Operations:
- push: Add an element to the top of the stack
- pop: Remove the top element from the stack

Time Complexity:
- Push: O(1)
- Pop: O(1)

Space Complexity: O(n) where n is the number of elements in the stack
"""
from typing import Optional, Any, TypeVar

T = TypeVar('T')  # Define a type variable for generic typing


class Element:
    """
    A class representing an element in a linked list.

    Attributes:
        value: The value stored in the element
        next: Reference to the next element in the linked list
    """
    def __init__(self, value: Any):
        """
        Initialize a new Element with a value.

        Args:
            value: The value to be stored in the element
        """
        self.value = value
        self.next: Optional['Element'] = None


class LinkedList:
    """
    A class representing a singly linked list.

    Attributes:
        head: Reference to the first element in the linked list
    """
    def __init__(self, head: Optional[Element] = None):
        """
        Initialize a new LinkedList with an optional head element.

        Args:
            head: The first element of the linked list (default: None)
        """
        self.head: Optional[Element] = head

    def append(self, new_element: Element) -> None:
        """
        Append a new element to the end of the linked list.

        Args:
            new_element: The element to append
        """
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def insert_first(self, new_element: Element) -> None:
        """
        Insert a new element as the head of the LinkedList.

        Args:
            new_element: The element to insert at the beginning
        """
        # Fetch the current head
        current = self.head
        new_element.next = current
        self.head = new_element

    def delete_first(self) -> Optional[Element]:
        """
        Delete the first (head) element in the LinkedList and return it.

        Returns:
            The deleted element or None if the list is empty
        """
        current = self.head
        if current:
            if current.next:
                self.head = current.next
            else:
                self.head = None
            return current
        else:
            return None


class Stack:
    """
    A class representing a Stack data structure implemented using a LinkedList.

    Attributes:
        ll: The LinkedList used to store the stack elements
    """
    def __init__(self, top: Optional[Element] = None):
        """
        Initialize a new Stack with an optional top element.

        Args:
            top: The element to be placed at the top of the stack (default: None)
        """
        self.ll = LinkedList(top)

    def push(self, new_element: Element) -> None:
        """
        Push (add) a new element onto the top of the stack.

        Args:
            new_element: The element to push onto the stack
        """
        self.ll.insert_first(new_element)

    def pop(self) -> Optional[Element]:
        """
        Pop (remove) the first element off the top of the stack and return it.

        Returns:
            The element removed from the top of the stack or None if the stack is empty
        """
        return self.ll.delete_first()

    def is_empty(self) -> bool:
        """
        Check if the stack is empty.

        Returns:
            True if the stack is empty, False otherwise
        """
        return self.ll.head is None


if __name__ == "__main__":
    # Test cases
    # Set up some Elements
    e1 = Element(1)
    e2 = Element(2)
    e3 = Element(3)
    e4 = Element(4)

    # Start setting up a Stack
    stack = Stack(e1)

    # Test stack functionality
    stack.push(e2)
    stack.push(e3)
    print(f"Pop: {stack.pop().value}")
    print(f"Pop: {stack.pop().value}")
    print(f"Pop: {stack.pop().value}")

    # Test empty stack
    empty_result = stack.pop()
    print(f"Pop from empty stack: {empty_result}")

    # Test pushing after empty
    stack.push(e4)
    print(f"Pop after pushing to empty stack: {stack.pop().value}")

    # Test is_empty method
    print(f"Is stack empty? {stack.is_empty()}")
