import youtube_dl

url = input("Enter URL of Video")

with youtube_dl.YoutubeDL() as ydl:
    ydl.download(url)