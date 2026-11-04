def round_robin(processes, burst_time, time_quantum):
    n = len(processes)
    remaining_bt = burst_time.copy()
    waiting_time = [0] * n
    turnaround_time = [0] * n
    time = 0

    while True:
        done = True
        for i in range(n):
            if remaining_bt[i] > 0:
                done = False
                if remaining_bt[i] > time_quantum:
                    time += time_quantum
                    remaining_bt[i] -= time_quantum
                else:
                    time += remaining_bt[i]
                    waiting_time[i] = time - burst_time[i]
                    remaining_bt[i] = 0

        if done:
            break

    for i in range(n):
        turnaround_time[i] = burst_time[i] + waiting_time[i]

    print("\nProcess\tBurst Time\tWaiting Time\tTurnaround Time")
    for i in range(n):
        print(f"{processes[i]}\t\t{burst_time[i]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")

    print("\nAverage Waiting Time =", sum(waiting_time)/n)
    print("Average Turnaround Time =", sum(turnaround_time)/n)


# Input
n = int(input("Enter number of processes: "))
processes = []
burst_time = []

for i in range(n):
    processes.append(f"P{i+1}")
    bt = int(input(f"Enter Burst Time for P{i+1}: "))
    burst_time.append(bt)

time_quantum = int(input("Enter Time Quantum: "))

round_robin(processes
