from PIL import Image,ImageGrab
import pytesser

def image_tess(pathname):
    im = Image.open(pathname)
    text = pytesser.image_to_string(im)
    return text
