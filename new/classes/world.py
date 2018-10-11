import random

class world:

    def __init__(self):
        self._map = []
        self.normalChar = ' '
        self.wall_char = '█'
        self.reset = False

        with open("MAP.map") as file:
            self._map = file.read().split('\n')

        self.height = len(self._map)
        self.width = len(self._map[0])


    def draw_map(self, m):
        for i in range(len(m)):
            print(m[i])


    def random_map(self, height, width):
        random.seed()
        new_map = ""
        new_map = new_map + self.wall_char*width
        new_map = new_map + '\n'

        for i in range(height-2):
            new_map = new_map + self.wall_char
            for j in range(width-2):
                randnum = random.randint(0, 3)
                if randnum == 0:
                    new_map = new_map + self.wall_char
                else:
                    new_map = new_map + self.normalChar
            new_map = new_map + self.wall_char
            new_map = new_map + '\n'

        new_map = new_map + '\n'
        new_map = new_map + self.wall_char*width

        new_map = new_map.split('\n')

        new_map[1] = new_map[1][:1] + self.normalChar + new_map[1][2:]
        new_map[height-1] = new_map[height-2][:width-2] + "!" + new_map[height-2][width-1:]

        self._map = new_map

        self.height = len(self._map)
        self.width = len(self._map[0])
