import os, time
from PIL import Image
import json
import ctypes
from pypresence import Presence
import time
import threading

from src.chunks import getChunksIds
from src.compare import compare
from src.pixworld import *
from src.strategy import *
from src.console import printFinished, printGetChunks, printCompare, printConnection, printCalculating


def hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b).upper()

def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

"""
def pixelUpdate(ws, xi, yi, xf, yf):
	global pixelStack
	print("b")
	while True:
		data = json.loads(ws.recv())
		if data["type"] == "placePixel":
			x = data["data"]["x"]
			y = data["data"]["y"]
			color = hex_to_rgb(data["data"]["color"])
			pixel = [x,y,color]
			if pixel not in pixelPlaced:
				if pixel in pixelStack:
					pixelStack.pop(pixelStack.index(pixel))
					printAssist(x, y, color)
				else:
					if  x >= xi and y >= yi and x <= xf and y <= yf:
						pixelStack.append(pixel)
						printAttack(x, y, color)"""

def richPresence():
	rpc = Presence("876161456717041694")
	rpc.connect()
	return rpc

totais = 0
erros = 0
count = 0

def loopPrecense(rpc, templat, start):
	while True:
		updateRich(rpc,templat,start)
		time.sleep(5)

def updateRich(rpc, templat, strat):

	rpc.update(large_image="logo", large_text=f"{strat}", details=f"Template: {templat}",  state=f"Pixels: ({(totais-erros)+count}/{totais})")


def startTemplate(world, x, y, templat, strat, option=None):
	global totais, erros, count
	path = os.getcwd()
	template = Image.open(os.path.dirname(path)+'\\bot\\images\\'+templat)
	printGetChunks()
	canvas = getChunksIds(world, x, y, x+template.width, y+template.height)
	printCompare()
	pixelStack, erros, totais = compare(template, canvas, x, y)

	hashG = generateHash()

	f = open(os.path.dirname(path)+'\\bot\\config.json')
	data = json.load(f)
	account = data["account"]["active"]

	printConnection()
	if account:
		username = data["account"]["username"]
		password = data["account"]["password"]

		token = getAccount(username, password)
		ws = connect(hashG, token)
	else:
		ws = connect(hashG)

	printCalculating()
	if strat == "random":
		pixelStack = randomizar(pixelStack)
	elif strat == "linear":
		pass
	elif strat == "columns":
		pixelStack = columns(pixelStack)
	elif strat == "checkers":
		pixelStack = checkers(pixelStack)
	elif strat == "lines":
		pixelStack = lines(pixelStack)
	elif strat == "diagonal":
		pixelStack = diagonal(pixelStack)
	elif strat == "spiral":
		pixelStack = spiral(pixelStack, x, y, template.width, template.height)
	elif strat == "linear-random":
		pixelStack = randomlinear(pixelStack)
	elif strat == "diagonal-right":
		pixelStack = rightdiagonal(pixelStack)
	elif strat == "horizontal":
		pixelStack = horizontal(pixelStack)
	elif strat == "circle":
		pixelStack = circle(pixelStack, x, y, template.width, template.height)
	elif strat == "zigzag":
		pixelStack = alternativelinear(pixelStack)

	count = 0
	
	if option == "reverse" or option == "reversed" or option == "inverted" or option == "invert":
		pixelStack = pixelStack[::-1]
	try:
		rpc = richPresence()
		threading.Thread(target=loopPrecense, args=(rpc, templat, strat)).start()
	except: 
		pass
	while(len(pixelStack) > 0):
		i = pixelStack[0]
		x = i[0]
		y = i[1]
		hexcolor = hex(i[2][0],i[2][1],i[2][2])
		response = placePixel(ws, world, x, y, hexcolor)
		time.sleep(0.2)
		if type(response) == int:
			pixelStack.pop(0)
			count+=1
			ctypes.windll.kernel32.SetConsoleTitleW(f"DRACON BOT | {templat} ({(totais-erros)+count}/{totais}) | {round((100*((totais-erros)+count))/totais, 2)}%")
			if response >= 50:
				time.sleep(4)
		elif response == "captcha":
			input()

	printFinished(templat, count)
			



