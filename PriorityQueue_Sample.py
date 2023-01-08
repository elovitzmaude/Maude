import SLNode

class PriorityQueue:
    def __init__(self):
      self._front = None
      self._rear = None
      self._length = 0

    def size(self):
        return (self._length)

    def is_empty(self):
        return (self._length == 0)

    def enqueue(self, item):
        newNode = SLNode.SLNode(item)
        if self.is_empty():
            newNode.set_next(self._front)
            self._front = newNode
            self._rear = newNode
            self._length += 1
        
        else:
            if newNode.get_data() < self._front.get_data():
                if self._length == 1:
                    newNode.set_next(self._front)
                    self._rear = self._front
                    self._front = newNode
                    self._length += 1
                    
                else:
                    newNode.set_next(self._front)
                    self._front = newNode
                    self._length += 1
                    
            else:
                if newNode.get_data() >= self._rear.get_data():
                    self._rear.set_next(newNode)
                    self._rear = newNode
                    self._length += 1
                    
                else:
                    temp = self._front
                    temp_next = self._front.get_next()
                    while temp.get_data() <= newNode.get_data() and temp_next.get_data() <= newNode.get_data():
                        temp = temp.get_next()
                        temp_next = temp_next.get_next()
                    
                    if temp.get_data() <= newNode.get_data() and temp_next.get_data() >= newNode.get_data():
                        newNode.set_next(temp_next)
                        temp.set_next(None)
                        temp.set_next(newNode)
                        self._length += 1

    def dequeue(self):
        if self.is_empty():
            return None
        data = self._front.get_data()
        self._front = self._front.get_next()
        self._length -= 1

        if (self._length == 0 ):
            self._front = None
            self._rear = None
        return(data)

    def first(self):
        if self.is_empty():
            return None
        temp = self._front.get_data()
        return temp

    def __str__(self):
        temp = self._front 
        temp_queue = ""
        count = 0
        while temp != None:
            if count == 0:
                temp_queue = str(str(temp.get_data()))
                temp = temp.get_next()
                count += 1
            else:
                temp_queue= str(str(temp_queue) + ", " + str(temp.get_data())) 
                temp = temp.get_next()
        return(temp_queue)
