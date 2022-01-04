# HW8 task 1 - Stack, Queue
class Stack:

    def __init__(self) -> None:
        self.__stack = []

    def size(self):
        return len(self.__stack)

    def isEmpty(self):
        return self.size() == 0
        
    def peek(self):
        if self.isEmpty():
            return "Stack is empty!"
        return self.__stack[len(self.__stack) - 1]
         
    def push(self, new_element):
        self.__stack.append(new_element)

    def pop(self):
        if self.isEmpty():
            raise RuntimeError("Stack is empty!") 
        return self.__stack.pop()

    def __repr__(self) -> str:
        return f"It's a stack! Number of stack elements: {self.size()}"

    def __iter__(self):
        self.__counter = len(self.__stack)
        return self

    def __next__(self):
        if self.__counter > 0:
            self.__counter -= 1
            return self.__stack[self.__counter]
        else:
            raise StopIteration

class Queue:

    def __init__(self) -> None:
        self.__queue = []

    def size(self):
        return len(self.__queue)

    def isEmpty(self):
        return self.size() == 0
    
    def peek(self):
        if self.isEmpty():
            return "Queue is empty!"
        return self.__queue[0]
    
    def enqueue(self, new_element):
        self.__queue.append(new_element)

    def dequeue(self):
        if self.isEmpty():
            raise RuntimeError("Queue is empty!")
        return self.__queue.pop(0)
            
    def __repr__(self) -> str:
       return f"It's a queue! Number of queue items: {self.size()}"

    def __iter__(self):
        self.__counter = 0
        return self

    def __next__(self):
        try:
            while True:
                self.__counter += 1
                return self.__queue[self.__counter-1]
        except IndexError:
            raise StopIteration


if __name__ == "__main__":
    new_stack = Stack()
    for i in range(10):
        new_stack.push(i+1)
    print(new_stack)
    print(f"Peek a stack: {new_stack.peek()}")
    print("Iterate over the stack and see all the elements:")
    for item in new_stack:
        print(item)
    print("Pop all the elements of the stack:")
    for i in range(new_stack.size()):
        print(new_stack.pop())
    print("Try pop an element of the empty stack:")
    try:
        print(new_stack.pop())
    except RuntimeError as error:
        print(error) 

    new_queue = Queue()
    for i in range(10):
        new_queue.enqueue(i+1)
    print(new_queue)
    print(f"Peek a queue: {new_queue.peek()}")
    print("Iterate over the queue and see all the elements:")
    for item in new_queue:
        print(item)
    print("Dequeue all the elements of the queue:")
    for i in range(new_queue.size()):
        print(new_queue.dequeue())   
    print("Try dequeue an element of the empty queue:")
    try:
        print(new_queue.dequeue())
    except RuntimeError as error:
        print(error) 