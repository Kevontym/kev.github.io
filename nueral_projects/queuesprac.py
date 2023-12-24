import queue

# numbers = [10, 20, 30, 40, 50, 60, 70]
# counter = 

#------------

# q = queue.Queue()

# numbers = [10, 20, 30, 40, 50, 60, 70]
# for number in numbers:
#     q.put(number)

# print(q.get())
# print(q.get())

#--------------

# q = queue.LifoQueue()

# numbers = [1, 2, 3, 4, 5, 6, 7]
# for x in numbers:
#     q.put(x)
    
# print(q.get())

#-----------

q = queue.PriorityQueue()

q.put((2, "Helloworld!"))
q.put((11, 99))
q.put((5, 7.5))
q.put((1, True))

print(q.get())

while not q.empty():
    print(q.get())