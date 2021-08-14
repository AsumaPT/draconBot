from PIL import Image
def compare(template, canvas, xi, yi):

    img = template.convert('RGBA')
    canvas = canvas.convert('RGBA')

    width = template.width
    height = template.height

    transparent = 0
    erros = 0

    pixels = []

    for y in range(height):
        for x in range(width):
            ri, gi, bi, ai = img.getpixel((x,y))
            rc, gb, bc, ac = canvas.getpixel((x,y))
            if ai == 0:
                transparent+=1
                continue
            if ri == rc and gi == gb and bi == bc:
                continue
            pixels.append([x+xi,y+yi,(ri,gi,bi)])
            erros+=1

    return pixels, erros, (canvas.width * canvas.height) - transparent