import random as r
import time as t
height = 10
width = 10
new_map = ""

def map_gen():
    global new_map
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

while True:
    print('\n'*100)
    map_gen()
    print(new_map)
    t.sleep(1)
