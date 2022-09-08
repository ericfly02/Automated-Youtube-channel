from PIL import Image
from pytesseract import pytesseract
from pathlib import Path
import os
import time
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


def initialize(username):

    print('-----------------------------------------------------------')
    print('|                       CREATING VIDEO                    |')
    print('-----------------------------------------------------------')

    #Define path to image
    try:
        path_to_image = Path('lib\\images\\'+username)
    except:
        os.mkdir('lib\\images\\'+username)
        path_to_image = Path('lib\\images\\'+username)

    #Array to store all the image names
    filenames = next(os.walk(path_to_image), (None, None, []))[2]  # [] if no file

    count = 0
    for name in filenames:
        # Save text from image to "new_text" variable
        print('\n---------------------- '+name+' ----------------------')
        path = Path('lib\\images\\'+username+'\\' + name)
        text = create_text(path)
        words = text.split()
        new_text = " ".join(words[1:])
        create_video(new_text, name, username, count)

        #we wait 1 day to upload the next video
        time.sleep(86400)

    
    
