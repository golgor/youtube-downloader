import argparse


welcome="Download youtube videos!"

file_help="Path to a file containing links to YouTube videos."
url_help="URL to download from"

def create_parser():
    parser = argparse.ArgumentParser(description=welcome, prog="youtube-downloader")
    parser.add_argument("url", help=url_help)
    parser.add_argument("--file", action="store_true", help=file_help, required=False)

    return parser.parse_args