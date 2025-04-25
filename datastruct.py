############################### 72 chars ###############################


class Node:
    """
    Represents a node in a linkedlist.
    
    Arguments
    ---------
    - data
      The data encapsulated in the node.

    Attributes
    ----------
    - next: Node | None
      The next node in the linkedlist, or None if the node is the tail.

    Methods
    -------
    - get() -> data
      Return the data stored in the node.
    """
    def __init__(self, data):
        self._data = data

    def __repr__(self) -> str:
        return f'Node({self.get()})'

    def get(self):
        return self._data


class LinkedList:
    """
    Represents a sequence of data items.

    Arguments
    ---------
    None

    Attributes
    ----------
    - head

    Methods
    -------
    - length() -> int
    - get(index) -> item
    - insert(index, item) -> None
    - append(item) -> None
    - delete(index) -> None
    """

    def __init__(self):
        self._head = None
        
    def __repr__(self) -> str:
        return 'LinkedList()'

    def length(self) -> int:
        """Returns the number of nodes in the linkedlist. 
        
        Arguments
        ---------
        None

        Return: int
        """
        # Replace the line below with your code
        size = 0
        if self.head:
            current = self.head
            while(current):
                current = current.next
                size += 1
            return size
        else:
          return 0

    def get(self, n: int) -> "item":
        """Returns item at n-th node.

        Arguments
        ---------
        - n: int
          sequence number of item to be retrieved.

        Returns: item

        Raises: IndexError if n > length
        """
        # Replace the line below with your code
        if n < self.length():
            current = self.head
            count = n
            while count > 0:
              current = current.next
              count -= 1
            return current
        else:
            raise IndexError

    def insert(self, n: int, item) -> None:
        """Insert item into linkedlist at position n.
        insert at head -> n == 0
        append -> n == length

        Arguments
        ---------
        - n: int
          sequence number of item to be inserted.

        Returns: None

        Raises: IndexError if n > length
        """
        # Replace the line below with your code
        if n > length():
            raise IndexError
        else:
            new_node = Node(item)
            current = self.get(n-1)
            new_node.next = current.next
            current.next = new_node

    def append(self, item) -> None:
        """Append item at the end of linkedlist.

        Arguments
        ---------
        - item
          The item to be appended.

        Returns: None
        """
        # Replace the line below with your code
        new_node = Node(item)
        if self._head = None:
            self._head = new_node
        else:
          current = self.get(self.length()-1)
          current.next = new_node

    def delete(self, n: int) -> None:
        """Delete n-th item from linkedlist.

        Arguments
        ---------
        - n: int
          sequence number of item to be retrieved.

        Returns: None

        Raises: IndexError if n > length
        """
        # Replace the line below with your code
        if n > length():
          raise IndexError
        else:
          current = self.get(n-1)
          prev = self.get(n-2)
          prev.next = current.next
          
       
    def contains(self, item) -> bool:
        """Checks whether an item is in the linkedlist and returns
        a boolean value to indicate the status of the search

        Arguments
        ---------
        - item
          The item to be searched for.

        Returns: True if item is found in the linkedlist,
        otherwise False
        """
        # Replace the line below with your code
        if self._head = None:
            return False
        else:
            current = self._head
            while current:
                current = current.next
                if current.get() == item:
                  return True
                else:
                  return False
        

if __name__ == "__main__":
    list1 = 