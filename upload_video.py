from Google import Create_Service
from googleapiclient.http import MediaFileUpload

def initialize(video_path, name, count):
  CLIENT_SECRET_FILE = 'client_secrets.json'
  API_NAME = 'youtube'
  API_VERSION = 'v3'
  SCOPES = ['https://www.googleapis.com/auth/youtube.upload']

  service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

  request_body = {
      'snippet': {
          'categoryI': 24,
          'title': name,
          'description': "anonymous crypto confessions number {count} by @illustratealpha".format(count=count),
          'tags': ['crypto', 'btc', '#shorts', 'coinfessions', 'short', 'shorts', 'enterpreneur']
      },
      'status': {
          'privacyStatus': 'public',
          'selfDeclaredMadeForKids': False, 
      },
      'notifySubscribers': True
  }

  mediaFile = MediaFileUpload(video_path)

  service.videos().insert(
      part='snippet,status',
      body=request_body,
      media_body=mediaFile
  ).execute()
