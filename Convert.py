from __future__ import print_function

import glob
import json
import os
from os.path import join, dirname
from watson_developer_cloud import SpeechToTextV1
from watson_developer_cloud.websocket import RecognizeCallback

# ///////////////////////////////////////////////////////////////////////////////////////////////////////
# Get these from the Blumix service page. There are not your Bluemix username and password
# ///////////////////////////////////////////////////////////////////////////////////////////////////////
speech_to_text = SpeechToTextV1(
    username='XXXXXXXX-XXXX-XXXXX-XXXXX-XXXXXXXXXXXX',
    password='XXXXXXXXXXXX',
    url='https://stream.watsonplatform.net/speech-to-text/api')

# The input file should already exist as a .flac file from "ffmpeg -i *.mov *.flac"
input_dir = "./1_Input_flca_Files/"
json_from_IBM_Watson_dir = "./2_Output_Files/"

#Debuggin
print(json.dumps(speech_to_text.list_models(), indent=2))
print(json.dumps(speech_to_text.get_model('en-US_BroadbandModel'), indent=2))

# ///////////////////////////////////////////////////////////////////////////////////////////////////////
# Sends the .flac file to IBM Watson
# NOTE: The .flac file must be under 100 MB. I use ffmpeg to convert the .mov file to .flac
# then use Audacity to compress the .flac file to under 100 MB
# You will recive JSON data that will be saved in json_from_IBM_Watson_dir
# ///////////////////////////////////////////////////////////////////////////////////////////////////////
list_of_files = glob.glob(input_dir + "*.flac")
for (finel_number, f_Name) in enumerate(list_of_files):
    print(str(finel_number) + ' - ' + f_Name)
    with open(join(dirname(__file__), f_Name),'rb') as audio_file:
        data=speech_to_text.recognize(audio=audio_file, content_type='audio/flac', timestamps=True,word_confidence=True)
        print (json.dumps(data,indent=2))
        output_file = json_from_IBM_Watson_dir+ os.path.splitext(os.path.basename(f_Name))[0] + '_json.text'
        with open(output_file, 'w') as output:
            json.dump(data, output)



import CreateTextFromJSON
list_of_files = glob.glob(json_from_IBM_Watson_dir + "*.text")
for (finel_number, f_Name) in enumerate(list_of_files):
    writer = CreateTextFromJSON.srtMakerFromText(f_Name).writeFile()
