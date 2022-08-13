# Stack implementation in python

# Creating a stack
def createStack():
    stack = []
    return stack

# Check if stack is empty
def isEmpty(stack):
    return len(stack) == 0

# Adding items into stack
def push(stack, item):
    stack.append(item)

# Removing an element from stack
def pop(stack):
    if (isEmpty(stack)):
        print("Stack is empty")

    else:
        stack.pop()


stack = createStack()
push(stack, 1)
push(stack, 2)
push(stack, 4)
push(stack, 5)


for val in stack:
    print(val)
