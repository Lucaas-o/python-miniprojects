from clear_screen import clear_screen
import time

rooms = {
    'room1': {'north': 'room2', 'south': 'room3'},
    'room2': {'south': 'room1'},
    'room3': {'north': 'room1'}
}

descriptions = {
    'room1': "You are in the starting room. There are doors to the north and south.",
    'room2': "You are in a room with a key on the table.",
    'room3': "You are in a room with a locked chest."
}

items = {
    'room1': [],
    'room2': ['key'],
    'room3': ['chest']
}

takeable_items = ['key', 'treasure']

current_room = 'room1'
player_inventory = []
game_over = False
won_game = False

AVAILABLE_COMMANDS = "Commands: go [direction], take [item], use [item] [target], inventory, look, quit"

def display_room(room, room_items):
    print(descriptions[room])
    if room_items[room]:
        print(f"You see: {room_items[room]}")
    else:
        print("The room is empty.")

def move_player(current, direction, room_map):
    if direction in room_map[current]:
        print(f"You move to the {direction}.")
        return room_map[current][direction]
    print("You can't go that way.")
    return current

def take_item(item, room_items, current, inventory, allowed_items):
    global won_game
    if item in room_items[current] and item in allowed_items:
        if item == 'treasure':
            print("You take the treasure. You win!")
            won_game = True
            return True
        inventory.append(item)
        room_items[current].remove(item)
        print(f"You take the {item}.")
        return False
    print("You can't take that.")
    return False

def use_item(item, target, inventory, room_items, current):
    if item not in inventory:
        print("You don't have that item.")
    elif target not in room_items[current]:
        print("That target is not here.")
    elif item == 'key' and target == 'chest' and current == 'room3':
        print("You use the key on the chest and it opens. Inside, you find a treasure.")
        room_items[current].remove('chest')
        room_items[current].append('treasure')
    else:
        print("You can't use that item on that target.")

while not game_over:
    display_room(current_room, items)
    print("You are carrying:", player_inventory)
    print(AVAILABLE_COMMANDS)
    
    command = input("What do you do? ").lower().strip().split()
    if not command:
        clear_screen()
        continue
    
    action = command[0]
    
    if action == 'go' and len(command) > 1:
        current_room = move_player(current_room, command[1], rooms)
    elif action == 'take' and len(command) > 1:
        game_over = take_item(command[1], items, current_room, player_inventory, takeable_items)
    elif action == 'use' and len(command) == 3:
        use_item(command[1], command[2], player_inventory, items, current_room)
    elif action == 'inventory':
        print("You are carrying:", player_inventory)
    elif action == 'look':
        display_room(current_room, items)
    elif action == 'help':
        print(AVAILABLE_COMMANDS)
    elif action == 'quit':
        game_over = True
    else:
        print("Unknown command.")
    
    time.sleep(1)
    clear_screen()

clear_screen()
print("You won!" if won_game else "Game over.")
if won_game:
    time.sleep(5)
