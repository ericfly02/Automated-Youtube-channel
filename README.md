# Youtube-Autmated-channel
Automated youtube bot which downloads tweets converts image to text and creates a video

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the dependencies.

Clone the repository:
```bash
git clone https://github.com/ericfly02/Youtube-Autmated-channel.git

cd Youtube-Autmated-channel
```
Create a virtual environment using python (so you don't install all the libraries on your computer)
```bash
pip install virtualenv # If you don't have virtualenv already installed:

virtualenv venv

.\env\Scripts\activate (to activate the virtual environment)

deactivate (to deactivate the virtual environment)
```

Install all the dependencies
```bash
pip install -r requirements.txt
```



## Usage

First thing you'd have to change both `config.json` file
```json
{
    "consumer_key": "YOUR_CONSUMER_KEY", 
    "consumer_secret": "YOUR_CONSUMER_SECRET",
    "access_token": "YOUR_ACCESS_TOKEN",
    "access_token_secret": "YOUR_ACCESS_TOKEN_SECRET"
}
```
and `client_secrets.json` file 
```json
{
    "web": {
      "client_id": "YOUR_CLIENT_ID",
      "client_secret": "YOUR_CLIENT_SECRET",
      "redirect_uris": [],
      "auth_uri": "https://accounts.google.com/o/oauth2/auth",
      "token_uri": "https://accounts.google.com/o/oauth2/token"
    }
  }
```
Then , you're ready to go 🚀🚀

Execute the program on the command line:
```bash
# If you're using Windows
python automation.py  

# If you're using Linux/MacOS
python3 automation.py  
```

Once the code has been executed, it will ask you to specify the twitter account user where you want to download the images from. And then you'll be asked for the number of images/post that you want to download.


You can follow those two video to set up all the credentials to be able to interact with Google's API:

[Set up youtube credentials (from minute 4:20 to 11:10)](https://www.youtube.com/watch?v=aFwZgth790Q)

[Upload videos publicly](https://www.youtube.com/watch?v=dhrv5RhKewA&t=623s)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. 😉

## License
[MIT](https://choosealicense.com/licenses/mit/)
