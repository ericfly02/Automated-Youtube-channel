from posixpath import split
from PIL import Image
from pytesseract import pytesseract
from pathlib import Path
from os import walk
from text_to_video import create_video

def create_text(path_to_image):

    #Define path to tessaract.exe
    path_to_tesseract = Path("C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe")

    #Point tessaract_cmd to tessaract.exe
    pytesseract.tesseract_cmd = path_to_tesseract

    #Open image with PIL
    img = Image.open(path_to_image)

    #Extract text from image
    text = pytesseract.image_to_string(img)

    return text


#def initialize():

#Define path to image
path_to_image = Path('lib\\images\\coinfessions')
#Array to store all the image names
filenames = next(walk(path_to_image), (None, None, []))[2]  # [] if no file

for name in filenames:
    # Save text from image to "new_text" variable
    path = Path('lib\\images\\coinfessions\\' + name)
    text = create_text(path)
    words = text.split()
    new_text = " ".join(words[1:])
    create_video(new_text, name)

    
    
