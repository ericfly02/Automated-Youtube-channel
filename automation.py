from twitterscrapper import initialize as initialize_twitter
from image_to_text import initialize as initialize_image

def main():
    #Defining user and number of tweets to fetch
    username = input("Enter the Twitter user: ")
    no_of_tweets = input("Enter the number of tweets to download: ")

    # We get the tweets from the user
    initialize_twitter(username, no_of_tweets)

    # We get the text from the images, create the video and upload it to youtube
    initialize_image(username)


if __name__ == '__main__':
    main()

# 