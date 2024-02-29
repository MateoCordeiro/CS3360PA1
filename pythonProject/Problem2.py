import random

# Constants
MTBF = 500  # Mean Time Between Failures in hours
RESTORE_TIME = 10  # Time to restore from mirror in hours
HOURS_PER_DAY = 24
DAYS_PER_YEAR = 365
SIMULATION_YEARS = 20

def generate_failure_data():
    # Initialize variables
    current_time = 0
    failure_times = []

    while current_time < SIMULATION_YEARS * DAYS_PER_YEAR * HOURS_PER_DAY:
        # Generate failure time based on exponential distribution
        failure_time = random.expovariate(1 / MTBF)
        current_time += failure_time
        failure_times.append(current_time)

        # Add restore time to the failure time for the mirror server
        current_time += RESTORE_TIME

    return failure_times

def find_system_failure_time():
    num_simulations = 1000
    total_failures = 0
    total_system_failure_time = 0

    for _ in range(num_simulations):
        server1_failures = generate_failure_data()
        server2_failures = generate_failure_data()

        # Check for system failure
        for failure_time in server1_failures:
            if any(failure_time <= t <= failure_time + RESTORE_TIME for t in server2_failures):
                total_failures += 1
                total_system_failure_time += failure_time

    average_failure_time = total_system_failure_time / total_failures if total_failures > 0 else 0
    return average_failure_time / (DAYS_PER_YEAR * HOURS_PER_DAY)  # Convert to years

if __name__ == "__main__":
    # Part (a)
    print("Failure and restoration times for each server over 20 years:")
    for i in range(2):
        print(f"Server {i+1} failures:", generate_failure_data())

    # Part (b)
    average_system_failure_time = find_system_failure_time()
    print("\nAverage time until the whole computing system fails:", average_system_failure_time, "years")
