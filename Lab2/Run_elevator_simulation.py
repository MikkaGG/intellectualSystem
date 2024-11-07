from Elevator import Elevator

def run_elevator_simulation(num_floors, start_floors, requests):
    elevators = [Elevator(num_floors) for _ in start_floors]

    for i, floor in enumerate(start_floors):
        elevators[i].current_floor = floor

    results = []
    for i, elevator in enumerate(elevators):
        print(f"Лифт {i+1} начинает с этажа {elevator.current_floor}")
        for request in requests[i]:
            elevator.call_elevator(request[0])
            elevator.call_elevator(request[1])
        results.append(elevator.process_requests())
    
    for i, commands in enumerate(results):
        print(f"\nКоманды для лифта {i+1}:")
        print("\n".join(commands))
        print(f"Количество перемещений: {elevators[i].moves}")
        