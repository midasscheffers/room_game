class player:
    def __init__(self):
        self.name = ''
        self.x = 1
        self.y = 1
        self.char = '@'
        self.inventory = []
        self.show_data = False
        self.show_data_str = ""
        self.health = 100

    def print_data(self):
        if self.show_data == True:
            print(self.show_data_str)

    def draw_player(self, _map):
        player_map = _map.copy()
        player_map[self.y] = player_map[self.y][:self.x] + self.char[0] + player_map[self.y][self.x+1:]
        return player_map

    def move(self, user_inp, _map):
        if (user_inp == "d"):
                if(not _map[self.y][self.x+1] == '^'):
                    self.x += 1
                    self.show_data = False
                else:
                    self.show_data = True
                    self.show_data_str = "you can't move here\n"
        elif (user_inp == "a"):
                if(not _map[self.y][self.x-1] == '^'):
                    self.x -= 1
                    self.show_data = False
                else:
                    self.show_data = True
                    self.show_data_str = "you can't move here\n"
        elif (user_inp == "s"):
                if(not _map[self.y+1][self.x] == '^'):
                    self.y += 1
                    self.show_data = False
                else:
                    self.show_data = True
                    self.show_data_str = "you can't move here\n"
        elif (user_inp == "w"):
                if(not _map[self.y-1][self.x] == '^'):
                    self.y -= 1
                    self.show_data = False
                else:
                    self.show_data = True
                    self.show_data_str = "you can't move here\n"
        else:
            self.show_data = False

    def player_logic(self, user_inp, rooms):
        if user_inp[0:4] == "use "
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
