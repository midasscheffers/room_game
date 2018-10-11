import random

class player:

    def __init__(self):
        self.name = ''
        self.x = 1
        self.y = 1
        self.char = '@'
        self.inventory = ["key"]
        self.show_data = False
        self.show_data_str = ""
        self.health = 100
        self.use_functions = {"sword" : self.attack, "healing potion" : self.heal}


    def print_data(self):
        if self.show_data:
            print(self.show_data_str)


    def draw_player(self, _map):
        player_map = _map.copy()
        player_map[self.y] = player_map[self.y][:self.x] + self.char[0] + player_map[self.y][self.x+1:]
        return player_map


    def move(self, user_inp, w):
        if (user_inp == "d"):
                if(not w._map[self.y][self.x+1] == w.wall_char):
                    self.x += 1
                    self.show_data = False
                else:
                    self.show_data = True
                    self.show_data_str = "you can't move here\n"
        elif (user_inp == "a"):
                if(not w._map[self.y][self.x-1] == w.wall_char):
                    self.x -= 1
                    self.show_data = False
                else:
                    self.show_data = True
                    self.show_data_str = "you can't move here\n"
        elif (user_inp == "s"):
                if(not w._map[self.y+1][self.x] == w.wall_char):
                    self.y += 1
                    self.show_data = False
                else:
                    self.show_data = True
                    self.show_data_str = "you can't move here\n"
        elif (user_inp == "w"):
                if(not w._map[self.y-1][self.x] == w.wall_char):
                    self.y -= 1
                    self.show_data = False
                else:
                    self.show_data = True
                    self.show_data_str = "you can't move here\n"
        else:
            self.show_data = False


    def attack(self, room, j):
        room.monsterHealth -= 20
        if random.randint(1,20) == 19:
            self.inventory.remove(j)
            self.show_data = True
            self.show_data_str = "your sword broke"
        if room.monsterHealth <= 0:
            room.monsterHere = False
            self.show_data = True
            self.show_data_str = "you have slain the monster"


    def heal(self, room, j):
        self.health += 20
        self.inventory.remove(j)


    def player_logic(self, user_inp, rooms):
        if user_inp[0:4] == "use ":
            for room in rooms:
                if room.x == self.x and room.y == self.y:
                    if (user_inp[4:-1] + user_inp[-1]) in self.inventory[::-1]:
                        j = user_inp[4:-1] + user_inp[-1]
                        # self.use_functions[user_inp[4:-1] + user_inp[-1]](room, j)
                        try:
                            self.use_functions[user_inp[4:-1] + user_inp[-1]](room, j)

                        except:
                            self.show_data = True
                            self.show_data_str = "you can't use this Item:" + user_inp[4:-1] + user_inp[-1]
                        break
                    else:
                        self.show_data = True
                        self.show_data_str = "you haven't got that Item"
        if user_inp == "i":
            self.show_data = True
            self.show_data_str = str(self.inventory) + "\n"

        if user_inp[0:5] == "drop ":
            for i in range(len(rooms)):
                if rooms[i].x == self.x and rooms[i].y == self.y:
                    for j in self.inventory[::-1]:
                        if user_inp[5:-1] + user_inp[-1] == j:
                            rooms[i].inventory.append(j)
                            print()
                            self.show_data = True
                            self.show_data_str = "You droped: " + j + "\n"
                            self.inventory.remove(j)
                            break
