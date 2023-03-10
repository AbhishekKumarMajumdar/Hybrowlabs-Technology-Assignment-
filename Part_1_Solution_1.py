
# Problem 1: Stack
# Implement a stack data structure in Python. The stack should support the following operations:
# push(item) - Add an item to the top of the stack.
# pop() - Remove and return the item on the top of the stack.
# peek() - Return the item on the top of the stack without removing it.
# is_empty() - Return True if the stack is empty, else False.

'''Solution'''

Stack = []
Top = len(Stack)-1
def is_Empty(stk):
    if(stk==[]):
        return True
    else:
        return False

def Push(stk,Item):
    stk.append(Item)
    Top = len(stk)-1

def S_Pop(stk):
    if(is_Empty(stk)):
        print("The Stack is Empty")
    else:
        i = stk.pop()
        return i

def Peek(stk):
    if(is_Empty(stk)):
        print("The Stack is Empty")
    else:
        Top = len(stk)-1
        return stk[Top]

def Display(stk):
    if(is_Empty(stk)):
        print("The Stack is Empty")
    else:
        top = len(stk)-1
        print(stk[top],"<---Top")
        for i in range (top-1,-1,-1):
            print(stk[i])

while True:
    print("Implement a stack data structure in Python")
    choose = input("Enter your Operation (push , pop , peek , display , exit \n").lower()
    if(choose=='pop'):
        Item = S_Pop(Stack)
        if(Item==None):
            print(" ")
        else:
            print(Item ,"Element is  Popped in Stack and",end=" ")
            if(is_Empty(Stack)):
                print("Stack is Empty.")
            else:
                print("Top Element of Stack is ",Peek(Stack))
        input("enter to continue")
    if 'push' in choose:
        Item = int(input("Enter the Item For Push in Stack \n"))
        Push(Stack,Item)
        print("%d is Pushed in Stack"%Item)
        input("enter to continue")

    if  'peek' in choose:
        Item = Peek(Stack)
        if(Item==None):
            print("Stack is Empty")
        else:
            print(Item," is Top Item in The stack")
        input("enter to continue")

    if  'display' in choose:
        Display(Stack)
        input("enter to continue")

    if 'exit' in choose:
        break