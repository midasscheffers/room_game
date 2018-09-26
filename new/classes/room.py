class room:
    def __init__(self, _x, _y):
        self.inventory = []
        self.id = ""
        self.description = ""
        self.x = _x
        self.y = _y
        self.monsterHere = False
        self.monsterHealth = 50
        self.show_data = False
        self.show_data_str = ""


    def print_data(self):
        if self.show_data == True:
            print(self.show_data_str)


    def what_to_print(self):
        if self.inventory == [] and self.monsterHere == False:
            self.show_data_str = "there is nothing here\n"
        elif self.inventory == [] and self.monsterHere == True:
            self.show_data_str = "there is a big monster in the corner\n"
        elif not self.inventory == [] and self.monsterHere == False:
            self.show_data_str = "In this room there is {}, you are the biggest here\n".format(self.inventory)
        else:
            self.show_data_str = "In this room there is {}, here is a monster in te corner\n".format(self.inventory)


    def room_logic(self, user_inp, p):
        global gameExit

        if self.x == p.x and self.y == p.y:
            if self.monsterHere == True:
                p.health -= 20
            if (user_inp == "data"):
                if not self.id == "Exit":
                    self.show_data = True
                    self.what_to_print()
                else:
                    self.show_data = True
                    self.show_data_str == "In this room is {} \n{}\n".format(self.inventory, self.description)

            elif self.id == "Exit":
                if user_inp == "x":
                    if "key" in p.inventory:
                        gameExit = True

            elif user_inp[0:7] == "pick up":
                for j in self.inventory[::-1]:
                    if user_inp[8:-1] + user_inp[-1] == j:
                        p.inventory.append(j)
                        self.show_data_str = "You picked up: " + j + "\n"
                        self.show_data = True
                        self.inventory.remove(j)
                        break
            else:
                self.show_data = False
        else:
            self.show_data = False
