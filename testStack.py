from queue import LifoQueue

stack = LifoQueue(maxsize=3)

print()
print('Initial number of elements : ', stack.qsize())

stack.put('a')
stack.put('b')
stack.put('c')

print('Populated number of elements : ', stack.qsize())
print('Full : ', stack.full())
print("Empty : ", stack.empty())

print('Popping elements from stack...')
print(stack.get())
print(stack.get())
print(stack.get())

print('Full : ', stack.full())
print("Empty: ", stack.empty())
print('Populated number of elements : ', stack.qsize())
print()
