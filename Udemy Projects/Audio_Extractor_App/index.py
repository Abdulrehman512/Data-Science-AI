import moviepy.editor as mp
import os

path = input("Enter Path of Video File")

videoclip = mp.VideoClip(path)
audioclip = videoclip.audio
audioclip.write_audiofile("audio.mp3")