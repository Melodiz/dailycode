Okay, here's the quiz solution in the requested Markdown format:

* **1. Select the statements that are true about any operating system:**
    > * It provides an interface for user applications to interact with the hardware
    > * It provides management of computer resources
    > * It controls the execution of all other programs

---
* **2. Select the statements that are true about system programs and user programs:**
    > * Some system programs, unlike user programs, can directly interact with computer resources, input-output devices.
    > * System programs are those that come with the operating system. For example, pre-installed drivers, utilities, built-in calculator

---
* **3. Match the objects to the memory regions where they are stored (stack, heap, static data, code):**
    > * **1. apple:** Static Data
    > * **2. banana:** Static Data
    > * **3. cherry:** Stack
    > * **4. date (where it points, not the pointer itself):** Heap
    > * **5. String literal "Completed\\n":** Static Data

---
* **4. What is declared here? `const char* (*f)(int);`**
    > 3. Pointer to a function that takes an int and returns a pointer to a constant char

---
* **5. Match some of the functions performed by operating systems with their descriptions.**
    > * **Ensuring that all access to system resources is controlled:** Protection
    > * **Distribution of CPU cycles, RAM, disk space between simultaneously running processes:** Resource allocation
    > * **User authentication, restriction of access of external input/output devices to the system:** Security
    > * **Taking corrective action in case of problems during process execution:** Error detection and handling

---
* **6. Select the correct statements about system calls:**
    > * System calls are APIs between user applications and the operating system kernel
    > * When a system call is executed, the process switches from user mode to kernel mode

---
* **7. Which C programs will compile successfully?**
    > Program 2 and Program 3 will compile successfully.
    > * **Program 2:** Will compile successfully.
    > * **Program 3:** Will compile successfully (likely with warnings about returning the address of a local variable).

---
* **8. What will be printed as a result of running the program? (Program with `sizeof(arr)` in a function where `arr` is a char array parameter)**
    > Impossible to tell, because the size of a pointer in bytes depends on the system

---
* **9. Match each system call to its type:**
    > 1-A, 2-C, 3-B, 4-D, 5-E
    > * **1. fork()** -> A) Process control
    > * **2. read()** -> C) Device I/O
    > * **3. open()** -> B) File management
    > * **4. chmod()** -> D) Protection
    > * **5. shmget()** -> E) Interprocess communication (IPC)

---
* **10. What happens if you compile and run this program? (Program with integer division by zero)**
    > The program will compile, but the result of the work is not guaranteed (undefined behavior)