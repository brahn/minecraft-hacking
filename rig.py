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


def speed_build(length, width, height, blockType):
    length, width, height, blockType = map(
        int, [length, width, height, blockType])
    pos = mc.player.getPos()
    x = pos.x
    y = pos.y
    z = pos.z
    mc.setBlocks(x, y, z, x + width, y + height, z + length, blockType)
    length = length - 2
    height = height - 2
    width = width - 2
    blockType = 0
    x = x + 1
    y = y + 1
    z = z + 1
    mc.setBlocks(x, y, z, x + width, y + height, z + length, blockType)


def growPlant(x, y, z, blockType=6):
    # Creates a tree at the coordinates given
    mc.setBlock(x, y, z, blockType, 3)


# Carrots not working, TO DO
def grow(count, dim, blockType):
    count, dim, blockType = int(count), int(dim), int(blockType)
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


def bw():
    mc.postToChat("Prepare for battle!")
    time.sleep(60)
    blockHits = mc.events.pollBlockHits()
    print("block hits: " + str(blockHits))
    n = len(blockHits)
    mc.postToChat("your score is " + str(n))


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

