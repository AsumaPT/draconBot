# Packages

import sys
import time
import ctypes

from src.update import checkUpdate
from src.template import startTemplate
from src.console import *

# Variables

version = 1.0

# Main

clear()
ctypes.windll.kernel32.SetConsoleTitleW("DRACON BOT v"+str(version))
uptodate = checkUpdate(version)
printDragon()

if uptodate:
	printUptodate(version)
else:
	printAvaiable()
	sys.exit()

canvas = sys.argv[1]
x = int(sys.argv[2])
y = int(sys.argv[3])
template = sys.argv[4]
try:
	strategy = sys.argv[5]
except:
	strategy = "random"

try:
	option = sys.argv[6]
except:
	pass


time.sleep(2)
clear()
startTemplate(canvas, x, y, template, strategy, option=None)
    
