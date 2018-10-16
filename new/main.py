from classes.world import *
from classes.room import *
from classes.player import *

import time as t
import random
import os

def item_spawn(r):
    randnum = random.randint(0,11)
    if randnum == 10:
        r.inventory.append("sword")
    randnum = random.randint(0,21)
    if randnum >= 15:
        r.inventory.append("healing potion")

def spawn_monster(r):
    randnum = random.randint(0,31)
    if randnum >= 30:
        r.monsterHere = True

def set_up_rooms(world, rooms):
    rooms = []
    for y in range(world.height-1):
        for x in range(world.width-1):
            if world._map[y][x] == "!":
                r = room(x, y)
                r.inventory = []
                r.description = "There seems to be an exit here. Do you go in?......\nType \"x\" to exit, You need a key"
                r.id = "Exit"
                item_spawn(r)
                spawn_monster(r)
                rooms.append(r)
            elif not world._map[y][x] == world.wall_char:
                r = room(x, y)
                item_spawn(r)
                spawn_monster(r)
                r.description = "there is nothing exeptional here"
                r.id = (x, y)
                rooms.append(r)

    # for room in rooms:
    for j in range(len(rooms)):
        if rooms[j].id == (1, 1):
            rooms[j].monsterHere = False
    randroom = random.randint(0, len(rooms)-1)
    rooms[randroom].inventory.append("key")
    return rooms


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n")


def print_menu_line(text):
    print("| {:<61}|".format(text))


def print_UI(world, rooms, player):
    print('-'*64)
    print_menu_line("Player Name : {:^46}".format(player.name))
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
    print_menu_line("use \"Item\" - use an Item in the current room")
    print('-'*64)
    print("\n")
    world.draw_map(player.draw_player(world._map))
    print("\n")
    print_health(rooms, player)
    print("\n")
    # for room in rooms:
    for room in rooms:
        room.print_data()
    player.print_data()

def print_health(rooms, player):
    print("your score is: " + str(player.score))
    print("Your health is: " + str(player.health))
    for room in rooms:
    # for i in range(len(rooms)):
        if room.x == player.x and room.y == player.y:
            if room.monsterHere:
                print("monsters health is: {}".format(room.monsterHealth))
                print("\n")


def room_logics(user_inp, world, rooms, player):
    for room in rooms:
    # room.room_logic(user_inp,p)
    # for i in range(len(rooms)):
        rooms = room.room_logic(user_inp, world, player)



def game_loop(world, rooms, player):
    user_inp = ""
    while not user_inp == "q":
        user_inp = input(': ').lower()
        clear()
        player.move(user_inp, world)
        room_logics(user_inp, world, rooms, player)
        player.player_logic(user_inp, rooms)
        if player.health <= 0:
            clear()
            print("you died")
            print("your score was: " + str(player.score))
            t.sleep(2)
            break
        if world.reset:
            world.random_map(10, 20)
            rooms = set_up_rooms(world, player)
            world.reset = False
        print_UI(world, rooms, player)

        # if user_inp == "q":
        #     gameExit = True


def main():
    w = world()
    p = player()
    rooms = []

    w.random_map(10, 20)

    rooms = set_up_rooms(w, rooms)

    clear()

    name = input('what is your name: ')
    if (len(name) > 41):
        name = name[0:41]

    clear()
    p.name = name
    print("-"*64)
    print("| Begin your quest : {:^41} |".format(p.name))
    print("-"*64)
    print("\n")
    print("this is the map")
    print("\n")
    w.draw_map(p.draw_player(w._map))
    print("\n")
    print("Press Enter!")
    print("\n")

    game_loop(w, rooms, p)

        # while not gameExit:
        #
        #     user_inp = input(': ').lower()
        #     clear()
        #     p.move(user_inp, w._map)
        #     room_logics(user_inp)
        #     p.player_logic(user_inp, rooms)
        #     print_UI()
        #     if user_inp == "q":
        #         gameExit = True


main()
