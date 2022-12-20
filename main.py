from api import upload, save_transcript

filename = "test.mp3"
audio_url = upload(filename)

save_transcript(audio_url, 'file_title')
