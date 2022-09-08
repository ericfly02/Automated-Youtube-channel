import httplib2
import os
import random
import sys
import time

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import run_flow

class yt_Class:

    def __init__(self):
        # Explicitly tell the underlying HTTP transport library not to retry, since
        # we are handling retry logic ourselves.
        httplib2.RETRIES = 1

        # Maximum number of times to retry before giving up.
        self.MAX_RETRIES = 10

        # Always retry when these exceptions are raised.
        self.RETRIABLE_EXCEPTIONS = (httplib2.HttpLib2Error, IOError)

        # Always retry when an apiclient.errors.HttpError with one of these status
        # codes is raised.
        self.RETRIABLE_STATUS_CODES = [500, 502, 503, 504]

        self.CLIENT_SECRETS_FILE = "client_secrets.json"

        # This OAuth 2.0 access scope allows an application to upload files to the
        # authenticated user's YouTube channel, but doesn't allow other types of access.
        self.YOUTUBE_UPLOAD_SCOPE = "https://www.googleapis.com/auth/youtube.upload"
        self.YOUTUBE_API_SERVICE_NAME = "youtube"
        self.YOUTUBE_API_VERSION = "v3"

        # This variable defines a message to display if the CLIENT_SECRETS_FILE is
        # missing.
        self.MISSING_CLIENT_SECRETS_MESSAGE = """
        WARNING: Please configure OAuth 2.0

        To make this sample run you will need to populate the client_secrets.json file
        found at:

        %s

        with information from the API Console
        https://console.developers.google.com/

        For more information about the client_secrets.json file format, please visit:
        https://developers.google.com/api-client-library/python/guide/aaa_client_secrets
        """ % os.path.abspath(os.path.join(os.path.dirname(__file__),
                                        self.CLIENT_SECRETS_FILE))

        self.VALID_PRIVACY_STATUSES = ("public", "private", "unlisted")


    def get_authenticated_service(args):
        yt = yt_Class()
        flow = flow_from_clientsecrets(yt.CLIENT_SECRETS_FILE,
            scope=yt.YOUTUBE_UPLOAD_SCOPE,
            message=yt.MISSING_CLIENT_SECRETS_MESSAGE)

        storage = Storage("%s-oauth2.json" % sys.argv[0])
        credentials = storage.get()

        if credentials is None or credentials.invalid:
            credentials = run_flow(flow, storage, args)

        return build(yt.YOUTUBE_API_SERVICE_NAME, yt.YOUTUBE_API_VERSION,
            http=credentials.authorize(httplib2.Http()))

    def initialize_upload(youtube, options):
        yt = yt_Class()
        tags = None
        if options.keywords:
            tags = options.keywords.split(",")

        body=dict(
            snippet=dict(
            title=options.title,
            description=options.description,
            tags=tags,
            categoryId=options.category
            ),
            status=dict(
            privacyStatus=options.privacyStatus
            )
        )

        # Call the API's videos.insert method to create and upload the video.
        insert_request = youtube.videos().insert(
            part=",".join(body.keys()),
            body=body,
            media_body=MediaFileUpload(options.file, chunksize=-1, resumable=True)
        )

        yt.resumable_upload(insert_request)
    # This method implements an exponential backoff strategy to resume a
    # failed upload.
    def resumable_upload(insert_request):
        yt = yt_Class()
        response = None
        error = None
        retry = 0
        while response is None:
            try:
                print ("Uploading file...")
                status, response = insert_request.next_chunk()
                if response is not None:
                    if 'id' in response:
                        print ("Video id '%s' was successfully uploaded." % response['id'])
                    else:
                        exit("The upload failed with an unexpected response: %s" % response)
            except HttpError as e:
                if e.resp.status in yt.RETRIABLE_STATUS_CODES:
                    error = "A retriable HTTP error %d occurred:\n%s" % (e.resp.status,
                                                                        e.content)
                else:
                    raise
            except yt.RETRIABLE_EXCEPTIONS as e:
                error = "A retriable error occurred: %s" % e

            if error is not None:
                print (error)
                retry += 1
                if retry > yt.MAX_RETRIES:
                    exit("No longer attempting to retry.")

                max_sleep = 2 ** retry
                sleep_seconds = random.random() * max_sleep
                print ("Sleeping %f seconds and then retrying..." % sleep_seconds)
                time.sleep(sleep_seconds)