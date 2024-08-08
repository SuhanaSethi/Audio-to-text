import assemblyai as aai
from hide_it import *
aai.settings.api_key= my_api_key

FILE_URL= "C:/Users/Suhana/Audio-to-text/santa-claus-a-reading-christmas-story-17777.mp3"
transcriber = aai.Transcriber()

transcript =transcriber.transcribe(FILE_URL)

if transcript.status == aai.TranscriptStatus.error:
    print(f"Error: {transcript.error}")
else:
    transcription_text = transcript.text
    print(f"Transcription: {transcription_text}")


    with open("text.txt", "w") as text_file:
        text_file.write(transcription_text)
