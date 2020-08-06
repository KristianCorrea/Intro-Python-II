# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
    
    def __str__(self):
        return {self.name}

    def locate(self):
        print(f'You are now in: \n{self.current_room}.') 

    def movement(self, direction):
        if direction == 'n':
            if self.current_room.n_to == None:
                print("No pathway North.")
            else:
                self.current_room = self.current_room.n_to
                print(f'You are now in: \n{self.current_room}.')
        elif direction == 's':
            if self.current_room.s_to == None:
                print("No pathway South.")
            else:
                self.current_room = self.current_room.s_to
                print(f'You are now in: \n{self.current_room}.')
        elif direction == 'w':
            if self.current_room.w_to == None:
                print("No pathway West.")
            else:
                self.current_room = self.current_room.w_to
                print(f'You are now in: \n{self.current_room}.')
        elif direction == 'e':
            if self.current_room.e_to == None:
                print("No pathway East.")
            else:
                self.current_room = self.current_room.e_to
                print(f'You are now in: \n{self.current_room}.')