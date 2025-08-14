import os
import eyed3
import yaml

# Create a function that reads the audio files in mp3 formate from the
# `audio` directory and returns a list of them.
def get_audio_files(): 
  audio_files = []
  for file in os.listdir('audio'): 
    if file.endswith('.mp3'):
      audio_file = eyed3.load(os.path.join('audio', file))
      comments = ''
      if audio_file.tag.comments:
        for comment in audio_file.tag.comments:
          comments += comment.text + '\n'
      audio_files.append({
          'title': audio_file.tag.title,
          'comments': comments,
          'filename': '/audio' + file
      })
  return audio_files

print(yaml.dump(get_audio_files(), sort_keys=False))