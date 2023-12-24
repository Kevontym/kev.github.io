import threading 

# def function1():
#     for x in range(10000):
#         print("One")
# def function2():
#     for x in range(10000):
#         print("Two")

# t1 = threading.Thread(target=function1)

# t2 = threading.Thread(target=function2)

# t1.start()
# t2.start()

def hello():
    for x in range(50):
        print("Hello")

t1 = threading.Thread(target=hello)
t1.start()

t1.join()

print("Another text")