import clipboard
import Image

im1 = clipboard.get_image(idx=0)
im2 = clipboard.get_image(idx=1)
_1 = im1.resize((366,650),Image.ANTIALIAS)
_2 = im2.resize((366,650),Image.ANTIALIAS)
background = Image.new('RGBA', (746,650), (255, 255, 255, 255))
background.paste(_1,(0,0))
background.paste(_2,(380,0))
background.show()

clipboard.set_image(background)
