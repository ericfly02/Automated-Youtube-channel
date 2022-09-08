import os
from  youtube import yt_Class 
from googleapiclient.errors import HttpError
from oauth2client.tools import argparser


def initialize(video_path, name, count):
  #yt = yt_Class()
  current_path =str(os.path.abspath(__file__))
  path = current_path[:-15]
  path_file = path+video_path
  argparser.add_argument(path_file)
  title = name
  argparser.add_argument(title)
  description = "anonymous crypto confessions by @illustratealpha"
  argparser.add_argument(description)
  category = '24'
  argparser.add_argument(category)
  keywords = "anonymous, crypto, confessions, #shorts, #short, #enterpreneur"
  argparser.add_argument(keywords)
  privacyStatus = 'private'
  argparser.add_argument(privacyStatus)

  args = argparser.parse_args()
  
  youtube = yt_Class.get_authenticated_service(args)
  try:
    yt_Class.initialize_upload(youtube, args)
  except HttpError as e:
    print ("An HTTP error %d occurred:\n%s" % (e.resp.status, e.content))