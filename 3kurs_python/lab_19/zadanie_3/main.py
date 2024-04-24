from PIL import Image
image = Image.open("risunok2.jpg")
width, height = image.size
red_sum = green_sum = blue_sum = 0
for x in range(width):
    for y in range(height):
        r, g, b = image.getpixel((x, y))
        red_sum += r
        green_sum += g
        blue_sum += b

total_pixels = width * height
avg_red = red_sum // total_pixels
avg_green = green_sum // total_pixels
avg_blue = blue_sum // total_pixels
print(f"Среднее значение R: {avg_red}")
print(f"Среднее значение G: {avg_green}")
print(f"Среднее значение B: {avg_blue}")
image.show()
