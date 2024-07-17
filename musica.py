import os
import argparse
from pytube import Playlist

def download_audio_from_playlist(link, dest="Brani"):
    try:
        p = Playlist(link)
    except Exception as e:
        print(f"Failed to fetch playlist: {e}")
        return

    if not os.path.exists(dest):
        os.makedirs(dest)
    
    print(f"Downloading {len(p.videos)} videos to {dest}")

    for yt in p.videos:
        print(f"Downloading -> {yt.title}")
        try:
            video = yt.streams.filter(only_audio=True).first()
            if video:
                out_file = video.download(output_path=dest)
                base, ext = os.path.splitext(out_file)
                new_file = base + '.mp4'
                os.rename(out_file, new_file)
                print(f"Success: {new_file}")
            else:
                print(f"No audio streams found for {yt.title}")
        except Exception as e:
            print(f"Failed to download {yt.title}: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download audio from a YouTube playlist.")
    parser.add_argument("link", help="The URL of the YouTube playlist")
    parser.add_argument("--dest", default="Brani", help="Destination directory to save audio files")
    
    args = parser.parse_args()
    download_audio_from_playlist(args.link, args.dest)
