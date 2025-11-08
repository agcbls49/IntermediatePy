# Threading vs Multiprocessing
# See Threading.md file

# Supposed to work but doesnt
import os
import time
from multiprocessing import Process

def square_numbers():
    for i in range(5):
        i * i
        time.sleep(0.1)

processes = []
num_processes = os.cpu_count()

# Create Processes
for i in range(num_processes):
    # add (target=, args=) if there are arguments
    p = Process(target=square_numbers)
    processes.append(p)

# Start each process
for p in processes:
    p.start()

# Join waits for a process to finish and 
# while waiting, it blocks the main thread
for p in processes:
    p.join()

print("End Main")