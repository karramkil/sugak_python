from PIL import Image
image = Image.open("risunok3.jpg")
bw_image = image.convert("L")
mirrored_image = bw_image.transpose(Image.FLIP_LEFT_RIGHT)
new_width = 400
new_height = 300
resized_image = mirrored_image.resize((new_width, new_height))
resized_image.save("risunok4.jpg")

print("Изображение успешно обработано и сохранено в файл risunok4.jpg")
input()
