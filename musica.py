from sys import argv
from pytube import Playlist
import os

link = argv[1]

p = Playlist(link)

dest = "Brani"

for yt in p.videos:

    print("Downloading -> " + yt.title)
    
    video = yt.streams.filter(only_audio = True).first()
    out_file = video.download(output_path=dest)
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp4'
    os.rename(out_file, new_file)

    print("Success")
