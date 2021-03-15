#Version
version = "1.0.0"

#Imports
import os

#For Console Colors
os.system("cls")

#File Path
path=os.path.realpath(__file__)
path = path.split("\\")
folder = ""
file = ""
for i in range(len(path)):
    if i == len(path) - 1:
        file = path[i]
    else:
        folder += path[i] + "\\"
os.chdir(folder)

#Import The Bot
from lib.bot import Bot


#Variables
#Change The Prefix To Anything You Like
prefix = "!"
#Add The Owners' Id's As An Integer List
ownersId = []


#Start The Bot
bot = Bot(prefix, ownersId)
bot.run(version)