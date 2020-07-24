# importing module
from pytube import YouTube
from pathlib import Path
import pyinputplus as pyip

program = True

# main loop
while program:
    # Getting YT link
    ytLink = pyip.inputURL('Provide YouTube link:')

    # Trying to create YT object
    try:
        yt = YouTube(ytLink)
    except:
        print('Error occured. It could be connection error or check your URL validity')
        program = False
        break
    quality = pyip.inputChoice(['high', 'low', 'only audio'], 'Choose quality: ')
    if quality == 'low':
        stream = yt.streams.get_lowest_resolution()
    elif quality == 'high':
        stream = yt.streams.get_highest_resolution()
    elif quality == 'only audio':
        stream = yt.streams.get_audio_only()

    path = str(Path('/Users/bartoszszadkowski/Downloads'))

    differentPath = pyip.inputYesNo('Would you like specify path to download?(y/n) (by default is: /Users/bartoszszadkowski/Download)')
    if differentPath == 'Yes':
        path = pyip.inputStr('Provide your path: ')

    try:
        stream.download(path)
    except:
        print('Some error occured. Check validity of your path.')
        program = False
        break

    program = False

print('done')
