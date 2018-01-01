import time
import sys
import random
from mcpi.minecraft import Minecraft

# Create the Minecraft game
mc = Minecraft.create()

# Plant dictionary
PLANT_KINDS = {
    # "Acacia": 6,
    "Carrots": 141,
    "Allium": 38,
    "Cactus": 81,
    "Jungle": 6,
}


def growPlant(x, y, z, blockType=6):
    # Creates a tree at the coordinates given
    mc.setBlock(x, y, z, blockType, 3)


# Carrots not working, TO DO
def grow(count, dim, kind):
    blockType = PLANT_KINDS.get(kind)
    count, dim = int(count), int(dim)
    pos = mc.player.getTilePos()
    x = pos.x
    y = pos.y
    z = pos.z
    for num in range(count):
        growPlant(
            x + random.randint(-dim, dim),
            y,
            z + random.randint(-dim, dim),
            blockType=blockType)


def list_grow():
    plants = ','.join(PLANT_KINDS.keys())
    mc.postToChat(plants)


def forest(count, dim):
    count, dim = int(count), int(dim)
    pos = mc.player.getTilePos()
    x = pos.x
    y = pos.y
    z = pos.z
    for num in range(count):
        growPlant(
            x + random.randint(-dim, dim),
            y,
            z + random.randint(-dim, dim))


# Game loop
while True:
    time.sleep(.2)

    # Get all the chat events
    chats = mc.events.pollChatPosts()

    # For each chat, execute the command!
    for chat in chats:
        print(chat.message)
        command = chat.message.split()[0]
        args = chat.message.split()[1:]
        print(args)
        function = getattr(sys.modules[__name__], command)
        args = function(*args)
