'''
def cupcake():
    local_flavorr = "Bread"
local_flavorr = "Water"
print(local_flavorr)
'''
from minecraft import *

'''
def create_egyptian_pyramid(base_area, block_type, position):
    # Make sure the base is odd
    if base % 2 == 0:
        base += 1

    # Calculate height of the pyramid based on its base
    height = base // 2 + 1

    for y in range(height):
        for x in range(position.x - y, position.x + base - y):
            for z in range(position.z - y, position.z + base - y):
                setblock(x, position.y + y, z, block_type)

# Get the player's position
player_position = getpos()

# Create a pyramid of base 21, made of sand, at the player's position
create_egyptian_pyramid(21, 4, player_position)

'''
'''
import math
def egyptian_pyramid(base_size, block_type):
    position = getpos()
    x = position.x
    y = position.y
    z = position.z
    a = int(math.sqrt(base_size)-1)
    setblocks(x,y,z,x+a,y,z+a,block_type)
    k = True
    cd = 1
    while k is True:
        setblocks(x+cd,y+cd,z+cd,x+a-cd,y+cd,z+a-cd,block_type)
        cd+=1 
        if z+a-cd < 1:
            break


egyptian_pyramid(36,24)
'''
'''
import time


for i in range(20):
    position = getpos()
    x = position.x
    y = position.y
    z = position.z
    setblocks(x,y,z,x+50,y+2,z+50, 46)
    time.sleep(15)
'''
