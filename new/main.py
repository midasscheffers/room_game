from classes.world import *
from classes.room import *
from classes.player import *

import time as t
import random
import os

#global gameExit
gameExit = False
#global Exit
Exit = False

w = world()
p = player()
rooms = []

w.random_map(10, 20)
def item_spawn(r):
    randnum = random.randint(0,11)
    if randnum == 10:
        r.inventory.append("sword")
    randnum = random.randint(0,21)
    if randnum >= 20:
        r.inventory.append("healing potion")

def spawn_monster(r):
    randnum = random.randint(0,31)
    if randnum >= 30:
        r.monsterHere = True

def set_up_rooms():
    global rooms
    rooms = []
    for y in range(w.height-1):
        for x in range(w.width-1):
            if w._map[y][x] == "!":
                r = room(x, y)
                r.inventory = []
                r.description = "There seems to be an exit here. Do you go in?......\nType \"x\" to exit, You need a key"
                r.id = "Exit"
                item_spawn(r)
                spawn_monster(r)
                rooms.append(r)
            elif not w._map[y][x] == '^':
                r = room(x, y)
                item_spawn(r)
                spawn_monster(r)
                r.description = "there is nothing exeptional here"
                r.id = (x, y)
                rooms.append(r)

    for j in range(len(rooms)):
        if rooms[j].id == (1, 1):
            rooms[j].monsterHere = False
    randroom = random.randint(0, len(rooms)-1)
    rooms[randroom].inventory.append("key")


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n")


def print_menu_line(text):
    print("| {:<61}|".format(text))


def print_UI():
    print('-'*64)
    print_menu_line("Player Name : {:^46}".format(p._name))
    print_menu_line(' ')
    print_menu_line("Commands :")
    print_menu_line(' ')
    print_menu_line("w - move Up")
    print_menu_line("a - move Left")
    print_menu_line("s - move Down")
    print_menu_line("d - move Right")
    print_menu_line("q - quit game.. !data wil be lost")
    print_menu_line("data - get room data")
    print_menu_line("pick up \"Item\" - Wil put an item from a room in you inventory")
    print_menu_line("drop \"Item\" - drop a seleted item from inventory to room")
    print_menu_line("i - show inventory")
    print('-'*64)
    print("\n")
    w.draw_map(p.draw_player(w._map))
    print("\n")
    print_health()
    print("\n")
    for i in range(len(rooms)):
        rooms[i].print_data()

def print_health():
    print("Your health is: " + str(p.health))
    print("\n")
    for i in range(len(rooms)):
        if rooms[i].x == p.x and rooms[i].y == p.y:
            if rooms[i].monsterHere == True:
                print("monsters health is: {}".format(rooms[i].monsterHealth))
                print("\n")


def room_logics(user_inp):
    for i in range(len(rooms)):
        rooms[i].room_logic(user_inp, p)


def player_logic(user_inp):
    if user_inp == "i":
        print(p.inventory)
        print("\n")

    if user_inp[0:4] == "drop":
        for i in range(len(rooms)):
            if rooms[i].x == p.x and rooms[i].y == p.y:
                for j in p.inventory[::-1]:
                    if user_inp[5:-1] + user_inp[-1] == j:
                        rooms[i].inventory.append(j)
                        print("You droped: " + j)
                        print("\n")
                        p.inventory.remove(j)
                        break


while not Exit:
    gameExit = False
    set_up_rooms()
    clear()
    name = input('what is your name: ')
    if (len(name) > 41):
        name = name[0:41]
    clear()
    p = player()
    p._name = name
    print("-"*64)
    print("| Begin your quest : {:^41} |".format(p._name))
    print("-"*64)
    print("\n")
    print("this is the map")
    print("\n")
    w.draw_map(p.draw_player(w._map))
    print("\n")
    print("Press Enter!")
    print("\n")

    while not gameExit:

        user_inp = input(': ').lower()
        clear()
        p.move(user_inp, w._map)
        room_logics(user_inp)
        player_logic(user_inp)
        print('\n')
        print_UI()
        if user_inp == "q":
            gameExit = True
        if(not p.moved):
            print('you can\'t move here')
            print('\n')
