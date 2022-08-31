from moviepy import editor
from gtts import gTTS     
from mutagen.mp3 import MP3
from PIL import Image
from pathlib import Path
import os

def create_video(text, image_name):

    name = image_name[:-3]

    #Define the paths
    video_path = Path('lib\\video\\coinfessions\\'+name+'mp4')
    audio_path = Path('lib\\audio\\coinfessions\\'+name+'mp3')
    image_path = Path('lib\\images\\coinfessions\\'+image_name)
    gif_path = Path('lib\\gif\\coinfessions\\'+name+'gif')

    #Create a video from text
    tts = gTTS(text=text, lang='en', slow = False)
    try:
        tts.save(audio_path)
    except:
        os.mkdir('lib\\audio\\coinfessions')
        tts.save(audio_path)

    #Get the length of the audio file
    audio = MP3(audio_path)
    audio_length = audio.info.length
    
    image = Image.open(image_path).resize((1080, 1920), Image.ANTIALIAS)
     
    try:
        image.save(gif_path, duration=audio_length)
    except:
        os.mkdir('lib\\gif\\coinfessions\\')
        image.save(gif_path, duration=audio_length)

    print(gif_path)
    video = editor.VideoFileClip(gif_path)

    try:
        audio = editor.AudioFileClip(audio_path)
    except:
        os.mkdir('lib\\audio\\coinfessions\\')
        audio = editor.AudioFileClip(audio_path)

    final_video =  video.set_audio(audio)

    try:
        final_video.write_videofile(video_path, fps = 60)
    except:
        os.mkdir('lib\\video\\coinfessions\\')
        final_video.write_videofile(video_path, fps = 60)
