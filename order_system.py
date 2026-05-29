# order_system.py (FINAL CODE)

from mpi4py import MPI
import time
import random

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# =========================
# MASTER PROCESS
# =========================
if rank == 0:

    print("\nMASTER: Starting order system...\n")

    # Orders (5–8 as required)
    orders = [
        (1, "Burger"),
        (2, "Fries"),
        (3, "Pizza"),
        (4, "Soda"),
        (5, "Chicken"),
        (6, "Ice Cream")
    ]

    print("MASTER: Orders created")
    print(orders, "\n")

    # Send orders to workers
    worker_count = size - 1

    for i, order in enumerate(orders):
        worker = (i % worker_count) + 1
        comm.send(order, dest=worker)

    # Send stop signal
    for worker in range(1, size):
        comm.send(None, dest=worker)

    print("MASTER: Sending orders...\n")

    # Collect results
    completed_orders = []

    for _ in range(len(orders)):
        result = comm.recv()
        completed_orders.append(result)

    print("\nMASTER: FINAL COMPLETED ORDERS\n")

    for item in completed_orders:
        print(item)

    print("\nMASTER: Done.\n")


# =========================
# WORKER PROCESSES
# =========================
else:

    while True:

        order = comm.recv(source=0)

        if order is None:
            break

        order_id, item = order

        print(f"Worker {rank} received order: {order}")

        # simulate processing delay
        time.sleep(random.randint(1, 3))

        result = f"Order {order_id} ({item}) completed by Worker {rank}"

        comm.send(result, dest=0)
