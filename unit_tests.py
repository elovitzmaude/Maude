import unittest
import Task
import SLPriorityQueue

#create class for the tests
class PQTests(unittest.TestCase):

    def test_create_priorityqueue(self):
        #Testing if the SLPriorityQueue is created and initialized correctly and if the size is 0 and the queue is empty.
        pq = SLPriorityQueue.PriorityQueue() #initializing the queue
        self.assertIsInstance(pq, SLPriorityQueue.PriorityQueue) #assertion statement that the queue exists
        self.assertTrue(pq.is_empty(), "queue should be empty, but is_empty() says it is not") #assertion statement that the queue is empty
        self.assertTrue(pq.size() == 0, "queue should have a size of 0, but size() is not 0") #assertion statement that the size is 0

    def test_size_1(self):
        #Testing if the size function works when enqueuing one item to the priority queue
        pq = SLPriorityQueue.PriorityQueue()
        a =  Task.Task("2022-04-15", 3, "lab due") #initializing the queue
        pq.enqueue(a) #enqueuing an item into the priority queue
        self.assertTrue(pq.size() == 1, "size should be 1 after enqueuing one task into the queue") #assertion statement that the size is 1 after enqueuing one task

    def test_size_many(self):
        #Testing if the size function works after enqueuing multiple tasks to the priority queue
        pq = SLPriorityQueue.PriorityQueue()  #initializing the queue
        a = Task.Task("2022-04-05", 3, "lab due")
        b = Task.Task("2021-04-06", 2, "homework due")
        c = Task.Task("2020-03-09", 1, "taxes due")
        d = Task.Task("2023-09-02", 5, "bills due")
        pq.enqueue(a) #enqueuing a task into the priority queue
        pq.enqueue(b)  #enqueuing a task into the priority queue
        pq.enqueue(c)  #enqueuing a task into the priority queue
        pq.enqueue(d)  #enqueuing a task into the priority queue
        self.assertTrue(pq.size() == 4, "size should be 4 after enqueuing four tasks into the queue") #assertion statement that the size is 4 after enqueuing four tasks
    
    def test_isNOTempty(self):
        #Testing if the is_empty function works after enqueuing multiple tasks into the priority queue
        pq = SLPriorityQueue.PriorityQueue() #initializing the queue
        a = Task.Task("2022-04-05", 3, "lab due")
        b = Task.Task("2021-04-06", 2, "homework due")
        c = Task.Task("2020-03-09", 1, "taxes due")
        d = Task.Task("2023-09-02", 5, "bills due")
        pq.enqueue(a) #enqueuing a task into the priority queue
        pq.enqueue(b)  #enqueuing a task into the priority queue
        pq.enqueue(c)  #enqueuing a task into the priority queue
        pq.enqueue(d)  #enqueuing a task into the priority queue
        self.assertFalse(pq.is_empty(), "queue should be not be empty, but is_empty() says it is") #assertion statement that the queue is not empty

    def test_enqueue_1(self):
        #Testing if the enqueue function works with 1 task and that the size increases after enqueueing 1 task.
        pq = SLPriorityQueue.PriorityQueue() #initializing the queue
        a = Task.Task("2022-04-05", 3, "lab due")
        pq.enqueue(a) #enqueuing a task into the priority queue
        self.assertEqual(str(pq.first()), "2022-04-05, 3: lab due", "the first item in the queue should be the highest priority item, but first() says it is not") #verifying that the first item in the queue is the highest priority item
        self.assertTrue(pq.size() == 1, "size should be 1 after enqueuing one task into the queue") #assertion statement that the size is 1 after enqueuing one task  l

    def test_enqueue_2(self):
        #Testing if the enqueue function works with 2 tasks and that the size increases after enqueueing 2 tasks.
        pq = SLPriorityQueue.PriorityQueue()  #initializing the queue
        a = Task.Task("2022-04-05", 3, "lab due")
        b = Task.Task("2021-04-06", 2, "homework due")
        pq.enqueue(a) #enqueuing a task into the priority queue
        pq.enqueue(b) #enqueuing a task into the priority queue
        self.assertEqual(str(pq.first()), "2021-04-06, 2: homework due", "the first item in the queue should be the highest priority item, but first() says it is not") #verifying that the first item in the queue is the highest priority item
        self.assertTrue(pq.size() == 2, "size should be 2 after enqueuing two tasks into the queue") #assertion statement that the size is 2 after enqueuing two tasks
        self.assertFalse(pq.is_empty(), "queue should be not be empty, but is_empty() says it is") #assertion statement that the queue is not empty 
    
    def test_enqueue_4_reverseorder(self):
        #Testing if the enqueue function works with 4 tasks that are enqueued in reverse order and that the size increases after enqueueing 4 tasks.
        pq = SLPriorityQueue.PriorityQueue()  #initializing the queue
        a = Task.Task("2023-04-05", 3, "lab due")
        b = Task.Task("2022-04-06", 2, "homework due")
        c = Task.Task("2021-03-09", 1, "taxes due")
        d = Task.Task("2020-09-02", 5, "bills due")
        pq.enqueue(a) #enqueuing a task into the priority queue
        pq.enqueue(b) #enqueuing a task into the priority queue
        pq.enqueue(c) #enqueuing a task into the priority queue
        pq.enqueue(d)
        self.assertEqual(str(pq.first()), "2020-09-02, 5: bills due", "the first item in the queue should be the highest priority item, but first() says it is not") #verifying that the first item in the queue is the highest priority item
        self.assertEqual(str(pq), "2020-09-02, 5: bills due, 2021-03-09, 1: taxes due, 2022-04-06, 2: homework due, 2023-04-05, 3: lab due", "string function is not working properly.")
        self.assertTrue(pq.size() == 4, "size should be 4 after enqueuing four tasks into the queue") #assertion statement that the size is 4 after enqueuing four tasks
        self.assertFalse(pq.is_empty(), "queue should be not be empty, but is_empty() says it is") #assertion statement that the queue is not empty

    def test_enqueue_4_rightorder(self):
        #Testing if the enqueue function works with 4 tasks and that are enqueued in the right order the size increases after enqueueing 4 tasks.
        pq = SLPriorityQueue.PriorityQueue()  #initializing the queue
        a = Task.Task("2020-04-05", 3, "lab due")
        b = Task.Task("2021-04-06", 2, "homework due")
        c = Task.Task("2022-03-09", 1, "taxes due")
        d = Task.Task("2023-09-02", 5, "bills due")
        pq.enqueue(a) #enqueuing a task into the priority queue
        pq.enqueue(b) #enqueuing a task into the priority queue
        pq.enqueue(c) #enqueuing a task into the priority queue
        pq.enqueue(d) #enqueuing a task into the priority queue
        self.assertEqual(str(pq.first()), "2020-04-05, 3: lab due", "the first item in the queue should be the highest priority item, but first() says it is not") #verifying that the first item in the queue is the highest priority item
        self.assertEqual(str(pq), "2020-04-05, 3: lab due, 2021-04-06, 2: homework due, 2022-03-09, 1: taxes due, 2023-09-02, 5: bills due", "string function is not working properly.")
        self.assertTrue(pq.size() == 4, "size should be 4 after enqueuing four tasks into the queue") #assertion statement that the size is 4 after enqueuing four tasks
        self.assertFalse(pq.is_empty(), "queue should be not be empty, but is_empty() says it is") #assertion statement that the queue is not empty

    def test_enqueue_4_randomorder(self):
        #Testing if the enqueue function works with 4 tasks and that are in random order and that the size increases after enqueueing 4 tasks.
        pq = SLPriorityQueue.PriorityQueue()  #initializing the queue
        a = Task.Task("2020-04-05", 3, "lab due")
        b = Task.Task("2021-04-06", 2, "homework due")
        c = Task.Task("2022-03-09", 1, "taxes due")
        d = Task.Task("2023-09-02", 5, "bills due")
        pq.enqueue(a) #enqueuing a task into the priority queue
        pq.enqueue(d) #enqueuing a task into the priority queue
        pq.enqueue(c) #enqueuing a task into the priority queue
        pq.enqueue(b) #enqueuing a task into the priority queue
        self.assertEqual(str(pq.first()), "2020-04-05, 3: lab due", "the first item in the queue should be the highest priority item, but first() says it is not") #verifying that the first item in the queue is the highest priority item
        self.assertEqual(str(pq), "2020-04-05, 3: lab due, 2021-04-06, 2: homework due, 2022-03-09, 1: taxes due, 2023-09-02, 5: bills due", "string function is not working properly.")
        self.assertTrue(pq.size() == 4, "size should be 4 after enqueuing four tasks into the queue") #assertion statement that the size is 4 after enqueuing four tasks
        self.assertFalse(pq.is_empty(), "queue should be not be empty, but is_empty() says it is") #assertion statement that the queue is not empty
    
    def test_enqueue_4_samedata(self):
        #Testing if the enqueue function works with 4 tasks that all have the same date and same priority.
        pq = SLPriorityQueue.PriorityQueue()  #initializing the queue
        a = Task.Task("2020-04-05", 3, "lab due")
        b = Task.Task("2020-04-05", 3, "homework due")
        c = Task.Task("2020-04-05", 3, "taxes due")
        d = Task.Task("2020-04-05", 3, "bills due")
        pq.enqueue(a) #enqueuing a task into the priority queue
        pq.enqueue(b) #enqueuing a task into the priority queue
        pq.enqueue(c) #enqueuing a task into the priority queue
        pq.enqueue(d) #enqueuing a task into the priority queue
        self.assertEqual(str(pq.first()), "2020-04-05, 3: lab due", "the first item in the queue should be the highest priority item, but first() says it is not") #verifying that the first item in the queue is the highest priority item
        self.assertEqual(str(pq), "2020-04-05, 3: lab due, 2020-04-05, 3: homework due, 2020-04-05, 3: taxes due, 2020-04-05, 3: bills due", "string function is not working properly.")
        self.assertTrue(pq.size() == 4, "size should be 4 after enqueuing four tasks into the queue") #assertion statement that the size is 4 after enqueuing four tasks
        self.assertFalse(pq.is_empty(), "queue should be not be empty, but is_empty() says it is") #assertion statement that the queue is not empty

    def test_enqueue_samedate(self):
        #Testing if the enqueue function works with 2 tasks when the tasks have the same date and different priorities
        pq = SLPriorityQueue.PriorityQueue() #initializing the queue
        a = Task.Task("2022-04-05", 3, "lab due")
        b = Task.Task("2022-04-05", 2, "homework due")
        pq.enqueue(a) #enqueuing a task into the priority queue
        pq.enqueue(b) #enqueuing a task into the priority queue 
        self.assertEqual(str(pq.first()), "2022-04-05, 2: homework due", "the first item in the queue should be the highest priority item, but first() says it is not") #verifying that the first item in the queue is the highest priority item 
        self.assertTrue(pq.size() == 2, "size should be 2 after enqueuing two tasks into the queue") #assertion statement that the size is 2 after enqueuing two tasks
        self.assertFalse(pq.is_empty(), "queue should be not be empty, but is_empty() says it is") #assertion statement that the queue is not empty

    def test_dequeue_1(self):
        #Tests that dequeue works after enqueuing 1 task to the priority queue
        pq = SLPriorityQueue.PriorityQueue() #initializing the queue
        a = Task.Task("2022-04-05", 3, "lab due")
        pq.enqueue(a) #enqueuing a task into the priority queue
        self.assertEqual(str(pq.dequeue()), "2022-04-05, 3: lab due", "dequeue() should remove and return the highest priority task in the queue first")  #verifying that dequeue removes and returns the highest priority task in the queue   
        self.assertTrue(pq.is_empty(), "queue should be empty after dequeuing one task, but is_empty() says it is not") #assertion statement that the queue is empty after dequing one task
        self.assertTrue(pq.size() == 0, "size should be 0 after dequeuing all of the tasks from the queue") #assertion statement that the size is 0 after dequeuing all of the tasks

    def test_dequeue_from_multiple(self):
        #Tests that dequeue works after enqueuing more than 1 task to the priority queue, and removes and returns the correct highest priority task 
        pq = SLPriorityQueue.PriorityQueue() #initializing the queue
        a = Task.Task("2022-04-05", 3, "lab due")
        b = Task.Task("2021-04-06", 2, "homework due")
        c = Task.Task("2020-03-09", 1, "taxes due")
        d = Task.Task("2023-09-02", 5, "bills due")
        pq.enqueue(a) #enqueuing a task into the priority queue
        pq.enqueue(b) #enqueuing a task into the priority queue
        pq.enqueue(c) #enqueuing a task into the priority queue
        pq.enqueue(d) #enqueuing a task into the priority queue
        self.assertEqual(str(pq.dequeue()), "2020-03-09, 1: taxes due", "dequeue() should remove and return the highest priority task in the queue first")  #verifying that dequeue removes and returns the highest priority task in the queue
        self.assertFalse(pq.is_empty(), "queue should be not be empty after dequeuing one task from a queue with multiple tasks, but is_empty() says it is") #assertion statement that the queue is not empty after dequing one task when there are still tasks in the queue
        self.assertTrue(pq.size() == 3, "size should be 3 after dequeuing 1 task from the queue") #assertion statement that the size is 3 after dequeuing only one of the tasks

    def test_dequeue_all(self):
        #Tests that dequeue works after enqueuing more than 1 task to the priority queue and dequeuing all of the tasks 
        pq = SLPriorityQueue.PriorityQueue() #initializing the queue
        a = Task.Task("2022-04-05", 3, "lab due")
        b = Task.Task("2020-04-06", 2, "homework due")
        c = Task.Task("2021-03-09", 1, "taxes due")
        d = Task.Task("2023-09-02", 5, "bills due")
        pq.enqueue(a) #enqueuing a task into the priority queue
        pq.enqueue(b) #enqueuing a task into the priority queue
        pq.enqueue(c) #enqueuing a task into the priority queue
        pq.enqueue(d) #enqueuing a task into the priority queue
        self.assertEqual(str(pq.dequeue()), "2020-04-06, 2: homework due", "dequeue() should remove and return the highest priority task in the queue first")  #verifying that dequeue removes and returns the highest priority task in the queue   
        self.assertEqual(str(pq.dequeue()), "2021-03-09, 1: taxes due", "dequeue() should remove and return the highest priority task in the queue first")  #verifying that dequeue removes and returns the highest priority task in the queue
        self.assertEqual(str(pq.dequeue()), "2022-04-05, 3: lab due", "dequeue() should remove and return the highest priority task in the queue first")  #verifying that dequeue removes and returns the highest priority task in the queue
        self.assertEqual(str(pq.dequeue()), "2023-09-02, 5: bills due", "dequeue() should remove and return the highest priority task in the queue first")  #verifying that dequeue removes and returns the highest priority task in the queue
        self.assertTrue(str(pq.is_empty()), "queue should be empty after dequeuing one task, but is_empty() says it is not") #assertion statement that the queue is empty after dequing one task 
        self.assertTrue(pq.size() == 0, "size should be 0 after dequeuing all of the tasks from the queue") #assertion statement that the size is 0 after dequeuing all of the tasks

    def test_dequeue_all_add_1(self):
        #Tests that dequeue works after enqueuing more than 1 task to the priority queue and dequeuing all of the tasks
        pq = SLPriorityQueue.PriorityQueue() #initializing the queue
        a = Task.Task("2022-04-05", 3, "lab due")
        b = Task.Task("2020-04-06", 2, "homework due")
        c = Task.Task("2021-03-09", 1, "taxes due")
        d = Task.Task("2023-09-02", 5, "bills due")
        pq.enqueue(a) #enqueuing a task into the priority queue
        pq.enqueue(b) #enqueuing a task into the priority queue
        pq.enqueue(c) #enqueuing a task into the priority queue
        pq.enqueue(d) #enqueuing a task into the priority queue
        self.assertEqual(str(pq.dequeue()), "2020-04-06, 2: homework due", "dequeue() should remove and return the highest priority task in the queue first")  #verifying that dequeue removes and returns the highest priority task in the queue   
        self.assertEqual(str(pq.dequeue()), "2021-03-09, 1: taxes due", "dequeue() should remove and return the highest priority task in the queue first")  #verifying that dequeue removes and returns the highest priority task in the queue
        self.assertEqual(str(pq.dequeue()), "2022-04-05, 3: lab due", "dequeue() should remove and return the highest priority task in the queue first")  #verifying that dequeue removes and returns the highest priority task in the queue
        self.assertEqual(str(pq.dequeue()), "2023-09-02, 5: bills due", "dequeue() should remove and return the highest priority task in the queue first")  #verifying that dequeue removes and returns the highest priority task in the queue
        a = Task.Task("2022-07-12", 2, "notes due")
        pq.enqueue(a)
        self.assertFalse(pq.is_empty(), "queue should be not be empty after dequeuing one task from a queue with multiple tasks, but is_empty() says it is") #assertion statement that the queue is not empty after dequing one task when there are still tasks in the queue 
        self.assertTrue(pq.size() == 1, "size should be 1 after enqueuing a task to the queue") #assertion statement that the size is 1 after enqueuing one tasks
    
    def test_dequeue_samedate_samepriority(self):
        #Testing if the dequeue function returns the task that was entered first man4when 2 tasks with the same date and same priority are enqueued.
        pq = SLPriorityQueue.PriorityQueue() #initializing the queue
        a = Task.Task("2022-04-05", 3, "lab due")
        b = Task.Task("2022-04-05", 3, "homework due")
        pq.enqueue(a) #enqueuing a task into the priority queue
        pq.enqueue(b) #enqueuing a task into the priority queue 
        self.assertEqual(str(pq.dequeue()), "2022-04-05, 3: lab due", "dequeue() should remove and return the highest priority task in the queue first")  #verifying that dequeue removes and returns the highest priority task in the queue  
        self.assertTrue(pq.size() == 1, "size should be 1 after dequeuing 1 task from the queue") #assertion statement that the size is 1 after dequeuing only one of the tasks
        self.assertFalse(pq.is_empty(), "queue should be not be empty after dequeuing one task from a queue with multiple tasks, but is_empty() says it is") #assertion statement that the queue is not empty after dequing one task when there are still tasks in the queue

    def test_string_1(self):
        #Testing if the string function works with 1 task.
        pq = SLPriorityQueue.PriorityQueue() #initializing the queue
        a = Task.Task("2022-04-05", 3, "lab due")
        pq.enqueue(a) #enqueuing a task into the priority queue
        self.assertEqual(str(pq), "2022-04-05, 3: lab due", "the string is inncorrect") #verifying that the first item in the queue is the highest priority item


    def test_string_2(self):
        #Testing if the enqueue function works with 2 tasks and that the size increases after enqueueing 2 tasks.
        pq = SLPriorityQueue.PriorityQueue()  #initializing the queue
        a = Task.Task("2022-04-05", 3, "lab due")
        b = Task.Task("2021-04-06", 2, "homework due")
        pq.enqueue(a) #enqueuing a task into the priority queue
        pq.enqueue(b) #enqueuing a task into the priority queue
        self.assertEqual(str(pq), "2021-04-06, 2: homework due, 2022-04-05, 3: lab due", "the string is inncorrect") #verifying that the first item in the queue is the highest priority item

    def test_string_4(self):
        #Testing if the enqueue function works with 4 tasks and that are enqueued in the right order the size increases after enqueueing 4 tasks.
        pq = SLPriorityQueue.PriorityQueue()  #initializing the queue
        a = Task.Task("2020-04-05", 3, "lab due")
        b = Task.Task("2021-04-06", 2, "homework due")
        c = Task.Task("2022-03-09", 1, "taxes due")
        d = Task.Task("2023-09-02", 5, "bills due")
        pq.enqueue(a) #enqueuing a task into the priority queue
        pq.enqueue(b) #enqueuing a task into the priority queue
        pq.enqueue(c) #enqueuing a task into the priority queue
        pq.enqueue(d) #enqueuing a task into the priority queue
        self.assertEqual(str(pq), "2020-04-05, 3: lab due, 2021-04-06, 2: homework due, 2022-03-09, 1: taxes due, 2023-09-02, 5: bills due", "string function is not working properly.")
        
unittest.main()
