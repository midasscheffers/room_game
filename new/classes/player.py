class player:
    def __init__(self):
        self.name = ''
        self.x = 1
        self.y = 1
        self.char = '@'
        self.inventory = []
        self.moved = False
        self.health = 100

    def draw_player(self, _map):
        player_map = _map.copy()
        player_map[self.y] = player_map[self.y][:self.x] + self.char[0] + player_map[self.y][self.x+1:]
        return player_map

    def move(self, user_inp, _map):
        if (user_inp == "d"):
                if(not _map[self.y][self.x+1] == '^'):
                    self.x += 1
                    self.moved = True
                else:
                    self.moved = False
        elif (user_inp == "a"):
                if(not _map[self.y][self.x-1] == '^'):
                    self.x -= 1
                    self.moved = True
                else:
                    self.moved = False
        elif (user_inp == "s"):
                if(not _map[self.y+1][self.x] == '^'):
                    self.y += 1
                    self.moved = True
                else:
                    self.moved = False
        elif (user_inp == "w"):
                if(not _map[self.y-1][self.x] == '^'):
                    self.y -= 1
                    self.moved = True
                else:
                    self.moved = False
        else:
            self.moved = True
