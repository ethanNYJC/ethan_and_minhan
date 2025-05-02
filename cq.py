############################### 72 chars ###############################


class CircularQueue:
    """
    Circular Queue implemented as Array.

    Methods
    -------
    - enqueue(item)
      Adds item at the end of the queue.
    
    - dequeue()
      Returns the first item in the queue.
    """

    def __init__(self, size: int):
        self.size = size
        self.head = -1
        self.tail = 0
        self.queue = [0] * size

    def __repr__(self) -> str:
        return f"CircularQueue({self.size})"

    def enqueue(self, data) -> None:
        """
        Add item at the end of the queue.

        Arguments
        ---------
        - item
          The item to be added.

        Return: None
        """
        if self.tail == -1:
          #if the queue is previously full already
          print("Queue is full, unable to enqueue")
          return
        
        self.queue[self.tail] = data
        self.tail = (self.tail + 1) % self.size
        if self.head == -1:
          self.head = (self.head + 1) % self.size
        elif self.tail == self.head:
          #if the queue is full after incrementing
            self.tail = -1
        
        
    def dequeue(self) -> "item":
        """
        Return the item at the head of the queue.

        Arguments
        ---------
        None

        Return: item
        """
        if self.head == -1:
          print("Queue is empty, unable to dequeue")
          return
        else:
          item = self.queue[self.head]
          self.queue[self.head] = 0
          self.head = (self.head + 1) % self.size
          if self.head == self.tail:
            #case if the length of queue is 1, so head index == tail index
            self.head = -1
          return item
          

if __name__ == "__main__":
  cq = CircularQueue(5)
  cq.enqueue("a")
  cq.enqueue("b")
  cq.enqueue("c")
  cq.dequeue()
  cq.dequeue()
  cq.enqueue("a")
  print(cq.queue)