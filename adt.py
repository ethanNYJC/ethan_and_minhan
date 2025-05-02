############################### 72 chars ###############################

from datastruct import LinkedList
from datastruct import Node


class Empty(Exception):
    """
    Error raised when trying to pop/dequeue items from an empty
    Stack/Queue.
    """
    def __init__(self, msg="IndexError: list is empty"):
        self.msg = msg
        
    def __str__(self):
        return f'{self.msg}'


class Stack(LinkedList):
    """
    Implements the Stack ADT using a linkedlist.

    Arguments
    ---------
    None

    Methods
    -------
    - push(item) -> None
    - pop() -> item
    """

    def __repr__(self) -> str:
        return 'Stack()'

    def push(self, item) -> None:
        """
        Pushes item onto the top of the stack.

        Arguments
        ---------
        - item
          The item to be pushed.

        Returns: None
        """
        new_node = Node(item)
        if self._head == None:
            self._head = new_node
            return
        else:
          current = self.get(self.length()-1)
          current.next = new_node
          return
            

    def pop(self) -> "item":
        """
        Pops item off the top of the stack, and returns it.

        Arguments
        ---------
        None

        Returns: item

        Raises: Empty - if stack is already empty
        """
        if self._head == None:
            print("cannot pop from an empty list")
            return
        else: 
            if self.length() > 1:
                current = self.get(self.length()-2)
                popped = self.get(self.length()-1)
                current.next = None
                return popped
            else:
                current = self._head
                self._head = None
                return current
            
            

    def printStack(self):
        if self._head == None:
            print("Stack is empty")
            return
        temp = self._head
        stack_string = "Current Queue: "
        while temp is not None:
            stack_string += str(temp._data) + " "
            temp = temp.next
        print(stack_string)


# Queue can also inherit from Array
class Queue(LinkedList):
    """
    Implements the Queue ADT using a linkedlist.

    Arguments
    ---------
    None

    Methods
    -------
    - enqueue(item) -> None
    - dequeue() -> item
    """

    def __repr__(self) -> str:
        return 'Queue()'

    def enqueue(self, item) -> None:
        """
        Enqueues item into the end of the queue.

        Arguments
        ---------
        - item
          The item to be enqueued.

        Returns: None
        """
        # Replace the line below with your code
        if self._head == None:
            self._head = Node(item)
        else:
            new_node = Node(item)
            current = self.get(self.length() - 1)
            current.next = new_node

    def dequeue(self) -> "item":
        """
        Dequeues item from the front of the queue, and returns it.

        Arguments
        ---------
        None

        Returns: item

        Raises: Empty - if queue is already empty
        """
        if self._head == None:
            print("cannot dequeue from empty list")
            return
        else:
            if self.length() > 1:
                poppednode = self._head
                self._head = self._head.next
                return poppednode
            else:
                poppednode = self._head
                self._head = None
                return poppednode
                
    def printQueue(self):
        if self._head == None:
            print("Queue is empty")
            return
        temp = self._head
        queue_string = "Current Queue: "
        while temp is not None:
            queue_string += str(temp._data) + " "
            temp = temp.next
        print(queue_string)

if __name__ == "__main__":
    

    queue = Queue()
    queue.enqueue("a")
    queue.enqueue("b")
    queue.enqueue("c")
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.printQueue()