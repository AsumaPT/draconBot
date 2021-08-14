# Libraries
from PIL import Image
from math import floor
from urllib.request import urlopen


# Variables
chunks_to_get = []


# Get chunks 
def getChunksIds(world, xi, yi, xf, yf):

	pos1 = 0
	pos2 = 0

	world = "art" if world == "art" else "world"

	if (xf % 256 != 0 and xf != 0):
			pos1 = 1
	if (yf % 256 != 0 and yf != 0):
			pos2 = 1

	firstChunkX = floor(xi / 256)
	firstChunkY = floor(yi / 256)

	lastChunkX = floor(xf / 256)+pos1
	lastChunkY = floor(yf / 256)+pos2

	chunksXtoGet = lastChunkX - firstChunkX 
	chunksYtoGet = lastChunkY - firstChunkY

	chunksXGot = 0
	chunksYGot = 0

	canvas = Image.new('RGB', (256*chunksXtoGet, 256*chunksYtoGet))

	for y in range(firstChunkY, firstChunkY+chunksYtoGet):
		for x in range(firstChunkX, firstChunkX+chunksXtoGet):
			chunks_to_get.append([xi+x,yi+y])
			chunk = Image.open(urlopen(f"https://api.henrixounez.com/pixworld/chunk/{world}/{x}/{y}"))
			canvas.paste(chunk, (256*chunksXGot, 256*chunksYGot))
			chunksXGot = chunksXGot + 1
		chunksXGot = 0
		chunksYGot = chunksYGot + 1

	CoordXi = abs((firstChunkX*256)-xi)
	CoordYi = abs((firstChunkY*256)-yi)

	CoordXfCrop = xf-xi
	CoordYfCrop = yf-yi

	template = canvas

	template = template.crop((CoordXi, CoordYi, CoordXi+CoordXfCrop, CoordYi+CoordYfCrop))
	template.convert('RGBA')

	return template
 
