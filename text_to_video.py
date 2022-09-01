from moviepy import editor
from gtts import gTTS     
from mutagen.mp3 import MP3
from PIL import Image
from pathlib import Path
import os

def create_video(text, image_name, username):

    name = image_name[:-3]

    #Define the paths
    video_path = str(Path('lib\\video\\'+username+'\\'+name+'mp4'))
    audio_path = str(Path('lib\\audio\\'+username+'\\'+name+'mp3'))
    image_path = Path('lib\\images\\'+username+'\\'+image_name)
    gif_path = str(Path('lib\\gif\\'+username+'\\'+name+'gif'))

    #Create a video from text
    tts = gTTS(text=text, lang='en', slow = False)

    if not Path(audio_path).is_file():
        try:
            tts.save(audio_path)
        except:
            os.mkdir('lib\\audio\\'+username)
            tts.save(audio_path)
    else:
        print("Audio file already exists")

    #Get the length of the audio file
    audio = MP3(audio_path)
    
    audio_length = audio.info.length
    
    image = Image.open(image_path).resize((1080, 1920), Image.ANTIALIAS)
    
    if not Path(gif_path).is_file():
        try:
            image.save(gif_path, duration=audio_length)
        except:
            os.mkdir('lib\\gif\\'+username+'\\')
            image.save(gif_path, duration=audio_length)
    else:
        print(audio)
        print("Gif file already exists")

    video = editor.VideoFileClip(gif_path)
    audio = editor.AudioFileClip(audio_path)
    final_video =  video.set_audio(audio)

    if not Path(video_path).is_file():
        try:
            final_video.write_videofile(video_path, fps = 60)
        except:
            os.mkdir('lib\\video\\'+username+'\\')
            final_video.write_videofile(video_path, fps = 60)
    else:
        print("Video file already exists")
