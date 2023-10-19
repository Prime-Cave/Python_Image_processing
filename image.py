from PIL import Image, ImageFilter

im = Image.open('pokedex/pikachu.jpg')
filtered_image = im.filter(ImageFilter.BLUR)
#filtered_image.save('blur.png', 'png')
filtered_image.show()
print(im.size, im.width, im.mode)