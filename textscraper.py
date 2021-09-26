from PIL import Image
from pytesseract import pytesseract

img = Image.open("/Users/cmkarako/Desktop/Screen Shot 2021-09-25 at 11.38.29 PM.png")

text = pytesseract.image_to_string(img)

print(text[:-1])