from PIL import Image

img = Image.new('RGB', size=(100, 60), color='#eb8634')
img.save('first.png')
img.show()     # Using ImageMagic on Linux