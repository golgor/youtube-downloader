import sys
from pytube import YouTube
import youtube_downloader.cli as cli


def get_title(yt):
    return yt.player_response['videoDetails']['title']

def print_info(yt):
    print(" Clip to Download ".center(100, "="))
    print(f"Author: {yt.author}")
    print(f"Title: {get_title(yt)}")
    print(f"Lenght: {yt.length}")
    print(f"Rating: {yt.rating}")
    print("="*100)

def download_single(yt):
    stream = yt.streams.filter(progressive=True).get_highest_resolution()
    stream.download(output_path=yt.author, filename=get_title(yt))


def download_batch(filename):
    with open(filename, "r") as f:
        content = f.read().split("\n")
    for video in content:
        print("="*100)
        print("Downloading video!")
        yt = YouTube(video)
        download_single(yt)
        print(f'Finished downloading "{get_title(yt)}"')
        print(f'Url: {video}')

if __name__ == "__main__":
    parser = cli.create_parser()
    args = parser()
    if args.file:
        download_batch(args.url)
    else:
        yt = YouTube(args.url)
        print_info(yt)
        if (answer:=input("Is this the video you want to download? (y/n)\n")) == "y" or "Y":
            download_single(yt)
        else:
            sys.exit(0)
