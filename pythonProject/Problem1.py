import random

def generate_workload(num_processes, arrival_rate, service_time):
    arrival_time = 0
    process_list = []

    for process_id in range(1, num_processes + 1):
        interarrival_time = random.expovariate(arrival_rate)
        arrival_time += interarrival_time
        service_duration = random.expovariate(service_time)
        process_list.append((process_id, arrival_time, service_duration))

    return process_list

if __name__ == "__main__":
    num_processes = 1000
    arrival_rate = 2  # processes per second
    service_time = 1  # average service time in seconds

    process_list = generate_workload(num_processes, arrival_rate, service_time)

    # Print the list of tuples in the format of <process ID, arrival time, requested service time>
    for process in process_list:
        print(process)

    # Calculate the actual average arrival rate and actual average service time
    actual_avg_arrival_rate = num_processes / process_list[-1][1]  # total processes / total time
    actual_avg_service_time = sum(process[2] for process in process_list) / num_processes

    print("\nActual Average Arrival Rate:", actual_avg_arrival_rate, "processes per second")
    print("Actual Average Service Time:", actual_avg_service_time, "seconds")
