# Distributed_Order_Processing

Reflection Answers
1. How did you distribute orders among worker processes?

-Orders were distributed from the master process (rank 0) to worker processes using MPI communication. A round-robin method was used, where each order was assigned to a worker based on its index using the formula worker = (i % (size - 1)) + 1. This ensured that the workload was evenly shared among all available workers.

2. What happens if there are more orders than workers?

-If there are more orders than workers, some workers will receive and process multiple orders. The round-robin distribution allows tasks to cycle through workers, ensuring all orders are handled even if workers are fewer than tasks.

3. How did processing delays affect the order completion?

-Processing delays were added using time.sleep() to simulate real-world execution time. Because of these delays, workers completed tasks at different times, resulting in non-sequential output. This demonstrated concurrent processing across multiple processes.

4. How did you implement shared memory, and where was it initialized?

-Shared memory behavior was implemented using MPI message passing rather than direct shared variables. Workers sent processed order results back to the master process using comm.send(), and the master collected them using comm.recv(). The result collection was handled in the master process.

5. What issues occurred when multiple workers wrote to shared memory simultaneously?

-When multiple processes attempt to write at the same time, race conditions and inconsistent data can occur in traditional shared memory systems. In this implementation, this was avoided by letting only the master process collect and store results, ensuring controlled access.

6. How did you ensure consistent results when using multiple processes?

-Consistency was ensured by centralizing the collection of results in the master process. Workers only processed tasks and sent results, while the master handled all storage and final output. This avoided conflicts and ensured correct and complete results.

FINAL RESULT
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/50c9d185-19a4-4a4e-9965-d6c84892d114" />

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/06a4adb4-ad3e-426c-992c-4d7babeb8bb8" />




