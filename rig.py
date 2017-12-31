import time
import sys
import random
from mcpi.minecraft import Minecraft

# Create the Minecraft game
mc = Minecraft.create()


def growTree(x, y, z):
    # Creates a tree at the coordinates given
    blockType = 6
    mc.setBlock(x, y, z, blockType, 3)


def forest(count, dim):
    count, dim = int(count), int(dim)
    pos = mc.player.getTilePos()
    x = pos.x
    y = pos.y
    z = pos.z
    for num in range(count):
        growTree(
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
