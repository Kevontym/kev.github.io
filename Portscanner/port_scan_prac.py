from queue import Queue
import socket
import threading


#Then, we will also define three global variables that 
# we will use throughout the various functions:

target = "127.0.0.1"
queue = Queue()
open_ports = []

#We start by implementing the portscan function, 
# which we have already talked about.

def portscan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        return True
    except:
        return False

# Now, before we get into the threading, we need to first define 
# the ports we want to scan. For this, we will define another function 
# called get_ports.

def get_ports(mode):
    if mode == 1:
        for port in range(1, 1024): 
            queue.put(port)
    elif mode == 2:
        for port in range(1, 49152):
            queue.put(port)
    elif mode == 3:
        ports = [20, 21, 22, 23, 25, 53, 80, 110, 443]
        for port in ports:
            queue.put(port)
    elif mode == 4:
        ports = input("Enter your ports(seperate by blank):")
        ports = ports.split()
        ports = list(map(int,ports))
        for port in ports:
            queue.put(port)

#  This function will be responsible for getting the port numbers from the queue, 
# scanning them and printing the results.

def worker():
    while not queue.empty():
        port = queue.get()
        if portscan(port):
            print("Port {} is open!".format(port))
            open_ports.append(port)
        
#So, now that we have implemented the functionality, 
# we are going to write our main function, which creates, 
# starts and manages our threads.


def run_scanner(threads, mode):
    
    get_ports(mode)
    
    thread_list = []
    
    for t in range(threads):
        thread = threading.Thread(target=worker)
        thread_list.append(thread)
    
    for thread in thread_list:
        thread.start()
    
    for thread in thread_list:
        thread.join()
    
    print("Open ports are:", open_ports)


# The first one is for the amount of threads we want to start and the 
# second one is our mode. We load our ports, depending on the mode we 
# have chosen and we create a new empty list for our threads. 
# Then, we create the desired amount of threads, assign them our 
# worker function and add them to the list. After that, we start 
# all our threads and let them work. They are now scanning all the ports. Finally, we wait for all the threads to finish and print all the open ports once again.

run_scanner(100, 1)