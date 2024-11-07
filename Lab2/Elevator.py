import sys

class InvalidFloorError(Exception):
    pass

class FloorDispatcher:
    def __init__(self, max_floor):
        self.valid_floors = {floor: floor for floor in range(1, max_floor + 1)}

    def get_floor(self, floor):
        """Возвращает этаж или вызывает исключение при недопустимом этаже."""
        try:
            return self.valid_floors[floor]  
        except KeyError:
            raise InvalidFloorError(f"Этаж {floor} недопустим.")

class Elevator:
    def __init__(self, num_floors):
        self.num_floors = num_floors
        self.current_floor = 1
        self.requests = []
        self.moves = 0
        self.dispatcher = FloorDispatcher(num_floors)

    def call_elevator(self, request_floor):
        self.requests.append(request_floor)

    def move_up(self):
        """Подъем на один этаж с добавлением сообщения"""
        self.current_floor = self.dispatcher.get_floor(self.current_floor + 1)
        self.moves += 1
        return f"Лифт поднялся на этаж {self.current_floor}"

    def move_down(self):
        """Спуск на один этаж с добавлением сообщения"""
        self.current_floor = self.dispatcher.get_floor(self.current_floor - 1)
        self.moves += 1
        return f"Лифт опустился на этаж {self.current_floor}"

    def go_to_floor(self, target_floor):
        """Переход к целевому этажу"""
        commands = []
        
        try:
            direction = (target_floor - self.current_floor) // abs(target_floor - self.current_floor)
        except ZeroDivisionError:
            return commands

        move_methods = {1: self.move_up, -1: self.move_down}
        move_method = move_methods[direction]
        
        while self.current_floor != target_floor:
            try:
                commands.append(move_method())
            except InvalidFloorError as e:
                print(str(e))
                sys.exit("Программа завершена из-за недопустимого перемещения.")
        return commands

    def process_requests(self):
        commands = []
        while self.requests:
            next_request = self.requests.pop(0)
            commands.extend(self.go_to_floor(next_request))
            commands.append("Лифт открыл двери")
            commands.append("Лифт закрыл двери")
        return commands
