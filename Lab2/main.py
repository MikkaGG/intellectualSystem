from Run_elevator_simulation import run_elevator_simulation

num_floors = 5
start_floors = [1, 5]
requests = [
    [(1, 3), (4, 2)],
    [(2, 5), (3, 1)],
]

run_elevator_simulation(num_floors, start_floors, requests)
