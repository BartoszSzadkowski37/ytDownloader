# importing module
from pytube import YouTube
from pathlib import Path
import pyinputplus as pyip
import logging

program = True

#yt = ''
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# main loop
while program:
    # Getting YT link
    ytLink = pyip.inputURL('Provide YouTube link:')

    # Trying to create YT object
    try:
        yt = YouTube(ytLink)
    except:
        print('Error occured. It could be connection error or check your URL validity')
        # program = False
        break
    # let user to choose quality of the movie or only audio
    quality = pyip.inputChoice(['high', 'low', 'only audio'], 'Choose quality: (high, low, only audio):')
    if quality == 'low':
        stream = yt.streams.get_lowest_resolution()
    elif quality == 'high':
        stream = yt.streams.get_highest_resolution()
    elif quality == 'only audio':
        stream = yt.streams.get_audio_only()

    # default path for downloaded files
    path = str(Path('/Users/bartoszszadkowski/Downloads'))

    # ask for different path if yes get from the user
    differentPath = pyip.inputYesNo('Would you like specify path to download?(y/n) (by default is: /Users/bartoszszadkowski/Download)')
    if differentPath == 'Yes':
        path = pyip.inputStr('Provide your path: ')
    # try to download the yt file
    try:
        stream.download(path)
    except:
        print('Some error occured. Check validity of your path.')
        # program = False
        break

    program = False

print('done')
