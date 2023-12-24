import threading
import time

# x = 8192

# lock = threading.Lock()

# def double():
#     global x, lock
#     lock.acquire()
#     while x < 16384:
#         x *= 2
#         print(x)
#         time.sleep(1)
#     print("reached the maximum!")
#     lock.release()

# def halve():
#     global x, lock
#     lock.acquire()
#     while x > 1:
#         x /= 2
#         print(x)
#         time.sleep(1)
#     print("You have reached minimum")
#     lock.release()
        
# t1 = threading.Thread(target=halve)
# t2 = threading.Thread(target=double)

# t1.start()
# t2.start()

#---------------

semaphore = threading.BoundedSemaphore(value=5)

def access(thread_number):
    print("{} is trying to access!".format(thread_number))
    semaphore.acquire()
    print("{} was granted access!".format(thread_number))
    time.sleep(10)
    print("{} is now releasing!".format(thread_number))
    semaphore.release()
    
for thread_number in range(1, 11):
    t = threading.Thread(target=access, args=(thread_number,))
    t.start()
    time.sleep(1)

