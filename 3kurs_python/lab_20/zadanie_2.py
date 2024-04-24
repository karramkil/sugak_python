from PIL import Image, ImageDraw

def draw_mouse():
    image = Image.new('RGB', (300, 300), (0, 255, 0))
    draw = ImageDraw.Draw(image)

    draw.ellipse((100, 150, 200, 250), fill=(128, 128, 128))

    draw.ellipse((125, 100, 175, 150), fill=(128, 128, 128))

    draw.polygon([(115, 100), (125, 100), (120, 110)], fill=(128, 128, 128))
    draw.polygon([(165, 100), (175, 100), (170, 110)], fill=(128, 128, 128))

    draw.ellipse((135, 110, 145, 120), fill=(255, 255, 255))
    draw.ellipse((155, 110, 165, 120), fill=(255, 255, 255))

    draw.polygon([(145, 125), (155, 125), (150, 135)], fill=(255, 255, 255))

    draw.polygon([(200, 200), (195, 205), (190, 200)], fill=(128, 128, 128))

    draw.ellipse((160, 170, 180, 190), fill=(255, 255, 0))
    image.save('mouse.png')

draw_mouse()
