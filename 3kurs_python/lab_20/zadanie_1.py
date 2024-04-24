from PIL import Image, ImageDraw

def draw_letter(draw, letter, x, y, fill):
    if letter == 'К':
        draw.polygon([(x, y), (x + 50, y), (x + 50, y + 50), (x + 25, y + 25), (x, y + 50)], fill=fill)
    elif letter == 'а':
        draw.ellipse((x, y, x + 50, y + 50), fill=fill)
    elif letter == 'р':
        draw.polygon([(x, y), (x + 50, y), (x + 50, y + 50), (x + 25, y + 50), (x, y + 50)], fill=fill)
    elif letter == 'и':
        draw.polygon([(x, y), (x + 50, y), (x + 50, y + 50), (x, y + 50)], fill=fill)
    elif letter == 'н':
        draw.polygon([(x, y), + 50, y, (x + 50, y + 50), (x + 25, y + 25), (x, y + 50)], fill=fill)
    elif letter == 'а':
        draw.ellipse((x, y, x + 50, y + 50), fill=fill)

def draw_name():
    name = 'Карина'
    image = Image.new('RGB', (300, 100), (255, 255, 255))
    draw = ImageDraw.Draw(image)
    for i, letter in enumerate(name):
        draw_letter(draw, letter, i * 50, 0, (0, 0, 0))
    image.save('name.png')

draw_name()
