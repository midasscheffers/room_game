import time as t
import random as r

r.seed()

player_character = '@'

_map = []
x = 1
y = 1
prev_char = '0'

with open("MAP.map") as file:
    _map = file.read().split('\n')

gameRunning = True

def move(user_inp):
    global x
    global y
    global prev_char
    if (user_inp == "d" or user_inp == "D"):
            if(not _map[y][x+1] == '^'):
                _map[y] = _map[y][:x] + prev_char + _map[y][x+1:]
                x += 1
                prev_char = _map[y][x]
                _map[y] = _map[y][:x] + player_character + _map[y][x+1:]
            else:
                print("you can't move here")
    elif (user_inp == "a" or user_inp == "A"):
            if(not _map[y][x-1] == '^'):
                _map[y] = _map[y][:x] + prev_char + _map[y][x+1:]
                x -= 1
                prev_char = _map[y][x]
                _map[y] = _map[y][:x] + player_character + _map[y][x+1:]
            else:
                print("you can't move here")
    elif (user_inp == "s" or user_inp == "S"):
            if(not _map[y+1][x] == '^'):
                _map[y] = _map[y][:x] + prev_char + _map[y][x+1:]
                y += 1
                prev_char = _map[y][x]
                _map[y] = _map[y][:x] + player_character + _map[y][x+1:]
            else:
                print("you can't move here")
    elif (user_inp == "w" or user_inp == "W"):
            if(not _map[y-1][x] == '^'):
                _map[y] = _map[y][:x] + prev_char + _map[y][x+1:]
                y -= 1
                prev_char = _map[y][x]
                _map[y] = _map[y][:x] + player_character + _map[y][x+1:]
            else:
                print("you can't move here")


def map_gen(width, height):

    global _map
    new_map = ""
    new_map = new_map + '^'*height
    new_map = new_map + '\n'
    for i in range(height-2):
        new_map = new_map + '^'
        for j in range(width-2):
            randnum = r.randint(0, 1)
            if randnum == 0:
                new_map = new_map + '^'
            else:
                new_map = new_map + '0'
        new_map = new_map + '^'
        new_map = new_map + '\n'
    new_map = new_map + '^'*height

    _map = new_map.split('\n')



while True:
    #map_gen(10, 10)
    print(_map)
    print(_map[1])
    print(_map[1][2])
    t.sleep(2)
    print("\n"*100)
    name = input("What is your name: ")
    if (len(name) > 41):
        name = name[0:41]
    print("\n"*100)
    print("-"*64)
    print("| Begin your quest : {:^41} |".format(name))
    print("-"*64)
    print("this is the map")
    for i in range(len(_map)):
        print(_map[i])
    while gameRunning:
        user_inp = input(": ")
        print("\n"*100)
        move(user_inp)
        for i in range(len(_map)):
            print(_map[i])
