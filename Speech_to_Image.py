import openai
import json

OPENAI_API_KEY = "INSERT OPENAI KEY HERE" #add openai key here
openai.api_key = OPENAI_API_KEY

audio_file = open("C:\\Users\\saumi\\Downloads\\The_University_of_Texas_at_Dallas_2.m4a", "rb") #import audio file (add audio file path in the empty quotes)
audio = openai.Audio.transcribe("whisper-1", audio_file) #transcribe audio using whisper model

#access text from the whisper model output
transcription = str(audio)
data = json.loads(transcription)

#use the text from the whisper model output as the input to the dall E model
PROMPT = data['text']

#create an image from the input of the dall E model
response = openai.Image.create(
    prompt = PROMPT,
    n=1,
    size = "512x512"
)

#give a URL for the image that the dall E model creates
print(response["data"][0]["url"])