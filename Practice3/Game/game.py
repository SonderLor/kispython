import graphviz


class Room:
    def __init__(self, name, label, description, exits):
        self.name = name
        self.label = label
        self.description = description
        self.exits = exits


class Game:
    def __init__(self):
        self.rooms = dict()
        self.current_room = None

    def add_room(self, room):
        self.rooms[room.label] = room

    def start_game(self, start_room_label):
        if start_room_label in self.rooms:
            self.current_room = self.rooms[start_room_label]
            print("=" * 40)
            print("\nНачало игры.\n")
            self.print_current_room()
        else:
            print("Ошибка: Начальная комната не найдена.")

    def print_current_room(self):
        print("\n" + self.current_room.description)
        if self.current_room.name == "Выход":
            return True
        else:
            print("Доступные выходы:")
            for i, exit_label in enumerate(self.current_room.exits, 1):
                print(f"{i}. {exit_label}")

    def process_input(self, input_index):
        if input_index < 1 or input_index > len(self.current_room.exits):
            print("Ошибка: Неверный выбор выхода.")
            return
        next_room_label = self.current_room.exits[input_index - 1]
        if next_room_label in self.rooms:
            self.current_room = self.rooms[next_room_label]
            if self.print_current_room():
                return True
        else:
            print("Ошибка: Следующая комната не найдена.")


def generate_dot_graph(game):
    dot_code = "digraph G {\n"
    for room_label, room in game.rooms.items():
        for exit_label in room.exits:
            dot_code += f'"{room.name}" -> "{exit_label}";\n'
    dot_code += "}"
    return dot_code


def get_graph(game):
    dot_graph = generate_dot_graph(game)
    graph = graphviz.Source(dot_graph, format="png")
    graph.render("game_graph", view=True)


def dfs(rooms_data, room_id, visited):
    visited.add(room_id)
    for exit_room_id in rooms_data[room_id]["exits"]:
        if exit_room_id not in visited:
            dfs(rooms_data, exit_room_id, visited)


def find_unreachable_rooms(rooms_data):
    unreachable_rooms = list()
    exit_room_id = max(rooms_data.keys())
    for room_id in rooms_data.keys():
        reachable_rooms = set()
        dfs(rooms_data, room_id, reachable_rooms)
        if exit_room_id not in reachable_rooms:
            unreachable_rooms.append(room_id)

    print("Комнаты, из которых невозможно добраться до выхода:")
    for room_id in unreachable_rooms:
        print(f"Комната №{room_id}")


def create_game() -> "Game":
    rooms_data = {
        1: {"name": "Комната №1", "description": "Вы находитесь в комнате №1.", "exits": [2, 3]},
        2: {"name": "Комната №2", "description": "Вы находитесь в комнате №2.", "exits": [1, 4, 5]},
        3: {"name": "Комната №3", "description": "Вы находитесь в комнате №3.", "exits": [1, 6, 7]},
        4: {"name": "Комната №4", "description": "Вы находитесь в комнате №4.", "exits": [2, 8, 9]},
        5: {"name": "Комната №5", "description": "Вы находитесь в комнате №5.", "exits": [2, 10, 11]},
        6: {"name": "Комната №6", "description": "Вы находитесь в комнате №6.", "exits": [3, 12, 13]},
        7: {"name": "Комната №7", "description": "Вы находитесь в комнате №7.", "exits": [1, 14, 15]},
        8: {"name": "Комната №8", "description": "Вы находитесь в комнате №8.", "exits": [4]},
        9: {"name": "Комната №9", "description": "Вы находитесь в комнате №9.", "exits": [4]},
        10: {"name": "Комната №10", "description": "Вы находитесь в комнате №10.", "exits": [5]},
        11: {"name": "Комната №11", "description": "Вы находитесь в комнате №11.", "exits": [5]},
        12: {"name": "Комната №12", "description": "Вы находитесь в комнате №12.", "exits": [6, 16]},
        13: {"name": "Комната №13", "description": "Вы находитесь в комнате №13.", "exits": [6]},
        14: {"name": "Комната №14", "description": "Вы находитесь в комнате №14.", "exits": [7]},
        15: {"name": "Комната №15", "description": "Вы находитесь в комнате №15.", "exits": [7]},
        16: {"name": "Выход", "description": "Поздравляю, вы выбрались из лабиринта!", "exits": []}
    }

    find_unreachable_rooms(rooms_data)

    game = Game()
    for room_id, room_data in rooms_data.items():
        exits = [rooms_data[exit_id]["name"] for exit_id in room_data["exits"]]
        game.add_room(Room(room_data["name"], room_data["name"], room_data["description"], exits))
    return game


def play(game):
    while True:
        choice = input("> ")
        if choice.lower() == "exit":
            print("Выход из игры.")
            break
        try:
            choice_index = int(choice)
            if game.process_input(choice_index):
                return True
        except ValueError:
            print("Ошибка: Введите число или 'exit' для выхода.")


if __name__ == "__main__":
    my_game = create_game()

    get_graph(my_game)

    my_game.start_game("Комната №1")
    play(my_game)
