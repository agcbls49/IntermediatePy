### GLI: Global Interpreter Lock
*- A lock that allows only one thread at a time to exceute in Python* <br>
*- Needed in CPython because memory management is not thread-safe* <br><br>
*- Avoid:* <br>
*- Use multiprocessing* <br>
*- Use a different, free-threaded Python implementation (JPython, IronPython)* <br>
*- Use Python as a wrapper for third-party libraries (C, C++) -> numpy, scipy* <br>

----

### Process: An instance of a program (e.g a Python Interpreter)

*+ Takes advantage of multiple CPUs and cores* <br>
*+ Separate memory space -> Memory is not shared between processes* <br>
*+ Great for CPU-bound processing* <br>
*+ New process is stated independently from other processes* <br>
*+ Processes are interruptable/killable* <br>
*+ One GIL for each process -> avoids GIL limitation* <br>

*- Heavyweight* <br>
*- Starting a process is slower than starting a thread* <br>
*- More memory* <br>
*- IPC (inter-process communication) is more complicated* <br>

----

### Threads: Ann entity within a process that can be scheduled (also known as "lightweight process)
A process can spawn multiple threads

*+ All threads within a process share the same memory* <br>
*+ Lightweight* <br>
*+ Starting a thread is faster than starting a process* <br>
*+ Great for I/O-bound tasks* <br>

*- Threading is limited by GIL: Only one thread at a time* <br>
*- No effect for CPU-bound tasks* <br>
*- Not interruptable/killable* <br>
*- Careful with race conditions* <br>