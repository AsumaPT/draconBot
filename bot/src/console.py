from colorama import Fore, Style, init
import os
from datetime import datetime

init()

dragon_ascii = """$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$Y/'$$$$P'a$$$$$$$$$$$$$$$$
$$$$$$$$$",` /,/,mT$$$$ d$$$$$$$$$$$$$$$$$
$$$$$l',` , '/d$$$$P^$a `^a`W$$$$$$$$$$$$$
$$l', ` ,   |d$$$P^$'   _  _ ==~a$$$$$$$$$
$l.`  .     \\'i$^4'   _eP$$$$$$$$$$$$$$$$$ 
l '  .         /   ,  $$$$' `$~$$$$$$$$$$$   ___  ___    _   ___ ___  _  _   _____   __
; ' ,              l /^' .,$oa$$$$$$$$$$$$  |   \\| _ \\  /_\\ / __/ _ \\| \\| | | _ \\ \\ / /
b ' ,        .     (_ ,1$$$$$$'$$$$$$$$$$$  | |) |   / / _ \\ (_| (_) | .` |_|  _/\\ V / 
$ , ,      .;       _$$$$$$$P $a$$$$$$$$$$  |___/|_|_\\/_/ \\_\\___\\___/|_|\\_(_)_|   |_|  
$, ,`    .$Ly        lM"^ ,  ,$$$$$$$'$$$$
$$, ,`   d$Liy      /'   edb $$$$$$$'$$$$$
$$$$,,'. $$$Li     (    d$$$$$$$$$$'$$$$$$
$$$$$$,' v$$$Li4.   `  `Q$$$$$$$P',$$$$$$$
$$$$$$$$,$$$$$$$L44., . .     ,,;d$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
"""

clear = lambda: os.system('cls')
printDragon = lambda: print(f'{Fore.RED}{dragon_ascii}{Style.RESET_ALL}')
printAvaiable = lambda: print(f'{Fore.RED}[DRACON] Update avaiable!{Style.RESET_ALL}')

def printUptodate(version):
	print(f'{Fore.RED}[DRACON] Version: {version}{Style.RESET_ALL}')
	print(f'{Fore.RED}[DRACON] Author: Asuma{Style.RESET_ALL}')

def printPixel(x, y, color):
	h = datetime.now()
	horas = f'{h.strftime("%H")}:{h.strftime("%M")}:{h.strftime("%S")}'
	print(f'{Fore.GREEN}[{horas}]: Pixel placed at {x}, {y}, color: {color}.{Style.RESET_ALL}')

def printRefuse(x, y, color):
	h = datetime.now()
	horas = f'{h.strftime("%H")}:{h.strftime("%M")}:{h.strftime("%S")}'
	print(f'{Fore.RED}[{horas}]: Pixel failed placing at {x}, {y}, color: {color}.{Style.RESET_ALL}')

def printCaptcha():
	h = datetime.now()
	horas = f'{h.strftime("%H")}:{h.strftime("%M")}:{h.strftime("%S")}'
	print(f'{Fore.YELLOW}[{horas}]: Captcha, please solve it and then press enter.{Style.RESET_ALL}')



def printFinished(template, pixeisc):
	h = datetime.now()
	horas = f'{h.strftime("%H")}:{h.strftime("%M")}:{h.strftime("%S")}'
	print(f'{Fore.BLUE}[{horas}]: Template finished! Dracon placed in total ({pixeisc} pixels.) ')

def printAssist(x, y, color):
	h = datetime.now()
	horas = f'{h.strftime("%H")}:{h.strftime("%M")}:{h.strftime("%S")}'
	print(f'{Fore.LIGHTGREEN_EX}[{horas}]: Assist pixel placed at {x}, {y}, color: {color}.{Style.RESET_ALL}')

def printAttack(x,y,color):
	h = datetime.now()
	horas = f'{h.strftime("%H")}:{h.strftime("%M")}:{h.strftime("%S")}'
	print(f'{Fore.LIGHTRED_EX}[{horas}]: Attack pixel placed at {x}, {y}, color: {color}.{Style.RESET_ALL}')

def printGetChunks():
	print(f'{Fore.LIGHTCYAN_EX}[DRACON] Downloading chunks.{Style.RESET_ALL}')

def printCompare():
	print(f'{Fore.LIGHTCYAN_EX}[DRACON] Comparing template.{Style.RESET_ALL}')

def printConnection():
	print(f'{Fore.LIGHTCYAN_EX}[DRACON] Connecting to the websocket.{Style.RESET_ALL}')

def printCalculating():
	print(f'{Fore.LIGHTCYAN_EX}[DRACON] Calculating order of pixels.{Style.RESET_ALL}')


