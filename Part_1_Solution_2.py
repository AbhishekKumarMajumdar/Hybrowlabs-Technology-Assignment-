# Problem 2: Queue
# Implement a queue data structure in Python. The queue should support the following operations:
# enqueue(item) - Add an item to the back of the queue.
# dequeue() - Remove and return the item at the front of the queue.
# peek() - Return the item at the front of the queue without removing it.
# is_empty() - Return True if the queue is empty, else False.

'''Solution'''

Queue = []
Front = None
Rear = None

def is_Empty(que):
    if(Queue==[]):
        return True
    else:
        return False
def enqueue(que,Item):
    que.append(Item)
    if(len(que)==1):
        Front=Rear=0
    else:
        Rear =len(que)-1

def dequeue(que):
    if(is_Empty(que)):
        return("Underflow")
    else:
        i = que.pop(0)
    if(len(que)==0):
        Front=Rear=None
        return i

def Peek(que):
    if(is_Empty(que)):
        print("Underflow")
    else:
        Front = 0
    return que[Front]


while True:
    print("Implement a Queue data structure in Python")
    choose = input("Enter your Operation (Enqueue , Dequeue , Peek , is_empty , Exit \n").lower()
    if(choose=='dequeue'):
        Item = dequeue(Queue)
        if(Item=="Underflow"):
            print("The Queue is Empty")
        else:
            print(Item ,"Element is  dequeue in Queue and",end=" ")
            if(is_Empty(Queue)):
                print("Queue is Empty.")
            else:
                print("Front Element of Queue is ",Peek(Queue))
        input("enter to continue")
    if 'enqueue' in choose:
        Item = int(input("Enter the Item For Enqueue in Queue \n"))
        enqueue(Queue,Item)
        print("%d is Enqueue in Queue"%Item)
        input("enter to continue")

    if  'peek' in choose:
        Item = Peek(Queue)
        if(Item==None):
            print("Queue is Empty")
        else:
            print(Item," is Front Item in The Queue")
        input("enter to continue")
    
    if 'is_empty' in choose:
        print(is_Empty(Queue))

    if 'exit' in choose:
        break
       





